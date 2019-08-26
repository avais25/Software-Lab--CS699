import re
import string
file=open("input.txt","r")
fout=open("output.txt","w")
for  word in file:
    if(re.findall(r'\+91\d{10}\b',word)):
      word=re.sub(r'\+91\d{4}','******',word)    #masking phone no
    if(re.findall(r'[0-9a-zA-Z_\-\.]+@[a-zA-Z]+\.[a-zA-Z0-9_\-\.]+',word)):
      word=re.sub(r'[0-9a-zA-Z_\-\.]+@','******@',word) #masking email
    if(re.findall(r'\. .',word)):
      s=re.findall(r'\. .',word)
      word=re.sub(r'\. (.)', lambda m: ". "+m.group(1).upper(), word)    #capital after fullstop
    if(re.findall(r'\bwww\.[a-zA-Z0-9._-]+\.[a-zA-Z0-9._-]+\b',word)):
      word=re.sub(r'\bwww.','http://www.',word)     #addinng http in links
    word=re.sub(r'color','colour',word)		#replacing color with colour
    word=re.sub(r'Color','Colour',word)	
    fout.write(word)

    
