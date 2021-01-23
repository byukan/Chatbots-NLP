"""
This file contains definitions for functions that do OCR on pdf files, saves individual pages as images, and extracts names using NER.
:author:  Brant Yukan, brant.yukan@gmail.com
:date: 12/31/20
"""

# !brew install tesseract
# !pip install pytesseract
# !pip install mysql-connector-python
import mysql.connector
from mysql.connector.constants import ClientFlag
import pandas as pd
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import yaml

# !brew install poppler
from pdf2image import convert_from_path
import os
from tqdm.notebook import tqdm
# tqdm.pandas()
import sys
from collections import Counter
import spacy
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from dateutil.parser import parse


def ocr_save(p):
    """
    This function OCRs and saves individual txt files.
    """
    s = pytesseract.image_to_string(Image.open(p))
    txt_p = p.replace('png', 'txt').replace('images', 'text')
    dirname_txt_p = os.path.dirname(txt_p)
    if not os.path.exists(dirname_txt_p):
        os.makedirs(dirname_txt_p)
    with open(txt_p,"wt") as f:
        f.write(s)
    return s


def pdf_ocr(pdf_path, reprocess=False):
    """
    This function converts a pdf to individual png images and saves to disk.  It then runs OCR on those pngs and saves the individual txt files.
    :param: pdf_path is the path to the pdf file, for example, '/Users/byukan/upds/1607002492/16070024929618'
    :return: num_pages, OCRed text of the entire pdf contents combined
    """
    filename = os.path.basename(pdf_path)
    images_path = f'data/pngs/images_{filename}'
    exists = os.path.exists(images_path)
    if not exists or reprocess==True:
        try:
            # print('Converting pdf file to png images.')
            # PDFPageCountError if password encrypted
            pages = convert_from_path(pdf_path, dpi=120)
            num_pages = len(pages)
        except Exception as e:
            num_pages = -1
            return -1, f"This PDF,{filename}, is password encrypted, or has some other error: {e}"
        
        if not exists:
            os.makedirs(images_path)
        # save all the individual pngs
        print(f'Saving {num_pages} png images for file: {filename}.', end='')
        [page.save(f'{images_path}/{filename}_{i}.png', 'png')
         for i, page in tqdm(enumerate(pages))]
        # ocr all of them
        pngs = [f'{images_path}/{filename}_{i}.png' for i in range(len(pages))]
        print(
            f'Running OCR on images and saving {num_pages} .txt files for file: {filename}.', end='')
        return num_pages, '\n'.join([*map(ocr_save, tqdm(pngs))])


en_model = spacy.load('en_core_web_md')

def extract_name(s, en_model=en_model):
    """
    This function parses for PERSON entities using spacy's NER tagger.
    a patient could have MD following their name, so I have to rewrite that logic
    currently it's removing any name containing MD from consideration
    :param s: input document as string
    :param en_model: en_model = spacy.load('en_core_web_md')
    :return: Counter.most_common() list
    :notes: Needs more logic to identify patient, rather than doctor.
    """
    return Counter([*filter(lambda x: x[-2:] != 'MD', map(lambda x: str(x)[:-3].strip() if str(x)[-3:] == 'DOB' else str(x).strip(), [ent for ent in en_model(s).ents if ent.label_ == 'PERSON']))]).most_common()

