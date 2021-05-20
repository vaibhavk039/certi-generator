import cv2
import csv
import shutil
import os
from PIL import Image, ImageDraw, ImageFont
from colorama import Fore, Back, Style

import pandas as pd
from zipfile import ZipFile

PATH = "certificate.png"
NAME_LIST_PATH = "list.csv"




def fillName(path, name_list_path):
  
    data = pd.read_csv(name_list_path)

#Import 'Name' List from the imported .xlsx file
    name_list = data['name'].to_list()

#Determining the length of the list
    max_no = len(name_list)

#The Loops for creating certificates in bulk
# for i in name_list:
    for idx, i in enumerate(name_list):

        im = Image.open(path)
        d = ImageDraw.Draw(im)
        location = (700, 680)
    
        font = ImageFont.truetype("arial.ttf", 130, encoding="unic")
        d.text(location, i.title(), fill="#0E4573",font=font)
     
        im.save('out/{}.png'.format(i))

def certificateGen(path,name_list_path):
    os.mkdir('out')
    fillName(path,name_list_path)
    shutil.make_archive('output', 'zip', 'out')
    shutil.rmtree('out', ignore_errors=True)

if __name__ == "__main__":
    certificateGen(PATH, NAME_LIST_PATH)
