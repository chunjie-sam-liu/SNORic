from django.shortcuts import render_to_response, render
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_protect
from django.http import Http404, HttpResponseRedirect, HttpResponse, JsonResponse
from django.core import serializers
from django.apps import apps

from .models import *
import json
import base64
import subprocess
import os.path, sys

# resource and r scripts dir
rcommand = '/usr/bin/Rscript'
rscript_dir = os.path.dirname(os.path.abspath(__file__)) + '/rscripts/'
resource_jons = os.path.dirname(os.path.abspath(__file__)) + '/resource/jsons/'
resource_pngs = os.path.dirname(os.path.abspath(__file__)) + '/resource/pngs/'


# main home page
def index(request):
    title = "SNORic"
    context = {"title": title}

    return render(request, 'snorna/index.html', context)

# contact info
def contact(request):
    title = "SNORic | Contact"
    context = {
        "title": title
    }
    return render(request, 'snorna/contact.html', context)


# faq
def faq(request):
    title = "SNORic | FAQ"
    context = {
        "title": title
    }

    return render(request, 'snorna/faq.html', context)


# methods
def methods(request):
    title = "SNORic | Methods"
    context = {
        "title": title
    }
    return render(request, 'snorna/methods.html', context)


def download(request):
    title = "SNORic | API"
    context = {
        "title": title
    }
    return render(request, 'snorna/download.html', context)


def statistics(request):
    title = "SNORic | Statistics"
    context = {
        "title": title,
    }
    return render(request, 'snorna/statistics.html', context)


# basic analysis
def basic(request):
    title = "SNORic | Basic"
    context = {
        "title": title
    }
    return render(request, 'basic/main.html', context)


def get_expression(request):
    q_name = request.GET["genes"]
    dataset_id =  request.GET["dataset_ids"]
    subtype_id = request.GET["subtype_id"]
    # subtype == "0"
    # subtype == "all"
    # subtype == "subtype"
    model_str = "snorna_expression_" + dataset_id.replace("TCGA-","")
    model = apps.get_model("snorna", model_str)
    snorna_expr = model.objects.using('snoric').filter(
        dataset_id__exact=dataset_id,
        snorna__exact=q_name).values('dataset_id',
                                     'snorna',
                                     'sample_id',
                                     'snorna_expression')
    return snorna_expr


def snorna_expr_table(request):
    title = "SNORic | snorna expression"
    context = {"title": title}
    return render(request, 'basic/dataTables/snorna_expr_table.html', context)


def api_snorna_expr(request):
    q_name = request.GET["genes"]
    dataset_id = request.GET["dataset_ids"]
    subtype_id = request.GET["subtype_id"]
    arg = base64.b64encode(q_name + "#" + dataset_id + "#" + subtype_id)
    cmd = [rcommand, rscript_dir + "basic_snorna_expr.r", arg]
    json_file = resource_jons + arg + ".snorna_expr.json"
    if not os.path.exists(json_file):
        subprocess.check_output(cmd, universal_newlines=True)
    data = json.load(open(json_file, 'r'))
    return JsonResponse(data, safe=False)

def api_tm_comparison(request):
    q_name = request.GET["genes"]
    dataset_id = request.GET["dataset_ids"]
    subtype_id = request.GET["subtype_id"]
    arg = base64.b64encode(q_name + "#" + dataset_id + "#" + subtype_id)
    return JsonResponse({'png_name': arg})

def tm_comparison_table(request):
    title = "SNORic | tm comparison"
    context = {"title": title}
    return render(request, 'basic/dataTables/tm_comparison_table.html', context)

def tm_comparison_table_png(request, encode):
    png = resource_pngs + encode + ".tm_comparison.png"
    if os.path.exists(png):
        with open(png) as f:
            return HttpResponse(f.read(), content_type = "image/png")
    else:
        return HttpResponse("Not enough samples!", content_type = "text/plain")

# survival
def survival_table(request):
    title = "SNORic | survival"
    context = {"title": title}
    return render(request, 'basic/dataTables/survival_table.html', context)


def survival_table_png(request, encode):
    encode = encode + ".survival.png"
    png = resource_pngs + encode
    with open(png) as f:
        return HttpResponse(f.read(), content_type="image/png")


def api_survival(request):
    # snorna = snorna_info.objects.using('snoric').get(snorna__exact=request.GET["genes"])
    q_name = request.GET["genes"]
    dataset_id = request.GET["dataset_ids"]
    subtype_id = request.GET["subtype_id"]
    arg = base64.b64encode(q_name + "#" + dataset_id + "#" + subtype_id)
    cmd = [rcommand, rscript_dir + "basic_survival.r", arg]
    json_file = resource_jons + arg + ".survival.json"
    if not os.path.exists(json_file):
        subprocess.check_output(cmd, universal_newlines=True)
    data = json.load(open(json_file, 'r'))
    return JsonResponse(data, safe=False)


# diff_subtype
def diff_subtype_table(request):
    title = "SNORic | diff_subtype"
    context = {"title": title}
    return render(request, 'basic/dataTables/diff_subtype_table.html', context)


def api_diff_subtype(request):
    # snorna = snorna_info.objects.using('snoric').get(snorna__exact=request.GET["genes"])
    q_name = request.GET["genes"]
    dataset_id = request.GET["dataset_ids"]
    arg = base64.b64encode(q_name + "#" + dataset_id)
    cmd = [rcommand, rscript_dir + "basic_diff_subtype.r", arg]
    json_file = resource_jons + arg + ".diff_subtype.json"
    if not os.path.exists(json_file):
        subprocess.check_output(cmd, universal_newlines=True)
    data = json.load(open(json_file, 'r'))
    return JsonResponse(data, safe=False)


def diff_subtype_table_png(request, encode):
    encode = encode + ".diff_subtype.png"
    png = resource_pngs + encode
    with open(png) as f:
        return HttpResponse(f.read(), content_type="image/png")


# corr_geneexpr
def api_corr_geneexpr(request):
    q_name = request.GET["genes"]
    dataset_id = request.GET["dataset_ids"]
    subtype_id = request.GET["subtype_id"]
    arg = base64.b64encode(q_name + "#" + dataset_id + "#" + subtype_id)
    cmd = [rcommand, rscript_dir + "basic_corr_geneexpr.r", arg]
    json_file = resource_jons + arg + ".corr_geneexpr.json"
    if not os.path.exists(json_file):
        subprocess.check_output(cmd, universal_newlines=True)
    data = json.load(open(json_file, 'r'))
    return JsonResponse(data, safe=False)

def corr_geneexpr_table(request):
    title = "SNORic | corr_geneexpr"
    context = {"title": title}
    return render(request, 'basic/dataTables/corr_geneexpr_table.html', context)

def corr_geneexpr_table_png(request, encode):
    encode = encode + ".corr_geneexpr.png"
    png = resource_pngs + encode
    with open(png) as f:
        return HttpResponse(f.read(), content_type="image/png")

# corr_splicing
def api_corr_splicing(request):
    q_name = request.GET["genes"]
    dataset_id = request.GET["dataset_ids"]
    subtype_id = request.GET["subtype_id"]
    arg = base64.b64encode(q_name + "#" + dataset_id + "#" + subtype_id)
    cmd = [rcommand, rscript_dir + "basic_corr_splicing.r", arg]
    json_file = resource_jons + arg + ".corr_splicing.json"
    if not os.path.exists(json_file):
        subprocess.check_output(cmd, universal_newlines=True)
    data = json.load(open(json_file, 'r'))
    return JsonResponse(data, safe=False)

def corr_splicing_table(request):
    title = "SNORic | corr_splicing"
    context = {"title": title}
    return render(request, 'basic/dataTables/corr_splicing_table.html', context)

def corr_splicing_table_png(request, encode):
    encode = encode + ".corr_splicing.png"
    png = resource_pngs + encode
    with open(png) as f:
        return HttpResponse(f.read(), content_type="image/png")


# corr_rppa
def corr_rppa_table(request):
    title = "SNORic | corr_rppa"
    context = {"title": title}
    return render(request, 'basic/dataTables/corr_rppa_table.html', context)

def api_corr_rppa(request):
    q_name = request.GET["genes"]
    dataset_id = request.GET["dataset_ids"]
    subtype_id = request.GET["subtype_id"]
    arg = base64.b64encode(q_name + "#" + dataset_id + "#" + subtype_id)
    cmd = [rcommand, rscript_dir + "basic_corr_rppa.r", arg]
    json_file = resource_jons + arg + ".corr_rppa.json"
    if not os.path.exists(json_file):
        subprocess.check_output(cmd, universal_newlines=True)
    data = json.load(open(json_file, 'r'))
    return JsonResponse(data, safe=False)

def corr_rppa_table_png(request, encode):
    encode = encode + ".corr_rppa.png"
    png = resource_pngs + encode
    with open(png) as f:
        return HttpResponse(f.read(), content_type="image/png")

# corr_cnv
def corr_cnv_table(request):
    title = "SNORic | corr_cnv"
    context = {"title": title}
    return render(request, 'basic/dataTables/corr_cnv_table.html', context)

def api_corr_cnv(request):
    q_name = request.GET["genes"]
    dataset_id = request.GET["dataset_ids"]
    subtype_id = request.GET["subtype_id"]
    arg = base64.b64encode(q_name + "#" + dataset_id + "#" + subtype_id)
    cmd = [rcommand, rscript_dir + "basic_corr_cnv.r", arg]
    json_file = resource_jons + arg + ".corr_cnv.json"
    if not os.path.exists(json_file):
        subprocess.check_output(cmd, universal_newlines=True)
    data = json.load(open(json_file, 'r'))
    return JsonResponse(data, safe=False)

def corr_cnv_table_png(request, encode):
    encode = encode + ".corr_cnv.png"
    png = resource_pngs + encode
    with open(png) as f:
        return HttpResponse(f.read(), content_type="image/png")


# methylation
def methylation_table(request):
    title = "SNORic | methylation"
    context = {"title": title}
    return render(request, 'basic/dataTables/methylation_table.html', context)

def methylation_table_png(request, encode):
    encode = encode + ".methylation.png"
    png = resource_pngs + encode
    with open(png) as f:
        return HttpResponse(f.read(), content_type="image/png")

def api_methylation(request):
    q_name = request.GET["genes"]
    dataset_id = request.GET["dataset_ids"]
    subtype_id = request.GET["subtype_id"]
    arg = base64.b64encode(q_name + "#" + dataset_id + "#" + subtype_id)
    cmd = [rcommand, rscript_dir + "basic_methylation.r", arg]
    json_file = resource_jons + arg + ".methylation.json"
    if not os.path.exists(json_file):
        subprocess.check_output(cmd, universal_newlines=True)
    data = json.load(open(json_file, 'r'))
    return JsonResponse(data, safe=False)

# total analysis
def analysis(request):
    title = "SNORic | Analysis"
    context = {
        "title": title
    }
    return render(request, 'analysis/main.html', context)


# analysis


#api_snorna_expr_bygene
def api_snorna_expr_bygene(request):
    q_name = request.GET["query_gene"]
    dataset_id = request.GET["dataset_ids"]
    arg = base64.b64encode(q_name + "#" + dataset_id)
    cmd = [rcommand, rscript_dir + "snorna_expr_bygene.r", arg]
    json_file = resource_jons + arg + ".snorna_expr_bygene.json"
    if not os.path.exists(json_file):
        subprocess.check_output(cmd, universal_newlines=True)
    data = json.load(open(json_file, 'r'))
    return JsonResponse(data, safe = False)

def snorna_expr_bygene_table(request):
    title = "Analysis-SNORic| expr"
    context = {"title": title}
    return render(request, "analysis/dataTables/snorna_expr_bygene_table.html")

# api_diff_subtype_bygene
def api_diff_subtype_bygene(request):
    q_name = request.GET["query_gene"]
    dataset_id = request.GET["dataset_ids"]
    arg = base64.b64encode(q_name + "#" + dataset_id)
    cmd = [rcommand, rscript_dir + "diff_subtype_bygene.r", arg]
    json_file = resource_jons + arg + ".diff_subtype_bygene.json"
    if not os.path.exists(json_file):
        subprocess.check_output(cmd, universal_newlines=True)
    data = json.load(open(json_file, 'r'))
    return JsonResponse(data, safe = False)

def diff_subtype_bygene_table(request):
    title = "Analysis-SNORic| subtype"
    context = {"title": title}
    return render(request, "analysis/dataTables/diff_subtype_bygene_table.html")

def diff_subtype_bygene_table_png(request, encode):
    encode = encode + ".diff_subtype_bygene.png"
    png = resource_pngs + encode
    with open(png) as f:
        return HttpResponse(f.read(), content_type="image/png")

# api_survival_bygene
def api_survival_bygene(request):
    q_name = request.GET["query_gene"]
    dataset_id = request.GET["dataset_ids"]
    arg = base64.b64encode(q_name + "#" + dataset_id)
    cmd = [rcommand, rscript_dir + "survival_bygene.r", arg]
    json_file = resource_jons + arg + ".survival_bygene.json"
    if not os.path.exists(json_file):
        subprocess.check_output(cmd, universal_newlines=True)
    data = json.load(open(json_file, 'r'))
    return JsonResponse(data, safe = False)

def survival_bygene_table(request):
    title = "Analysis-SNORic| survival"
    context = {"title": title}
    return render(request, "analysis/dataTables/survival_bygene_table.html")

def survival_bygene_table_png(request, encode):
    encode = encode + ".survival_bygene.png"
    png = resource_pngs + encode
    with open(png) as f:
        return HttpResponse(f.read(), content_type="image/png")

# api_corr_geneexpr_bygene
def api_corr_geneexpr_bygene(request):
    q_name = request.GET["query_gene"]
    dataset_id = request.GET["dataset_ids"]
    arg = base64.b64encode(q_name + "#" + dataset_id)
    cmd = [rcommand, rscript_dir + "corr_geneexpr_bygene.r", arg]
    json_file = resource_jons + arg + ".corr_geneexpr_bygene.json"
    if not os.path.exists(json_file):
        subprocess.check_output(cmd, universal_newlines=True)
    data = json.load(open(json_file, 'r'))
    return JsonResponse(data, safe = False)

def corr_geneexpr_bygene_table(request):
    title = "Analysis-SNORic| corr_geneexpr"
    context = {"title": title}
    return render(request, "analysis/dataTables/corr_geneexpr_bygene_table.html")

def corr_geneexpr_bygene_table_png(request, encode):
    encode = encode + ".corr_geneexpr_bygene.png"
    png = resource_pngs + encode
    with open(png) as f:
        return HttpResponse(f.read(), content_type="image/png")

# api_corr_geneexpr_bygene
def api_corr_splicing_bygene(request):
    q_name = request.GET["query_gene"]
    dataset_id = request.GET["dataset_ids"]
    arg = base64.b64encode(q_name + "#" + dataset_id)
    cmd = [rcommand, rscript_dir + "corr_splicing_bygene.r", arg]
    json_file = resource_jons + arg + ".corr_splicing_bygene.json"
    if not os.path.exists(json_file):
        subprocess.check_output(cmd, universal_newlines=True)
    data = json.load(open(json_file, 'r'))
    # data = '{"cj":"cj"}'
    return JsonResponse(data, safe = False)

def corr_splicing_bygene_table(request):
    title = "Analysis-SNORic| corr_splicing"
    context = {"title": title}
    return render(request, "analysis/dataTables/corr_splicing_bygene_table.html")

def corr_splicing_bygene_table_png(request, encode):
    encode = encode + ".corr_splicing_bygene.png"
    png = resource_pngs + encode
    with open(png) as f:
        return HttpResponse(f.read(), content_type="image/png")
# api_corr_rppa_bygene
def api_corr_rppa_bygene(request):
    q_name = request.GET["query_gene"]
    dataset_id = request.GET["dataset_ids"]
    arg = base64.b64encode(q_name + "#" + dataset_id)
    cmd = [rcommand, rscript_dir + "corr_rppa_bygene.r", arg]
    json_file = resource_jons + arg + ".corr_rppa_bygene.json"
    if not os.path.exists(json_file):
        subprocess.check_output(cmd, universal_newlines=True)
    data = json.load(open(json_file, 'r'))
    return JsonResponse(data, safe = False)

def corr_rppa_bygene_table(request):
    title = "Analysis-SNORic| corr_rppa"
    context = {"title": title}
    return render(request, "analysis/dataTables/corr_rppa_bygene_table.html")

def corr_rppa_bygene_table_png(request, encode):
    encode = encode + ".corr_rppa_bygene.png"
    png = resource_pngs + encode
    with open(png) as f:
        return HttpResponse(f.read(), content_type="image/png")

# api_corr_cnv_bygene
def api_corr_cnv_bygene(request):
    q_name = request.GET["query_gene"]
    dataset_id = request.GET["dataset_ids"]
    arg = base64.b64encode(q_name + "#" + dataset_id)
    cmd = [rcommand, rscript_dir + "corr_cnv_bygene.r", arg]
    json_file = resource_jons + arg + ".corr_cnv_bygene.json"
    if not os.path.exists(json_file):
        subprocess.check_output(cmd, universal_newlines=True)
    data = json.load(open(json_file, 'r'))
    return JsonResponse(data, safe=False)

def corr_cnv_bygene_table(request):
    title = "Analysis-SNORic| corr_cnv"
    context = {"title": title}
    return render(request, "analysis/dataTables/corr_cnv_bygene_table.html")

def corr_cnv_bygene_table_png(request, encode):
    encode = encode + ".corr_cnv_bygene.png"
    png = resource_pngs + encode
    with open(png) as f:
        return HttpResponse(f.read(), content_type="image/png")

# api_corr_cnv_bygene
def api_methylation_bygene(request):
    q_name = request.GET["query_gene"]
    dataset_id = request.GET["dataset_ids"]
    arg = base64.b64encode(q_name + "#" + dataset_id)
    cmd = [rcommand, rscript_dir + "methylation_bygene.r", arg]
    json_file = resource_jons + arg + ".methylation_bygene.json"
    if not os.path.exists(json_file):
        subprocess.check_output(cmd, universal_newlines=True)
    data = json.load(open(json_file, 'r'))
    return JsonResponse(data, safe=False)

def methylation_bygene_table(request):
    title = "Analysis-SNORic| methylation"
    context = {"title": title}
    return render(request, "analysis/dataTables/methylation_bygene_table.html")

def methylation_bygene_table_png(request, encode):
    encode = encode + ".methylation_bygene.png"
    png = resource_pngs + encode
    with open(png) as f:
        return HttpResponse(f.read(), content_type="image/png")


# access api data
# dataset summary api
def api_summary(reuqest):
    # return json format for ajax api
    dataset_summary = dataset.objects.using('snoric').all()
    return JsonResponse({"data": json.loads(serializers.serialize('json', dataset_summary))})


def api_subtype(request, dataset_id):
    subtype = clinical_subtype.objects.using('snoric').filter(dataset_id__exact=dataset_id)
    return HttpResponse(serializers.serialize('json', subtype), content_type="application/json")


def api_snorna_list(request, search):
    snorna_list = snorna_info.objects.using('snoric').filter(snorna__icontains=search).values('snorna', 'symbold')[:10]
    return JsonResponse(list(snorna_list), safe=False)

def api_snorna(request, search):
    snorna = snorna_info.objects.using('snoric').filter(snorna__exact=search).values('snorna')
    return JsonResponse(list(snorna), safe=False)

def api_gene_symbol_list(request, search):
    gene_symbol_list = gene_symbol_info.objects.using('snoric').filter(gene_symbol__istartswith=search).values('gene_symbol')[:10]
    return JsonResponse(list(gene_symbol_list), safe=False)

def api_gene_symbol(request, search):
    gene_symbol = gene_symbol_info.objects.using('snoric').filter(gene_symbol__istartswith=search).values('gene_symbol')
    return JsonResponse(list(gene_symbol), safe = False)

#def handler404(request):
#    response = render_to_response('404.html', {}, context_instance = RequestContext(request))
#    response.status_code = 404
#    return response

#def handler500(request):
#    response = render_to_response('500.html', {}, context_instance = RequestContext(request))
#    response.status_code = 500
 #   return response
