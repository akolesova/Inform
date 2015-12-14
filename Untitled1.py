# -*- coding: utf-8 -*-
#!/usr/bin/python

import codecs
import nltk

dic={}
dic1={}
file= codecs.open('train.txt', "r", "utf_8_sig")
for str in file.readlines:
    str=str.lower()
    x= nltk.word_tokenize(str)
   dict[x[0]]=[]
   dict1[x[0]]=0

file.close
    
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
    dic[y] = list(set(dic[key]))

f.close
a=0

f1=codecs.open('test.txt', "r", "utf_8_sig")
my_file = open("result1.txt", "w")

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
   for key in dic1:
      dic1[key]=0    
    a=0
    my_file.write(b + '\n')
            


my_file.close()
f1.close
print("end")
                
            
        

