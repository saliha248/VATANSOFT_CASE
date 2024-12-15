# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 15:26:47 2024

@author: saliha
"""

import requests

api = "https://publicapis.io/random-dog-animals-api"

boyutSiniri = 1050000

istekSayisi = 100

buyukOlan = 0
kucukOlan = 0 

for _ in range (istekSayisi):
    istek = requests.get(api)
    istekBoyutu = len(istek.content);
    print(f"istek boyutu: {istekBoyutu}")
    
    if istekBoyutu > boyutSiniri:
        buyukOlan +=1
        print(f"büyüktür:{buyukOlan}")
    else:
        kucukOlan +=1
        print(f"küçüktür:{kucukOlan}")
        
