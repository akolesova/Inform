# -*- coding: utf-8 -*-
#!/usr/bin/python

import codecs


import nltk
SV=[]
ES=[]
EN=[]
HU=[]
DA=[]
IT=[]
NL=[]
PL=[]
LV=[]
EE=[]
FR=[]
CS=[]
FI=[]
DE=[]
LT=[]
dic ={'sv':SV, 'es':ES, 'en':EN,'hu':HU, 'da':DA, 'it': IT, 'nl':NL, 'pl':PL, 'lv':LV, 'ee':EE, 'fr':FR, 'cs':CS, 'fi':FI, 'de':DE, 'lt':LT}

f = codecs.open('train.txt', "r", "utf_8_sig")
for line in f.readlines():
    line=line.lower()
    x=nltk.word_tokenize(line)   
    for i in x:
        if i == ','  or i=='.' or i=='/' :
           x.remove(i)
    for i in x:
        if i == '-'  or i==':' :
            x.remove(i)   
    y=x[0]
    x.remove(y)
    dic[y]=dic[y]+x
    dic[y] = list(set(dic[y]))

f.close
a=0

dic1 ={'sv':0, 'es':0, 'en':0,'hu':0, 'da':0, 'it': 0, 'nl':0, 'pl':0, 'lv':0, 'ee':0, 'fr':0, 'cs':0, 'fi':0, 'de':0, 'lt':0}
f1=codecs.open('test.txt', "r", "utf_8_sig")
my_file = open("result.txt", "w")

for line1 in f1.readlines():
    line1=line1.lower()
    x1=nltk.word_tokenize(line1)
    for i in x1:
        if i == ','  or i=='.' or i=='/' :
           x1.remove(i)
    for i in x1:
        if i == '-'  or i==':' :
           x1.remove(i)
    for i in x1:
        for key in dic:
            if i in dic[key]:
                dic1[key]+=1
    for key in dic1:
        if dic1[key]>=a:
            a=dic1[key]
            b=key
            b=b.upper()
    dic1 ={'sv':0, 'es':0, 'en':0,'hu':0, 'da':0, 'it': 0, 'nl':0, 'pl':0, 'lv':0, 'ee':0, 'fr':0, 'cs':0, 'fi':0, 'de':0, 'lt':0}
    a=0
    my_file.write(b + '\n')
            


my_file.close()
f1.close
print("end")
                
            
        

