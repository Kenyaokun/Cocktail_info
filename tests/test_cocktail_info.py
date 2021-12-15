from cocktail_info import cocktail_info

import requests
import json
import pandas as pd
import numpy as np
import re
from IPython.display import Image, HTML
import warnings
warnings.filterwarnings('ignore')


def test_get_id():
    text = 'gin'
    actual = cocktail_info.get_id(text)
    
    assert type(actual) == pd.DataFrame, 'The test does not pass.'

def test_get_cocktail():
    name = 'gin'
    actual = cocktail_info.get_cocktail(name)
    expected = type(HTML())
    
    assert type(actual) == expected, 'The test does not pass.'
    
def test_get_pics():
    pic_no = 'gin'
    actual = cocktail_info.get_pics(pic_no)
    expected = type(HTML())
    
    assert type(actual) == expected, 'The test does not pass.'
    
def test_get_ingredient():
    text = 'gin'
    actual = cocktail_info.get_ingredient(text)
    
    assert type(actual) == pd.DataFrame, 'The test does not pass.'
    
def test_get_description():
    history = 'gin'
    expected = 'The name of the wine you type in is or similar to: Gin. Gin is a distilled alcoholic drink that derives its predominant flavour from juniper berries (Juniperus communis). Gin is one of the broadest categories of spirits, all of various origins, styles, and flavour profiles, that revolve around juniper as a common ingredient. From its earliest origins in the Middle Ages, the drink has evolved from a herbal medicine to an object of commerce in the spirits industry. Gin emerged in England after the introduction of the jenever, a Dutch liquor which originally had been a medicine. Although this development had been taking place since early 17th century, gin became widespread after the William of Orange-led 1688 Glorious Revolution and subsequent import restrictions on French brandy. Gin today is produced in subtly different ways, from a wide range of herbal ingredients, giving rise to a number of distinct styles and brands. After juniper, gin tends to be flavoured with botanical/herbal, spice, floral or fruit-flavours or often a combination. It is most commonly consumed mixed with tonic water. Gin is also often used as a base spirit to produce flavoured gin-based liqueurs such as, for example, Sloe gin, traditionally by the addition of fruit, flavourings and sugar.'
    actual = cocktail_info.description(history)
    
    assert actual == expected, 'The test does not pass.'

def test_get_is_in():
    ingredient = 'gin'
    expected = 'The ingredient is in the list.'
    actual = cocktail_info.is_in(ingredient)
    
    assert expected == actual, 'The test does not pass.'


