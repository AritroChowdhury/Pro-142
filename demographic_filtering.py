import numpy as pd 
import pandas,csv

with open('movies.csv',encoding="utf-8") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]
    headers = data[0]
