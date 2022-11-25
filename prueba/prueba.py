
from django.shortcuts import render
from prueba.models import Product
from django.http.response import HttpResponse
from bs4 import BeautifulSoup
import requests 
import json
import pandas as pd
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

    for i in aux1: 
        name = (i['information']['puretitle'])
        image = (i['image']['mainImage'])
        #sku = models.IntegerField(default=1)
        #valoration = models.IntegerField(default=5)
        price = float(i['promotionInfoVO']['localOriginalPriceFromStr'])
        product=Product(name=name,imagen=image,price=price)
        print (product)
        print (type(name))
        print (type(i['id']))
        print (type(i['reviews'].get('productScore',0)))
        print (type(price))
        print (type(image))
"""
        data.append(list_aux)

    df = pd.DataFrame(data, columns=['Title','ID','Score','Price','Image'])
    sorted_df = df.sort_values(by=['Price'], ascending=[True])
    ##seria mejor convertirlo a un json
    data_json=sorted_df.to_json()
    sorted=sorted_df.transpose()
    return(sorted_df)"""
scraping("bicicleta")



