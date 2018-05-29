from django.shortcuts import render
from django.http import HttpResponse
from website.helper import *
import urllib.request

# Create your views here.

def index(request):

    return render(request, "pages/main.html")

def developers(request):

    return render(request, "pages/developers.html")

#  Testing Views in development
def sample(request):

	return render(request, "sample.html")

def test(request):

    indicators = {"NY.GNP.PCAP.PP.KD" : "GNI per capita, PPP (constant 2011 international $)","NY.GDP.PCAP.PP.KD" : "GDP per capita, PPP (constant 2011 international $)", "SP.DYN.LE00.IN":"Life expectancy at birth, total (years)", "SE.XPD.TOTL.GD.ZS":"Government expenditure on education, total (% of GDP)", "TX.VAL.OTHR.ZS.WT":"Computer, communications and other services (% of commercial service exports)", "EG.ELC.ACCS.ZS":"Access to electricity (% of population)", "FB.CBK.BRCH.P5":"Commercial bank branches (per 100,000 adults)", "MS.MIL.TOTL.P1":"Armed forces personnel, total"}

    # "NY.ADJ.NNTY.PC.KD":"Adjusted net national income per capita (constant 2010 US$)", "MS.MIL.TOTL.P1":"Armed forces personnel, total", "SP.REG.BRTH.ZS":"Completeness of birth registration (%)", "SE.COM.DURS":"Compulsory education, duration (years)"
    
    return render(request, "test.html", {"indicators":indicators})

def customHDI(request):

    ids = [request.POST.get('ind1'),request.POST.get('ind2'),request.POST.get('ind3'),request.POST.get('ind4'),request.POST.get('ind5')]
    coefs = [request.POST.get('coef1'),request.POST.get('coef2'),request.POST.get('coef3'),request.POST.get('coef4'),request.POST.get('coef5')]

    id_one   = getIndicatorName(ids[0])
    id_two   = getIndicatorName(ids[1])
    id_three = getIndicatorName(ids[2])
    id_four  = getIndicatorName(ids[3])
    id_five  = getIndicatorName(ids[4])

    coef_one   = coefs[0]
    coef_two   = coefs[1]
    coef_three = coefs[2]
    coef_four  = coefs[3]
    coef_five  = coefs[4]

    # TO-DO: CHECK IF any coef == 0 remove from the list

    year = getRecentOfAll(ids)
    
    # Handle form data here
    data = handleData(request, year, ids, coefs)

    # dump = json.dumps({"result": data})
    # return HttpResponse(dump, content_type='application/json')
    return render(request, "custom.html", {"id_one":id_one,"id_two":id_two,"id_three":id_three,"id_four":id_four,"id_five":id_five, "coef_one":coef_one, "coef_two":coef_two, "coef_three":coef_three, "coef_four":coef_four, "coef_five":coef_five,"data":data})

def example(request):
    # GNI per capita, PPP (constant 2011 international $) (NY.GNP.PCAP.PP.KD)
    # GDP per capita, PPP (constant 2011 international $) (NY.GDP.PCAP.PP.KD)
    # Life expectancy at birth, total (years) (SP.DYN.LE00.IN)
    # UIS: Mean years of schooling of the population age 25+. Male (UIS.EA.MEAN.1T6.AG25T99.M) - NOT AVAILABLE
    # Government expenditure on education, total (% of GDP) (SE.XPD.TOTL.GD.ZS)
    # Computer, communications and other services (% of commercial service exports) (TX.VAL.OTHR.ZS.WT)
    # Access to electricity (% of population) (EG.ELC.ACCS.ZS)
    # Adjusted net national income per capita (constant 2010 US$) (NY.ADJ.NNTY.PC.KD)
    # Armed forces personnel, total (MS.MIL.TOTL.P1)
    # Commercial bank branches (per 100,000 adults) (FB.CBK.BRCH.P5)
    # Completeness of birth registration (%) (SP.REG.BRTH.ZS)
    # Compulsory education, duration (years) (SE.COM.DURS)

    ids = ["NY.GDP.PCAP.PP.KD","SP.DYN.LE00.IN","NY.GNP.PCAP.PP.KD"]

    year = getRecentOfAll(ids)

    url = "http://" + request.get_host() + "/api/" + ids[0] + "/" + str(year)
    data = requests.get(url=url).json()

    dump = json.dumps({"result": data})

    return HttpResponse(dump, content_type='application/json')
