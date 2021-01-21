#!/usr/bin/env python
"""
:file: name_extractor.py
:author: Brant Yukan
:date: 11/29/20
:brief: This program extracts the patient's name from a document.
:version: 0.0.1
:notes:
download('en')
download('en_core_web_md')
/root/anaconda3/envs/nlp/bin/python
source activate nlp
python name_extractor.py "Please find attached a report for Jose Hurtado. Andrew Hesseltine MD © 07-11-2019 12:35 PM Fax Services ~» 19098248234 pg 2 of 3"
"""
import os
import sys
from collections import Counter
import spacy
import logging

logging.basicConfig(level=logging.ERROR,
                    format=' %(asctime)s - %(levelname)s - %(message)s')
en_model = spacy.load('en_core_web_md')

def extract_name(s, en_model=en_model):
    """
    This function parses for PERSON entities using spacy's NER tagger.
    a patient could have MD following their name, so I have to rewrite that logic
    currently it's removing any name containing MD from consideration
    :param s: input document as string
    :param en_model: en_model = spacy.load('en_core_web_md')
    :return: Counter.most_common() list
    """
    return Counter([*filter(lambda x: x[-2:] != 'MD', map(lambda x: str(x)[:-3].strip() if str(x)[-3:] == 'DOB' else str(x).strip(), [ent for ent in en_model(s).ents if ent.label_ == 'PERSON']))]).most_common()


def main(log):
    return extract_name(sys.argv[1])


if __name__ == '__main__':
    log_output_path = "logs/name_extractor.log"
    if not os.path.exists('logs'):
        os.makedirs('logs')
    if not os.path.exists(log_output_path):
        open(log_output_path, 'w+')  # create the file

    print(main(log_output_path))
