# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 23:59:07 2018

@author: Rama krishna
"""

import re
import pandas as pd

def read_csv():
    input_df = pd.read_csv('')
    return input_df


    
def generate_rows():
    input_df = read_csv()
    

def get_field_len(data):
    try:
        return len(data)
    except:
        return 0

def hyphen_count(data):
    try:
        return data.count('-')
    except:
        return 0


def is_alpha_num(data):
    try:
        if(data.isalnum()):
            return 1
        else:
            return 0
    except:
        return 0
    

def is_hexa_decimal(data):    
    if(all(c in string.hexdigits for c in data)):
        return 1
    return 0

def has_hyphen(data):
    if('-' in data):
        return 1
    return 0
    
    
def has_brackets(data):
    c = re.compile('^[{}]')
    try:
        if(bool(c.match(data))):
            return 1
        else:
            return 0
    except:
        return 0
    
def tokenize(data):
    splits = data.split('-')
    return splits

def is_guid_pattern(data):
    
    c = re.compile('[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}', re.T)
    res = c.match(data)
    if res:
        return 1
return 0
    
def change_to_lower(data):
    return data.lower()

    
def token_by_fixed_len(data):
    
    
    
    
    
        
    
    
