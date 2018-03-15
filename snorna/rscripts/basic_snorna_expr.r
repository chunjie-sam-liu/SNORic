#!/usr/bin/R
library(RMySQL)
library(stringr)
library(jsonlite)
library(tidyverse)
library(ggpubr)
library(ggsci)

# snorna_gene_snorna_pair

args <- commandArgs(TRUE)
# all
# args <- "VTg7RU5TRzAwMDAwMjAwNDYzO1NOT1JEMTE4I1RDR0EtQUNDI2FsbA=="
# 0
# args <- "VTg7RU5TRzAwMDAwMjAwNDYzO1NOT1JEMTE4I1RDR0EtQ0hPTCMw"
# Stage I args <- 'VTg7RU5TRzAwMDAwMjAwNDYzO1NOT1JEMTE4I1RDR0EtQUNDI1N0YWdlIEk='
arg_encode <- args[1]
arg_decode <- str_split(rawToChar(base64_dec(arg_encode)), "#", simplify = T)

# output dir
root <- "/home/liucj/web/snorna_data_portal"
resource_jsons = file.path(root, "snorna/resource/jsons")
# resource_jsons = './'
resource_pngs = file.path(root, "snorna/resource/pngs")
# resource_pngs = './'

q_name <- arg_decode[1, 1]
dataset_id <- arg_decode[1, 2]
subtype_id <- arg_decode[1, 3]

table_snorna_expression <- paste("snorna_snorna_expression", str_to_lower(str_replace(dataset_id,
    "TCGA-", "")), sep = "_")

con <- dbConnect(RMySQL::MySQL(), username = "snoric_username", password = "snoric_password",
    dbname = "snoric", host = "localhost")

res_snorna_expr <- dbSendQuery(con, statement = paste("SELECT * FROM ", table_snorna_expression,
    "WHERE snorna = ", paste("\"", q_name, "\"", sep = ""), "AND dataset_id = ",
    paste("\"", dataset_id, "\"", sep = ""), sep = " "))
snorna_expr <- dbFetch(res_snorna_expr, n = -1) %>% as_tibble()
dbClearResult(res_snorna_expr)

expr_normal <-
  snorna_expr %>%
  dplyr::filter(stringr::str_detect(sample_id, "Normal"))

if (!subtype_id %in% c("all", "0")) {
    res_clinical <- dbSendQuery(con, statement = str_c("SELECT * FROM snorna_clinical WHERE stage = ",
        str_c("\"", subtype_id, "\"", sep = ""), "AND dataset_id = ", str_c("\"",
            dataset_id, "\"", sep = ""), sep = " "))
    clinical <- dbFetch(res_clinical, n = -1) %>% as_tibble()
    dbClearResult(res_clinical)
    snorna_expr <- snorna_expr %>% semi_join(clinical, by = c("dataset_id", "sample_id"))
}

if (!subtype_id %in% c("all", "0")) {
  snorna_expr <- dplyr::bind_rows(snorna_expr, expr_normal)
}

plot_ready <- snorna_expr %>% drop_na() %>% mutate(type = str_split(sample_id, "-",
    simplify = T)[, 2], expr = log2(snorna_expression + 1)) %>% select(-id, -sample_id,
    -snorna_expression)

check_number <- plot_ready %>% group_by(type) %>% count() %>% mutate(tf = n >= 8) %>%
    .$tf

if (all(check_number) && length(check_number) == 2) {
    plot_ready %>%
        ggboxplot(x = "type", y = "expr", color = "type", add = "jitter") +
        ggpubr::stat_compare_means(method = "t.test") +
        scale_color_npg() +
        labs(x = "Type", y = "Expression (log2)")-> p
    ggsave(file.path(resource_pngs, str_c(arg_encode, "tm_comparison",
        "png", sep = ".")), plot = p, device = "png")
}

snorna_expr %>% write_json(path = file.path(resource_jsons, str_c(arg_encode, "snorna_expr",
    "json", sep = ".")))
dbDisconnect(con)
