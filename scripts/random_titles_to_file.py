import datetime
import os
import sys

## https://stackoverflow.com/a/16985066
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from core.WikipediaPage import GetRandomTitles 

## Example call: python3 scripts/random_titles_to_file.py 3
## The above will create a file with the current datetime and three 
## titles (one per row) in the data/titles directory

## Parse input. Only argument is the number of titles to get
try: 
    n = int(sys.argv[1])
except: 
    raise ValueError("Must provide the number of titles to retrieve.")

## Get the random titles 
start = datetime.datetime.now() 
titles = GetRandomTitles(n)
print("Runtime: " + str(datetime.datetime.now() - start)) 

## Write the titles to a file 
file_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
os.makedirs("data/titles", exist_ok=True)
with open("data/titles/" + file_datetime + ".txt", "w+") as file:
    file.write("\n".join(titles))
