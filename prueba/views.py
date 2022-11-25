from django.shortcuts import render
from prueba.models import Product, Search
from django.http.response import HttpResponse,JsonResponse
from bs4 import BeautifulSoup
import requests 
import json
import pandas as pd
# Create your views here.
def search_to_url(search):
    url = f'https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&tab=all&SearchText={search}'
    return url
def scraping(search_input):
    url1 = search_to_url(search_input)
    result = requests.get(url1)
    soup = BeautifulSoup(result.content, 'html.parser')
    json_result = soup.findAll('script')[36].text.strip()[30:-64]
    format_json = json.loads(json_result)
    aux1 = format_json['props']['offerResultData']['offerList']
    data = []
    list_aux = []
    search_results =[]

    ##

    for i in aux1:


        search_results.append({

            'Title':i['information']['puretitle'],

            'ID':i['id'],

            'Score':float(i['reviews'].get('productScore',0)),

            'Price':i['promotionInfoVO']['localOriginalPriceFromStr'],

            'Image':i['image']['mainImage']

        })

    ##

    print(search_results)

    data_json =json.dumps(search_results) #json

    print(data_json)
    return(search_results)
def home(request):
    product = Product.objects.all()
    if request.method == 'POST':
        search_input = request.POST["input-product"]
        if not search_input == "":
            data_frame=scraping(search_input)
            obj = Search(search=search_input)
            obj.save()
            return render(request , "home.html", {"product":data_frame})
    return render(request , "home.html")