from __future__ import unicode_literals

from django.db import models

# Create your models here.
class dataset(models.Model):
    dataset_id = models.CharField(max_length=225, null=True)
    source = models.CharField(max_length=225, null=True)
    cancer_type = models.CharField(max_length=225, null=True)
    dataset_description = models.CharField(max_length=225, null=True)
    normal_n = models.IntegerField(null=True)
    tumor_n = models.IntegerField(null=True)
    build = models.CharField(max_length=225, null=True)
    average_mappable_reads = models.IntegerField(null=True)
    snorna_n = models.IntegerField(null=True)
    snorna_rpkm_n = models.IntegerField(null=True)

    def __str__(self):
        return self.dataset_id
# clinical data
class clinical(models.Model):
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    time = models.IntegerField(null=True)
    status = models.IntegerField(null=True)
    subtype = models.CharField(max_length=225, null=True)
    stage = models.CharField(max_length=225, null=True)
    def __str_(self):
        return self.dataset_id

class genomic_analysis(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length=225, null=True)
    gene_expression = models.FloatField(null=True)
    mirna_expression = models.FloatField(null=True)
    cna = models.FloatField(null=True)
    protein_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna

# clinical subtype for select
class clinical_subtype(models.Model):
    dataset_id = models.CharField(max_length=225, null=True)
    subtype = models.CharField(max_length=225, null=True)
    state = models.CharField(max_length=225, null=True)
    n = models.IntegerField(null=True)
    def __str__(self):
        return self.dataset_id

# protein_symvbol map
class rppa_name_symbol(models.Model):
    protein = models.CharField(max_length = 225)
    gene_symbol = models.CharField(max_length = 225)

    def __str__(self):
        return self.protein

# snorna info
class snorna_info(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    chrom = models.CharField(max_length=45, null=True)
    strand = models.CharField(max_length=45, null=True)
    start = models.IntegerField(null=True)
    end = models.IntegerField(null=True)
    symbold = models.CharField(max_length=45, null=True)
    type=models.CharField(max_length=45, null=True)

    def __str__(self):
        return self.snorna

class gene_symbol_info(models.Model):
    gene_symbol = models.CharField(max_length=225)

    def __str__(self):
        return self.gene_symbol

# snorna_expression
class snorna_expression(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id_expression = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    snorna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna

# mrna_expression
class mrna_expression(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length= 225, null=True)
    host = models.IntegerField(null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna

# cnv
class cnv(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    copy = models.FloatField(null=True)

    def __str__(self):
        return self.snorna

# methylation
class methylation(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    chrom = models.CharField(max_length=10, null=True)
    strand = models.CharField(max_length=4, null=True)
    start = models.IntegerField(null=True)
    end = models.IntegerField(null=True)
    source = models.CharField(max_length=45, null=True)
    distance = models.IntegerField(null=True)
    meth_id = models.CharField(max_length=225, null=True)
    pos = models.IntegerField(null=True)
    level = models.FloatField(null=True)

    def __str__(self):
        return self.snorna

# protein_expression
class protein_expression(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    protein = models.CharField(max_length= 225, null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna

# gene snorna pair
class gene_snorna_pair(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length=225)

    def __str__(self):
        return self.snorna

# split whole table as cancer type

# for snorna_expression
class snorna_expression_ACC(models.Model):
    snorna = models.CharField(max_length=225, null = True)
    dataset_id = models.CharField(max_length=225, null = True)
    sample_id = models.CharField(max_length=225, null=True)
    snorna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class snorna_expression_BLCA(models.Model):
    snorna = models.CharField(max_length=225, null = True)
    dataset_id = models.CharField(max_length=225, null = True)
    sample_id = models.CharField(max_length=225, null=True)
    snorna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class snorna_expression_BRCA(models.Model):
    snorna = models.CharField(max_length=225, null = True)
    dataset_id = models.CharField(max_length=225, null = True)
    sample_id = models.CharField(max_length=225, null=True)
    snorna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class snorna_expression_CESC(models.Model):
    snorna = models.CharField(max_length=225, null = True)
    dataset_id = models.CharField(max_length=225, null = True)
    sample_id = models.CharField(max_length=225, null=True)
    snorna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class snorna_expression_CHOL(models.Model):
    snorna = models.CharField(max_length=225, null = True)
    dataset_id = models.CharField(max_length=225, null = True)
    sample_id = models.CharField(max_length=225, null=True)
    snorna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class snorna_expression_COAD(models.Model):
    snorna = models.CharField(max_length=225, null = True)
    dataset_id = models.CharField(max_length=225, null = True)
    sample_id = models.CharField(max_length=225, null=True)
    snorna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class snorna_expression_DLBC(models.Model):
    snorna = models.CharField(max_length=225, null = True)
    dataset_id = models.CharField(max_length=225, null = True)
    sample_id = models.CharField(max_length=225, null=True)
    snorna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class snorna_expression_ESCA(models.Model):
    snorna = models.CharField(max_length=225, null = True)
    dataset_id = models.CharField(max_length=225, null = True)
    sample_id = models.CharField(max_length=225, null=True)
    snorna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class snorna_expression_HNSC(models.Model):
    snorna = models.CharField(max_length=225, null = True)
    dataset_id = models.CharField(max_length=225, null = True)
    sample_id = models.CharField(max_length=225, null=True)
    snorna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class snorna_expression_KICH(models.Model):
    snorna = models.CharField(max_length=225, null = True)
    dataset_id = models.CharField(max_length=225, null = True)
    sample_id = models.CharField(max_length=225, null=True)
    snorna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class snorna_expression_KIRC(models.Model):
    snorna = models.CharField(max_length=225, null = True)
    dataset_id = models.CharField(max_length=225, null = True)
    sample_id = models.CharField(max_length=225, null=True)
    snorna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class snorna_expression_KIRP(models.Model):
    snorna = models.CharField(max_length=225, null = True)
    dataset_id = models.CharField(max_length=225, null = True)
    sample_id = models.CharField(max_length=225, null=True)
    snorna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class snorna_expression_LGG(models.Model):
    snorna = models.CharField(max_length=225, null = True)
    dataset_id = models.CharField(max_length=225, null = True)
    sample_id = models.CharField(max_length=225, null=True)
    snorna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class snorna_expression_LIHC(models.Model):
    snorna = models.CharField(max_length=225, null = True)
    dataset_id = models.CharField(max_length=225, null = True)
    sample_id = models.CharField(max_length=225, null=True)
    snorna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class snorna_expression_LUAD(models.Model):
    snorna = models.CharField(max_length=225, null = True)
    dataset_id = models.CharField(max_length=225, null = True)
    sample_id = models.CharField(max_length=225, null=True)
    snorna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class snorna_expression_LUSC(models.Model):
    snorna = models.CharField(max_length=225, null = True)
    dataset_id = models.CharField(max_length=225, null = True)
    sample_id = models.CharField(max_length=225, null=True)
    snorna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class snorna_expression_MESO(models.Model):
    snorna = models.CharField(max_length=225, null = True)
    dataset_id = models.CharField(max_length=225, null = True)
    sample_id = models.CharField(max_length=225, null=True)
    snorna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class snorna_expression_OV(models.Model):
    snorna = models.CharField(max_length=225, null = True)
    dataset_id = models.CharField(max_length=225, null = True)
    sample_id = models.CharField(max_length=225, null=True)
    snorna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class snorna_expression_PAAD(models.Model):
    snorna = models.CharField(max_length=225, null = True)
    dataset_id = models.CharField(max_length=225, null = True)
    sample_id = models.CharField(max_length=225, null=True)
    snorna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class snorna_expression_PCPG(models.Model):
    snorna = models.CharField(max_length=225, null = True)
    dataset_id = models.CharField(max_length=225, null = True)
    sample_id = models.CharField(max_length=225, null=True)
    snorna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class snorna_expression_PRAD(models.Model):
    snorna = models.CharField(max_length=225, null = True)
    dataset_id = models.CharField(max_length=225, null = True)
    sample_id = models.CharField(max_length=225, null=True)
    snorna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class snorna_expression_READ(models.Model):
    snorna = models.CharField(max_length=225, null = True)
    dataset_id = models.CharField(max_length=225, null = True)
    sample_id = models.CharField(max_length=225, null=True)
    snorna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class snorna_expression_SARC(models.Model):
    snorna = models.CharField(max_length=225, null = True)
    dataset_id = models.CharField(max_length=225, null = True)
    sample_id = models.CharField(max_length=225, null=True)
    snorna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class snorna_expression_SKCM(models.Model):
    snorna = models.CharField(max_length=225, null = True)
    dataset_id = models.CharField(max_length=225, null = True)
    sample_id = models.CharField(max_length=225, null=True)
    snorna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class snorna_expression_STAD(models.Model):
    snorna = models.CharField(max_length=225, null = True)
    dataset_id = models.CharField(max_length=225, null = True)
    sample_id = models.CharField(max_length=225, null=True)
    snorna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class snorna_expression_TGCT(models.Model):
    snorna = models.CharField(max_length=225, null = True)
    dataset_id = models.CharField(max_length=225, null = True)
    sample_id = models.CharField(max_length=225, null=True)
    snorna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class snorna_expression_THCA(models.Model):
    snorna = models.CharField(max_length=225, null = True)
    dataset_id = models.CharField(max_length=225, null = True)
    sample_id = models.CharField(max_length=225, null=True)
    snorna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class snorna_expression_THYM(models.Model):
    snorna = models.CharField(max_length=225, null = True)
    dataset_id = models.CharField(max_length=225, null = True)
    sample_id = models.CharField(max_length=225, null=True)
    snorna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class snorna_expression_UCEC(models.Model):
    snorna = models.CharField(max_length=225, null = True)
    dataset_id = models.CharField(max_length=225, null = True)
    sample_id = models.CharField(max_length=225, null=True)
    snorna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class snorna_expression_UCS(models.Model):
    snorna = models.CharField(max_length=225, null = True)
    dataset_id = models.CharField(max_length=225, null = True)
    sample_id = models.CharField(max_length=225, null=True)
    snorna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class snorna_expression_UVM(models.Model):
    snorna = models.CharField(max_length=225, null = True)
    dataset_id = models.CharField(max_length=225, null = True)
    sample_id = models.CharField(max_length=225, null=True)
    snorna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna

# for mrna expression
class mrna_expression_ACC(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length= 225, null=True)
    host = models.IntegerField(null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class mrna_expression_BLCA(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length= 225, null=True)
    host = models.IntegerField(null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class mrna_expression_BRCA(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length= 225, null=True)
    host = models.IntegerField(null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class mrna_expression_CESC(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length= 225, null=True)
    host = models.IntegerField(null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class mrna_expression_CHOL(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length= 225, null=True)
    host = models.IntegerField(null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class mrna_expression_COAD(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length= 225, null=True)
    host = models.IntegerField(null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class mrna_expression_DLBC(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length= 225, null=True)
    host = models.IntegerField(null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class mrna_expression_ESCA(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length= 225, null=True)
    host = models.IntegerField(null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class mrna_expression_HNSC(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length= 225, null=True)
    host = models.IntegerField(null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class mrna_expression_KICH(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length= 225, null=True)
    host = models.IntegerField(null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class mrna_expression_KIRC(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length= 225, null=True)
    host = models.IntegerField(null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class mrna_expression_KIRP(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length= 225, null=True)
    host = models.IntegerField(null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class mrna_expression_LGG(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length= 225, null=True)
    host = models.IntegerField(null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class mrna_expression_LIHC(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length= 225, null=True)
    host = models.IntegerField(null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class mrna_expression_LUAD(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length= 225, null=True)
    host = models.IntegerField(null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class mrna_expression_LUSC(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length= 225, null=True)
    host = models.IntegerField(null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class mrna_expression_MESO(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length= 225, null=True)
    host = models.IntegerField(null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class mrna_expression_OV(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length= 225, null=True)
    host = models.IntegerField(null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class mrna_expression_PAAD(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length= 225, null=True)
    host = models.IntegerField(null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class mrna_expression_PCPG(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length= 225, null=True)
    host = models.IntegerField(null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class mrna_expression_PRAD(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length= 225, null=True)
    host = models.IntegerField(null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class mrna_expression_READ(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length= 225, null=True)
    host = models.IntegerField(null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class mrna_expression_SARC(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length= 225, null=True)
    host = models.IntegerField(null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class mrna_expression_SKCM(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length= 225, null=True)
    host = models.IntegerField(null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class mrna_expression_STAD(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length= 225, null=True)
    host = models.IntegerField(null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class mrna_expression_TGCT(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length= 225, null=True)
    host = models.IntegerField(null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class mrna_expression_THCA(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length= 225, null=True)
    host = models.IntegerField(null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class mrna_expression_THYM(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length= 225, null=True)
    host = models.IntegerField(null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class mrna_expression_UCEC(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length= 225, null=True)
    host = models.IntegerField(null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class mrna_expression_UCS(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length= 225, null=True)
    host = models.IntegerField(null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class mrna_expression_UVM(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length= 225, null=True)
    host = models.IntegerField(null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna

# for cnv
class cnv_ACC(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    copy = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class cnv_BLCA(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    copy = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class cnv_BRCA(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    copy = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class cnv_CESC(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    copy = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class cnv_CHOL(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    copy = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class cnv_COAD(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    copy = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class cnv_DLBC(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    copy = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class cnv_ESCA(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    copy = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class cnv_HNSC(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    copy = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class cnv_KICH(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    copy = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class cnv_KIRC(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    copy = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class cnv_KIRP(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    copy = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class cnv_LGG(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    copy = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class cnv_LIHC(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    copy = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class cnv_LUAD(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    copy = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class cnv_LUSC(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    copy = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class cnv_MESO(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    copy = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class cnv_OV(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    copy = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class cnv_PAAD(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    copy = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class cnv_PCPG(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    copy = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class cnv_PRAD(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    copy = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class cnv_READ(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    copy = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class cnv_SARC(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    copy = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class cnv_SKCM(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    copy = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class cnv_STAD(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    copy = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class cnv_TGCT(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    copy = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class cnv_THCA(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    copy = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class cnv_THYM(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    copy = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class cnv_UCEC(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    copy = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class cnv_UCS(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    copy = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class cnv_UVM(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    copy = models.FloatField(null=True)

    def __str__(self):
        return self.snorna

# methylation
class methylation_ACC(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    chrom = models.CharField(max_length=10, null=True)
    strand = models.CharField(max_length=4, null=True)
    start = models.IntegerField(null=True)
    end = models.IntegerField(null=True)
    source = models.CharField(max_length=45, null=True)
    distance = models.IntegerField(null=True)
    meth_id = models.CharField(max_length=225, null=True)
    pos = models.IntegerField(null=True)
    level = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class methylation_BLCA(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    chrom = models.CharField(max_length=10, null=True)
    strand = models.CharField(max_length=4, null=True)
    start = models.IntegerField(null=True)
    end = models.IntegerField(null=True)
    source = models.CharField(max_length=45, null=True)
    distance = models.IntegerField(null=True)
    meth_id = models.CharField(max_length=225, null=True)
    pos = models.IntegerField(null=True)
    level = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class methylation_BRCA(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    chrom = models.CharField(max_length=10, null=True)
    strand = models.CharField(max_length=4, null=True)
    start = models.IntegerField(null=True)
    end = models.IntegerField(null=True)
    source = models.CharField(max_length=45, null=True)
    distance = models.IntegerField(null=True)
    meth_id = models.CharField(max_length=225, null=True)
    pos = models.IntegerField(null=True)
    level = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class methylation_CESC(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    chrom = models.CharField(max_length=10, null=True)
    strand = models.CharField(max_length=4, null=True)
    start = models.IntegerField(null=True)
    end = models.IntegerField(null=True)
    source = models.CharField(max_length=45, null=True)
    distance = models.IntegerField(null=True)
    meth_id = models.CharField(max_length=225, null=True)
    pos = models.IntegerField(null=True)
    level = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class methylation_CHOL(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    chrom = models.CharField(max_length=10, null=True)
    strand = models.CharField(max_length=4, null=True)
    start = models.IntegerField(null=True)
    end = models.IntegerField(null=True)
    source = models.CharField(max_length=45, null=True)
    distance = models.IntegerField(null=True)
    meth_id = models.CharField(max_length=225, null=True)
    pos = models.IntegerField(null=True)
    level = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class methylation_COAD(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    chrom = models.CharField(max_length=10, null=True)
    strand = models.CharField(max_length=4, null=True)
    start = models.IntegerField(null=True)
    end = models.IntegerField(null=True)
    source = models.CharField(max_length=45, null=True)
    distance = models.IntegerField(null=True)
    meth_id = models.CharField(max_length=225, null=True)
    pos = models.IntegerField(null=True)
    level = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class methylation_DLBC(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    chrom = models.CharField(max_length=10, null=True)
    strand = models.CharField(max_length=4, null=True)
    start = models.IntegerField(null=True)
    end = models.IntegerField(null=True)
    source = models.CharField(max_length=45, null=True)
    distance = models.IntegerField(null=True)
    meth_id = models.CharField(max_length=225, null=True)
    pos = models.IntegerField(null=True)
    level = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class methylation_ESCA(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    chrom = models.CharField(max_length=10, null=True)
    strand = models.CharField(max_length=4, null=True)
    start = models.IntegerField(null=True)
    end = models.IntegerField(null=True)
    source = models.CharField(max_length=45, null=True)
    distance = models.IntegerField(null=True)
    meth_id = models.CharField(max_length=225, null=True)
    pos = models.IntegerField(null=True)
    level = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class methylation_HNSC(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    chrom = models.CharField(max_length=10, null=True)
    strand = models.CharField(max_length=4, null=True)
    start = models.IntegerField(null=True)
    end = models.IntegerField(null=True)
    source = models.CharField(max_length=45, null=True)
    distance = models.IntegerField(null=True)
    meth_id = models.CharField(max_length=225, null=True)
    pos = models.IntegerField(null=True)
    level = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class methylation_KICH(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    chrom = models.CharField(max_length=10, null=True)
    strand = models.CharField(max_length=4, null=True)
    start = models.IntegerField(null=True)
    end = models.IntegerField(null=True)
    source = models.CharField(max_length=45, null=True)
    distance = models.IntegerField(null=True)
    meth_id = models.CharField(max_length=225, null=True)
    pos = models.IntegerField(null=True)
    level = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class methylation_KIRC(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    chrom = models.CharField(max_length=10, null=True)
    strand = models.CharField(max_length=4, null=True)
    start = models.IntegerField(null=True)
    end = models.IntegerField(null=True)
    source = models.CharField(max_length=45, null=True)
    distance = models.IntegerField(null=True)
    meth_id = models.CharField(max_length=225, null=True)
    pos = models.IntegerField(null=True)
    level = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class methylation_KIRP(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    chrom = models.CharField(max_length=10, null=True)
    strand = models.CharField(max_length=4, null=True)
    start = models.IntegerField(null=True)
    end = models.IntegerField(null=True)
    source = models.CharField(max_length=45, null=True)
    distance = models.IntegerField(null=True)
    meth_id = models.CharField(max_length=225, null=True)
    pos = models.IntegerField(null=True)
    level = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class methylation_LGG(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    chrom = models.CharField(max_length=10, null=True)
    strand = models.CharField(max_length=4, null=True)
    start = models.IntegerField(null=True)
    end = models.IntegerField(null=True)
    source = models.CharField(max_length=45, null=True)
    distance = models.IntegerField(null=True)
    meth_id = models.CharField(max_length=225, null=True)
    pos = models.IntegerField(null=True)
    level = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class methylation_LIHC(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    chrom = models.CharField(max_length=10, null=True)
    strand = models.CharField(max_length=4, null=True)
    start = models.IntegerField(null=True)
    end = models.IntegerField(null=True)
    source = models.CharField(max_length=45, null=True)
    distance = models.IntegerField(null=True)
    meth_id = models.CharField(max_length=225, null=True)
    pos = models.IntegerField(null=True)
    level = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class methylation_LUAD(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    chrom = models.CharField(max_length=10, null=True)
    strand = models.CharField(max_length=4, null=True)
    start = models.IntegerField(null=True)
    end = models.IntegerField(null=True)
    source = models.CharField(max_length=45, null=True)
    distance = models.IntegerField(null=True)
    meth_id = models.CharField(max_length=225, null=True)
    pos = models.IntegerField(null=True)
    level = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class methylation_LUSC(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    chrom = models.CharField(max_length=10, null=True)
    strand = models.CharField(max_length=4, null=True)
    start = models.IntegerField(null=True)
    end = models.IntegerField(null=True)
    source = models.CharField(max_length=45, null=True)
    distance = models.IntegerField(null=True)
    meth_id = models.CharField(max_length=225, null=True)
    pos = models.IntegerField(null=True)
    level = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class methylation_MESO(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    chrom = models.CharField(max_length=10, null=True)
    strand = models.CharField(max_length=4, null=True)
    start = models.IntegerField(null=True)
    end = models.IntegerField(null=True)
    source = models.CharField(max_length=45, null=True)
    distance = models.IntegerField(null=True)
    meth_id = models.CharField(max_length=225, null=True)
    pos = models.IntegerField(null=True)
    level = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class methylation_OV(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    chrom = models.CharField(max_length=10, null=True)
    strand = models.CharField(max_length=4, null=True)
    start = models.IntegerField(null=True)
    end = models.IntegerField(null=True)
    source = models.CharField(max_length=45, null=True)
    distance = models.IntegerField(null=True)
    meth_id = models.CharField(max_length=225, null=True)
    pos = models.IntegerField(null=True)
    level = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class methylation_PAAD(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    chrom = models.CharField(max_length=10, null=True)
    strand = models.CharField(max_length=4, null=True)
    start = models.IntegerField(null=True)
    end = models.IntegerField(null=True)
    source = models.CharField(max_length=45, null=True)
    distance = models.IntegerField(null=True)
    meth_id = models.CharField(max_length=225, null=True)
    pos = models.IntegerField(null=True)
    level = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class methylation_PCPG(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    chrom = models.CharField(max_length=10, null=True)
    strand = models.CharField(max_length=4, null=True)
    start = models.IntegerField(null=True)
    end = models.IntegerField(null=True)
    source = models.CharField(max_length=45, null=True)
    distance = models.IntegerField(null=True)
    meth_id = models.CharField(max_length=225, null=True)
    pos = models.IntegerField(null=True)
    level = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class methylation_PRAD(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    chrom = models.CharField(max_length=10, null=True)
    strand = models.CharField(max_length=4, null=True)
    start = models.IntegerField(null=True)
    end = models.IntegerField(null=True)
    source = models.CharField(max_length=45, null=True)
    distance = models.IntegerField(null=True)
    meth_id = models.CharField(max_length=225, null=True)
    pos = models.IntegerField(null=True)
    level = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class methylation_READ(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    chrom = models.CharField(max_length=10, null=True)
    strand = models.CharField(max_length=4, null=True)
    start = models.IntegerField(null=True)
    end = models.IntegerField(null=True)
    source = models.CharField(max_length=45, null=True)
    distance = models.IntegerField(null=True)
    meth_id = models.CharField(max_length=225, null=True)
    pos = models.IntegerField(null=True)
    level = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class methylation_SARC(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    chrom = models.CharField(max_length=10, null=True)
    strand = models.CharField(max_length=4, null=True)
    start = models.IntegerField(null=True)
    end = models.IntegerField(null=True)
    source = models.CharField(max_length=45, null=True)
    distance = models.IntegerField(null=True)
    meth_id = models.CharField(max_length=225, null=True)
    pos = models.IntegerField(null=True)
    level = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class methylation_SKCM(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    chrom = models.CharField(max_length=10, null=True)
    strand = models.CharField(max_length=4, null=True)
    start = models.IntegerField(null=True)
    end = models.IntegerField(null=True)
    source = models.CharField(max_length=45, null=True)
    distance = models.IntegerField(null=True)
    meth_id = models.CharField(max_length=225, null=True)
    pos = models.IntegerField(null=True)
    level = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class methylation_STAD(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    chrom = models.CharField(max_length=10, null=True)
    strand = models.CharField(max_length=4, null=True)
    start = models.IntegerField(null=True)
    end = models.IntegerField(null=True)
    source = models.CharField(max_length=45, null=True)
    distance = models.IntegerField(null=True)
    meth_id = models.CharField(max_length=225, null=True)
    pos = models.IntegerField(null=True)
    level = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class methylation_TGCT(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    chrom = models.CharField(max_length=10, null=True)
    strand = models.CharField(max_length=4, null=True)
    start = models.IntegerField(null=True)
    end = models.IntegerField(null=True)
    source = models.CharField(max_length=45, null=True)
    distance = models.IntegerField(null=True)
    meth_id = models.CharField(max_length=225, null=True)
    pos = models.IntegerField(null=True)
    level = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class methylation_THCA(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    chrom = models.CharField(max_length=10, null=True)
    strand = models.CharField(max_length=4, null=True)
    start = models.IntegerField(null=True)
    end = models.IntegerField(null=True)
    source = models.CharField(max_length=45, null=True)
    distance = models.IntegerField(null=True)
    meth_id = models.CharField(max_length=225, null=True)
    pos = models.IntegerField(null=True)
    level = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class methylation_THYM(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    chrom = models.CharField(max_length=10, null=True)
    strand = models.CharField(max_length=4, null=True)
    start = models.IntegerField(null=True)
    end = models.IntegerField(null=True)
    source = models.CharField(max_length=45, null=True)
    distance = models.IntegerField(null=True)
    meth_id = models.CharField(max_length=225, null=True)
    pos = models.IntegerField(null=True)
    level = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class methylation_UCEC(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    chrom = models.CharField(max_length=10, null=True)
    strand = models.CharField(max_length=4, null=True)
    start = models.IntegerField(null=True)
    end = models.IntegerField(null=True)
    source = models.CharField(max_length=45, null=True)
    distance = models.IntegerField(null=True)
    meth_id = models.CharField(max_length=225, null=True)
    pos = models.IntegerField(null=True)
    level = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class methylation_UCS(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    chrom = models.CharField(max_length=10, null=True)
    strand = models.CharField(max_length=4, null=True)
    start = models.IntegerField(null=True)
    end = models.IntegerField(null=True)
    source = models.CharField(max_length=45, null=True)
    distance = models.IntegerField(null=True)
    meth_id = models.CharField(max_length=225, null=True)
    pos = models.IntegerField(null=True)
    level = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class methylation_UVM(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    sample_id = models.CharField(max_length=225, null=True)
    chrom = models.CharField(max_length=10, null=True)
    strand = models.CharField(max_length=4, null=True)
    start = models.IntegerField(null=True)
    end = models.IntegerField(null=True)
    source = models.CharField(max_length=45, null=True)
    distance = models.IntegerField(null=True)
    meth_id = models.CharField(max_length=225, null=True)
    pos = models.IntegerField(null=True)
    level = models.FloatField(null=True)

    def __str__(self):
        return self.snorna

# protein expression
class protein_expression_ACC(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    protein = models.CharField(max_length= 225, null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class protein_expression_BLCA(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    protein = models.CharField(max_length= 225, null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class protein_expression_BRCA(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    protein = models.CharField(max_length= 225, null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class protein_expression_CESC(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    protein = models.CharField(max_length= 225, null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class protein_expression_CHOL(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    protein = models.CharField(max_length= 225, null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class protein_expression_COAD(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    protein = models.CharField(max_length= 225, null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class protein_expression_DLBC(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    protein = models.CharField(max_length= 225, null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class protein_expression_ESCA(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    protein = models.CharField(max_length= 225, null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class protein_expression_HNSC(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    protein = models.CharField(max_length= 225, null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class protein_expression_KICH(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    protein = models.CharField(max_length= 225, null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class protein_expression_KIRC(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    protein = models.CharField(max_length= 225, null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class protein_expression_KIRP(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    protein = models.CharField(max_length= 225, null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class protein_expression_LGG(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    protein = models.CharField(max_length= 225, null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class protein_expression_LIHC(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    protein = models.CharField(max_length= 225, null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class protein_expression_LUAD(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    protein = models.CharField(max_length= 225, null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class protein_expression_LUSC(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    protein = models.CharField(max_length= 225, null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class protein_expression_MESO(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    protein = models.CharField(max_length= 225, null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class protein_expression_OV(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    protein = models.CharField(max_length= 225, null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class protein_expression_PAAD(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    protein = models.CharField(max_length= 225, null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class protein_expression_PCPG(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    protein = models.CharField(max_length= 225, null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class protein_expression_PRAD(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    protein = models.CharField(max_length= 225, null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class protein_expression_READ(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    protein = models.CharField(max_length= 225, null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class protein_expression_SARC(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    protein = models.CharField(max_length= 225, null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class protein_expression_SKCM(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    protein = models.CharField(max_length= 225, null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class protein_expression_STAD(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    protein = models.CharField(max_length= 225, null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class protein_expression_TGCT(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    protein = models.CharField(max_length= 225, null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class protein_expression_THCA(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    protein = models.CharField(max_length= 225, null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class protein_expression_THYM(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    protein = models.CharField(max_length= 225, null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class protein_expression_UCEC(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    protein = models.CharField(max_length= 225, null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class protein_expression_UCS(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    protein = models.CharField(max_length= 225, null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna
class protein_expression_UVM(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    protein = models.CharField(max_length= 225, null=True)
    spearman_corr = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    fdr = models.FloatField(null=True)
    sample_id = models.CharField(max_length=225, null=True)
    rna_expression = models.FloatField(null=True)

    def __str__(self):
        return self.snorna

# for gene snorna pair
class gene_snorna_pair_ACC(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length=225)

    def __str__(self):
        return self.snorna
class gene_snorna_pair_BLCA(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length=225)

    def __str__(self):
        return self.snorna
class gene_snorna_pair_BRCA(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length=225)

    def __str__(self):
        return self.snorna
class gene_snorna_pair_CESC(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length=225)

    def __str__(self):
        return self.snorna
class gene_snorna_pair_CHOL(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length=225)

    def __str__(self):
        return self.snorna
class gene_snorna_pair_COAD(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length=225)

    def __str__(self):
        return self.snorna
class gene_snorna_pair_DLBC(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length=225)

    def __str__(self):
        return self.snorna
class gene_snorna_pair_ESCA(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length=225)

    def __str__(self):
        return self.snorna
class gene_snorna_pair_HNSC(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length=225)

    def __str__(self):
        return self.snorna
class gene_snorna_pair_KICH(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length=225)

    def __str__(self):
        return self.snorna
class gene_snorna_pair_KIRC(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length=225)

    def __str__(self):
        return self.snorna
class gene_snorna_pair_KIRP(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length=225)

    def __str__(self):
        return self.snorna
class gene_snorna_pair_LGG(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length=225)

    def __str__(self):
        return self.snorna
class gene_snorna_pair_LIHC(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length=225)

    def __str__(self):
        return self.snorna
class gene_snorna_pair_LUAD(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length=225)

    def __str__(self):
        return self.snorna
class gene_snorna_pair_LUSC(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length=225)

    def __str__(self):
        return self.snorna
class gene_snorna_pair_MESO(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length=225)

    def __str__(self):
        return self.snorna
class gene_snorna_pair_OV(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length=225)

    def __str__(self):
        return self.snorna
class gene_snorna_pair_PAAD(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length=225)

    def __str__(self):
        return self.snorna
class gene_snorna_pair_PCPG(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length=225)

    def __str__(self):
        return self.snorna
class gene_snorna_pair_PRAD(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length=225)

    def __str__(self):
        return self.snorna
class gene_snorna_pair_READ(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length=225)

    def __str__(self):
        return self.snorna
class gene_snorna_pair_SARC(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length=225)

    def __str__(self):
        return self.snorna
class gene_snorna_pair_SKCM(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length=225)

    def __str__(self):
        return self.snorna
class gene_snorna_pair_STAD(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length=225)

    def __str__(self):
        return self.snorna
class gene_snorna_pair_TGCT(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length=225)

    def __str__(self):
        return self.snorna
class gene_snorna_pair_THCA(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length=225)

    def __str__(self):
        return self.snorna
class gene_snorna_pair_THYM(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length=225)

    def __str__(self):
        return self.snorna
class gene_snorna_pair_UCEC(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length=225)

    def __str__(self):
        return self.snorna
class gene_snorna_pair_UCS(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length=225)

    def __str__(self):
        return self.snorna
class gene_snorna_pair_UVM(models.Model):
    snorna = models.CharField(max_length=225, null=True)
    dataset_id = models.CharField(max_length=225, null=True)
    gene_symbol = models.CharField(max_length=225)

    def __str__(self):
        return self.snorna

# for RNA splicing
