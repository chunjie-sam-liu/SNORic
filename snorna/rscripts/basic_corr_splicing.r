library(magrittr)
# library(RMySQL)
library(ggplot2)
args <- commandArgs(TRUE)
# all
# args <- 'VTg7RU5TRzAwMDAwMjAwNDYzO1NOT1JEMTE4I1RDR0EtQUNDI2FsbA=='
# 0
# args <- 'VTg7RU5TRzAwMDAwMjAwNDYzO1NOT1JEMTE4I1RDR0EtQ0hPTCMw'
# Stage I
# args <- 'VTg7RU5TRzAwMDAwMjAwNDYzO1NOT1JEMTE4I1RDR0EtQUNDI1N0YWdlIEk='
arg_encode <- args[1]
arg_decode <- stringr::str_split(rawToChar(jsonlite::base64_dec(arg_encode)),"#", simplify=T)

# output dir
root <- "/home/liucj/web/snorna_data_portal"
rds_gz <- file.path(root, 'snorna/resource/rds_gz')
resource_jsons = file.path(root, 'snorna/resource/jsons')
# resource_jsons = "./"
resource_pngs = file.path(root, 'snorna/resource/pngs')
# resource_pngs = "./"

q_name <- arg_decode[1,1]
dataset_id <- arg_decode[1,2]
subtype_id <- "all"

cancer_type <- stringr::str_replace(string = dataset_id, pattern = "TCGA-", replacement = "")
rds_pair<- glue::glue("rna_splicing_pair_{cancer_type}.rds.gz")
rds_file <- file.path(rds_gz, rds_pair)

df <- readr::read_rds(path = rds_file)

df %>%
    dplyr::filter(snorna == q_name) %>%
    dplyr::mutate(encode = paste(arg_encode, snorna, gene, sep = ".")) %>%
    dplyr::distinct() %>%
    dplyr::mutate_all(.funs = dplyr::funs(ifelse(is.na(.), "-", .))) -> corr_data_json
jsonlite::write_json(corr_data_json, path = file.path(resource_jsons, glue::glue("{arg_encode}.corr_splicing.json")))

psi <- readr::read_rds(file.path(rds_gz, glue::glue("rna_splicing_value_{cancer_type}.rds.gz"))) %>%
  dplyr::filter(snorna == q_name) %>%
  tidyr::gather(sample_id, value, -c(snorna, gene))

# snorna expression
# database_table <- paste("snorna_snorna_expression_", stringr::str_to_lower(cancer_type), sep = "")
# con <- dbConnect(RMySQL::MySQL(), username = "snoric_username", password="snoric_password", dbname="snoric", host="localhost")
# snorna_expr_sq <- dbSendQuery(con, statement = paste(
#                        "SELECT * FROM ", database_table,
#                        "WHERE snorna = ", paste('"',q_name,'"', sep=''),
#                        "AND dataset_id = ",
#                        paste('"',dataset_id,'"', sep = ""), sep=" "))
# snorna_expr <- dbFetch(snorna_expr_sq, n = -1) %>% tibble::as_tibble()
# dbClearResult(snorna_expr_sq)
# dbDisconnect(con)

snorna_expr <- readr::read_rds(file.path(rds_gz, glue::glue("snorna_expression.{cancer_type}.rds.gz"))) %>%
    dplyr::filter(snorna == q_name) %>%
    tidyr::gather(key = sample_id, value = snorna_expression, -c(snorna, dataset_id))

snorna_expr %>%
    dplyr::select(snorna, sample_id, snorna_expression) %>%
    dplyr::mutate(sample_id = purrr::map_chr(.x = sample_id, .f = function(.x){
        stringr::str_split(.x, pattern = "-", simplify = T)[,c(3,4,5)] %>% stringr::str_c(collapse="_")
        })) %>%
    dplyr::inner_join(psi, by = c("sample_id", "snorna")) %>%
    tidyr::drop_na(value, snorna_expression) %>%
    dplyr::distinct() -> plot_ready

plot_point <- function(.df){
    .df %>%
    ggplot(aes(x = rank(log2(snorna_expression + 1)), y = rank(value))) +
        geom_point(color = "#ca2015") +
        geom_smooth(method=lm, se = FALSE, fullrange=TRUE, color = "#1abc9c") +
        theme_bw() +
        theme(panel.border = element_blank(),
            panel.grid.major = element_blank(),
            panel.grid.minor = element_blank(),
            axis.line = element_line(color = "black")
            ) +
        labs(
            x = "snoRNA expression (rank)",
            y = "PSI value of splicing (rank)"
            )->p
    return(p)
}
plot_ready %>%
    dplyr::group_by(snorna, gene) %>%
    purrr::by_slice(plot_point) %>%
    dplyr::transmute(
            filename = stringr::str_c(
            arg_encode,
            snorna,
            gene,
            "corr_splicing",
            "png",
            sep = "."
            ),
            plot = .out
    ) %>%
    purrr::pwalk(ggsave, path = resource_pngs, device = "png")
