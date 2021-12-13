import datetime
import os
import sys

## https://stackoverflow.com/a/16985066
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from core.WikipediaPage import GetRandomPage 

## Example call: python3 scripts/random_ngrams_to_file.py
## The above will create a file with the current datetime and one
## ngram per row in the data/ngrams directory

## Get the random titles 
page = GetRandomPage() 
ngrams = page.BodyAsNGrames(1)

## Write the titles to a file 
file_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
os.makedirs("data/ngrams", exist_ok=True)
with open("data/ngrams/" + file_datetime + ".txt", "w+") as file:
    for key in ngrams.keys():
        file.write(" ".join(key) + "\t" + str(ngrams[key]) + "\n")
