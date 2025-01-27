import requests
import pandas as pd
import json
import sys
import time
import subprocess
from urllib.parse import urlparse
import re

import concurrent.futures
import urllib.request
from os.path import exists

import glob
import os

def hash_output(f):
    s = f.split("/")[-1]
    s = 'out/terms/'+ s +'_term.json'
    return s

def find_term(source, term):
    with open(source) as fp:
        for line in fp:
            data = json.loads(line)
            domain = urlparse(data["url"]).netloc
            hit = re.search(term, line)
            print('.', end='', flush=True)
           
            if(hit):
                logline = '{"domain": "'+ domain+'", "url": "'+ data['url']  +'", "txt": "' + repr(data['text']) + '"}'
                logline = line
            
                with open(hash_output(source), 'a') as f:
                    f.write(logline)
                    print('*', end='', flush=True) 

DATA_FILES = ["/Volumes/bee/AI/data/en/c4-train.00000-of-01024.json"]
DATA_FILES = glob.glob(r'/Volumes/bee/AI/data/en/*.json') 
DATA_FILES = filter((lambda f: not(exists(hash_output(f)))), DATA_FILES)

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    l = list(executor.map(lambda f: find_term(f, "wheelchair|disabled|disability"), DATA_FILES))
