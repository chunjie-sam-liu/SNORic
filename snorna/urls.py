from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^contact/$', views.contact, name = 'contact'),
    url(r'^faq/$', views.faq, name = 'faq'),
    url(r'^methods/$', views.methods, name = 'methods'),
    url(r'^download/$', views.download, name = 'download'),

    # statistics
    url(r'^statistics/$', views.statistics, name = 'statistics'),

    # basic analysis
    url(r'^basic/$', views.basic, name='basic'),
    # snorna expression
    url(r'^basic/snorna_expr_table/$', views.snorna_expr_table, name='snorna_expr_table'),
    url(r'^api/snorna_expr/$', views.api_snorna_expr, name='api_snorna_expr'),

    # tumor normal comparison
    url(r'basic/tm_comparison_table/$', views.tm_comparison_table, name='tm_comparison_table'),
    url(r'api/tm_comparison/$', views.api_tm_comparison, name='api_tm_comparison'),
    url(r'^basic/tm_comparison_table/png/(?P<encode>.*)$', views.tm_comparison_table_png, name="tm_comparison_table_png"),

    # survival
    url(r'^basic/survival_table/$', views.survival_table, name="survival_table"),
    url(r'^basic/survival_table/png/(?P<encode>.*)$', views.survival_table_png, name="survival_table_png"),
    url(r'^api/survival/$', views.api_survival, name="api_survival"),

    # diff_subtype
    url(r'^api/diff_subtype/$', views.api_diff_subtype, name="api_diff_subtype"),
    url(r'^basic/diff_subtype_table/$', views.diff_subtype_table, name='diff_subtype_table'),
    url(r'^basic/diff_subtype_table/png/(?P<encode>.*)$', views.diff_subtype_table_png, name="diff_subtype_table_png"),

    # corr_geneexpr
    url(r'^api/corr_geneexpr/$', views.api_corr_geneexpr, name="api_corr_geneexpr"),
    url(r'^basic/corr_geneexpr_table/$', views.corr_geneexpr_table, name='corr_geneexpr_table'),
    url(r'^basic/corr_geneexpr_table/png/(?P<encode>.*)$', views.corr_geneexpr_table_png, name='corr_geneexpr_table_png'),

    # corr_splicing
    url(r'^api/corr_splicing/$', views.api_corr_splicing, name="api_corr_splicing"),
    url(r'^basic/corr_splicing_table/$', views.corr_splicing_table, name='corr_splicing_table'),
    url(r'^basic/corr_splicing_table/png/(?P<encode>.*)$', views.corr_splicing_table_png, name='corr_splicing_table_png'),


    # corr_rppa
    url(r'^basic/corr_rppa_table/$', views.corr_rppa_table, name="corr_rppa_table"),
    url(r'^basic/corr_rppa_table/png/(?P<encode>.*)$', views.corr_rppa_table_png, name="corr_rppa_table_png"),
    url(r'^api/corr_rppa/$', views.api_corr_rppa, name="api_corr_rppa"),

    # corr_cnv
    url(r'^basic/corr_cnv_table/$', views.corr_cnv_table, name="corr_cnv_table"),
    url(r'^basic/corr_cnv_table/png/(?P<encode>.*)$', views.corr_cnv_table_png, name="corr_cnv_table_png"),
    url(r'^api/corr_cnv/$', views.api_corr_cnv, name="api_corr_cnv"),

    # methylation
    url(r'^basic/methylation_table/$', views.methylation_table, name="methylation_table"),
    url(r'^basic/methylation_table/png/(?P<encode>.*)$', views.methylation_table_png, name="methylation_table_png"),
    url(r'^api/methylation/$', views.api_methylation, name="api_methylation"),

    # total analysis
    url(r'^analysis/$', views.analysis, name = 'analysis'),
    # api
    url(r'^api/summary$', views.api_summary, name='api_summary'),
    url(r'^api/subtype/(?P<dataset_id>TCGA-\w*)$', views.api_subtype, name = 'api_subtype'),
    url(r'^api/snorna_list/(?P<search>.*)$', views.api_snorna_list, name='api_snorna_list'),
    url(r'^api/snorna/(?P<search>.*)$', views.api_snorna, name='api_snorna'),

    # search gene symbol
    url(r'api/gene_symbol_list/(?P<search>.*)$', views.api_gene_symbol_list, name='api_gene_symbol_list'),
    url(r'api/gene_symbol/(?P<search>.*)$', views.api_gene_symbol, name='api_gene_symbol'),

    # cnv_corr_bygene
    url(r'api/corr_cnv_bygene/$', views.api_corr_cnv_bygene, name = "api_corr_cnv_bygene"),


    # snorna_expr_bygene
    url(r'api/snorna_expr_bygene/$', views.api_snorna_expr_bygene, name="api_snorna_expr_bygene"),
    url(r'basic/snorna_expr_bygene_table/$', views.snorna_expr_bygene_table, name = "snorna_expr_bygene_table"),

    # diff_subtype_bygene
    url(r'api/diff_subtype_bygene/$', views.api_diff_subtype_bygene, name = "api_diff_subtype_bygene"),
    url(r'basic/diff_subtype_bygene_table/$', views.diff_subtype_bygene_table, name = "diff_subtype_bygene_table"),
    url(r'basic/diff_subtype_bygene_table/png/(?P<encode>.*)$', views.diff_subtype_bygene_table_png, name = "diff_subtype_bygene_table_png"),

    # survival_bygene
    url(r'api/survival_bygene/$', views.api_survival_bygene, name = "api_survival_bygene"),
    url(r'basic/survival_bygene_table/$', views.survival_bygene_table, name = "survival_bygene_table"),
    url(r'basic/survival_bygene_table/png/(?P<encode>.*)$', views.survival_bygene_table_png, name = "survival_bygene_table_png"),

    # mrna expression
    url(r'api/corr_geneexpr_bygene/$', views.api_corr_geneexpr_bygene, name = "api_corr_geneexpr_bygene"),
    url(r'basic/corr_geneexpr_bygene_table/$', views.corr_geneexpr_bygene_table, name="corr_geneexpr_bygene_table"),
    url(r'basic/corr_geneexpr_bygene_table/png/(?P<encode>.*)$', views.corr_geneexpr_bygene_table_png, name="corr_geneexpr_bygene_table_png"),

    # splicing gene based
    url(r'api/corr_splicing_bygene/$', views.api_corr_splicing_bygene, name = "api_corr_splicing_bygene"),
    url(r'basic/corr_splicing_bygene_table/$', views.corr_splicing_bygene_table, name="corr_splicing_bygene_table"),
    url(r'basic/corr_splicing_bygene_table/png/(?P<encode>.*)$', views.corr_splicing_bygene_table_png, name="corr_splicing_bygene_table_png"),

    # protein
    url(r'api/corr_rppa_bygene/$', views.api_corr_rppa_bygene, name="api_corr_rppa_bygene"),
    url(r'basic/corr_rppa_bygene_table/$', views.corr_rppa_bygene_table, name="corr_rppa_bygene_table"),
    url(r'basic/corr_rppa_bygene_table/png/(?P<encode>.*)$', views.corr_rppa_bygene_table_png, name="corr_rppa_bygene_table_png"),

    # cnv
    url(r'api/corr_cnv_bygene/$', views.api_corr_cnv_bygene, name="api_corr_cnv_bygene"),
    url(r'basic/corr_cnv_bygene_table/$', views.corr_cnv_bygene_table, name="corr_cnv_bygene_table"),
    url(r'basic/corr_cnv_bygene_table/png/(?P<encode>.*)$', views.corr_cnv_bygene_table_png, name="corr_cnv_bygene_table_png"),    # cnv
    url(r'api/methylation_bygene/$', views.api_methylation_bygene, name="api_methylation_bygene"),
    url(r'basic/methylation_bygene_table/$', views.methylation_bygene_table, name="methylation_bygene_table"),
    url(r'basic/methylation_bygene_table/png/(?P<encode>.*)$', views.methylation_bygene_table_png, name="methylation_bygene_table_png"),


    ]
