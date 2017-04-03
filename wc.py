from wordcloud import WordCloud, STOPWORDS
from os import path
from PIL import Image
import pandas as pd
import numpy as np
import re

import matplotlib.pyplot as plt

songs = pd.read_json("rogerwaterlyrics.json", encoding='utf-8')

rw = songs['lyrics']

cs = ""
for i in rw:
    cs = cs + " " + i


wc = WordCloud(background_color="black", max_words=5000, stopwords=STOPWORDS)
wc.generate(cs)
wc.to_file("rogerwater.png")
