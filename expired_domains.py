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

#{"Text":"At Seven Avenue Design we design projects in wide range of scales from one space to whole neighborhoods.\nAt Seven Avenue Design we transform the interior of your space to make it functional, personal, according to your space and budget.\nOur architectural services include your conceptual and schematic design listening to your objectives, space requirements and even what you are planning ahead.\nWe accompany you to make your design a palpable building.","timestamp":"2019-04-25T19:52:44Z","url":"http://sevenavedesign.com/studio/"}

import glob
import os

def hash_output(f):
    s = f.split("/")[-1]
    s = 'out/domains/'+ s +'_expired.json'
    return s

DATA_FILES = ["/Volumes/bee/AI/data/en/c4-train.00000-of-01024.json"]

def domain_value(url):
    time.sleep(2)
    index = "CC-MAIN-2024-51-index"
    print("[*] Trying index %s" % index)
    cc_url  = "http://index.commoncrawl.org/%s?" % index
    cc_url += "url=%s&matchType=domain&output=json" % url
    response = requests.get(cc_url)

    score = 0
    if response.status_code == 200:
        records = response.content.splitlines()
        print(records)
        score = len(records)
        domain_hits.append({url: len(records)})
        for record in records:
            record_list.append(json.loads(record))
            print("[*] Added %d results." % len(records))
    return score

def find_expired_domains(source):
    with open(source) as fp:
        for line in fp:
            data = json.loads(line)
            domain = urlparse(data["url"]).netloc
            result = subprocess.run(["nslookup", domain], capture_output=True)
            out = result.stdout.decode("utf-8")

            if(re.search('NXDOMAIN', out)):
                #score = domain_value(domain)
                score=0
                logline = '{"expired": "'+ domain+'", "url": "'+ data['url']  +'", "score": '+str(score)+'}'
            
                with open(hash_output(source), 'a') as f:
                    f.write(logline + '\n')
                    print(logline)       
            time.sleep(0.1)

DATA_FILES = glob.glob(r'/Volumes/bee/AI/data/en/*.json') 
DATA_FILES = filter((lambda f: not(exists(hash_output(f)))), DATA_FILES)
            
with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
    l = list(executor.map(lambda f: find_expired_domains(f), DATA_FILES))
