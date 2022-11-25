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
    search_results =[]

    ##

    for i in aux1:


        search_results.append({

            'Title':i['information']['puretitle'],

            'ID':i['id'],

            'Score':float(i['reviews'].get('productScore',0)),

            'Price':i['promotionInfoVO']['localOriginalPriceFromStr'][1:],

            'Image':i['image']['mainImage']

        })

    ##

    # print(search_results)

    data_json =json.dumps(search_results) #json

    # print(data_json)
    return(search_results)

def tracked_product(tracked_product):
        product_elements = tracked_product[0].split('*')
        product_elements_dict= {
            "ID": product_elements[0],
            "Title": product_elements[1],
            "Score": product_elements[2],
            "Price": product_elements[3],
            "Image": product_elements[4]
        }
        return product_elements_dict

def home(request):
    # product = Product.objects.all()
    if request.method == 'POST':
        # data_frame =[]
        if "search_btn" in request.POST:
            search_input = request.POST["input-product"]
            if not search_input == "":
                data_frame=scraping(search_input)
                obj = Search(search=search_input)
                obj.save()
                return render(request , "home.html", {"product":data_frame})
        elif "track_btn" in request.POST:
            product_track = request.POST.getlist("product_tracked")
            product_tracked = tracked_product(product_track)
            print(product_tracked)
            return render(request , "home.html", {"product_tracked":product_tracked})
    return render(request , "home.html")