# -*- coding: UTF-8 -*-
# normalize.py
# normalizes and denormalizes Arabic text
# takes in a File, returns a File.
# libraries: RE (Regular Expression),

import re
from os.path import join 

# toRawText:
# converts classical Arabic to raw text
def toRawText(text):
    englishChars = re.compile(u"[0-9*#|؟.$,;:/<>a-zA-Z()%،؛~»«]|\]|\[|_|-|=|\}|\{")
    extraSpaces = re.compile('( ){2,}')
    text = re.sub(englishChars, " ", text)
    text = re.sub(extraSpaces, ' ', text)
    text = _deNoise(text)
    return text

# normalizeAndConcatenate:
# converts classical Arabic to raw text and concatenates into one string.
def normalizeAndConcatenate(text):
    text = toRawText(text)
    text = "|".join(text )

# cleanText:
# delete multiple spaces and multiple new lines.
def _cleanText(textBlocks):
    textBlocks = re.sub('(?<=\n)( ){2,}', ' ', textBlocks)
    textBlocks = re.sub('(\n){2,}', '\n\n', textBlocks)
    textBlocks = re.sub("\n ", "\n ", textBlocks)
    return textBlocks

# normalizeArabic:
# standardizes Classical Arabic removing variation among leters
# must be undone using denormalize before search
def _normalizeArabic(text):
    text = re.sub("[إأٱآا]", "ا", text)
    text = re.sub("ى", "ي", text)
    text = re.sub("(ؤ)", "و", text)
    text = re.sub("(ئ)", "ي", text)
    text = re.sub("(ة)", "ه", text)
    return text

# deNoise(text) deletes noise characters from Arabic text
def _deNoise(text):
    noise = re.compile(""" ّ | # Tashdid
                            َ | # Fatha
                            ً | # Tanwin Fath
                            ُ | # Damma
                            ٌ | # Tanwin Damm
                            ِ | # Kasra
                            ٍ | # Tanwin Kasr
                            ْ | # Sukun
                            ـ # Tatwil/Kashida
                            """, re.VERBOSE)
    text = noise.sub('', text)
    #text = re.sub(noise, '', text)
    return text

# deNormalizeArabic:
# deNormalizes normalized text by adding:
# array of variations to each potentially normalized character
# use during which phase??
def deNormalize(text):
    text = re.sub('[إأٱآا]', '[إأٱآا]', text)
    text = re.sub('(ي|ى)\\b', '[يى]', text) # HEAVY '[إأٱآايى]'
    #text = re.sub('ة', '[هة]', text)
    text = re.sub('(ؤ|ئ|ء)', '[ؤئءوي]', text)
    return text


