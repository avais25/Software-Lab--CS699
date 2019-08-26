import sys
import requests
import re
import bs4
import json
import urllib
import webbrowser

def main(argv):
    village=str(sys.argv[1])	#passing command line argument
    lsto= []
    lsti= []
    i=0
    with urllib.request.urlopen("https://gsda.maharashtra.gov.in/maps/data.js?_=1503477953046") as url:
      s = url.read()	#getting list of regions
    data = json.loads(s.decode('utf-8'))
    #print (data)
    for reg in data:
      #print(reg)
      with urllib.request.urlopen("https://gsda.maharashtra.gov.in/maps/%s/data.js?_=1503477953046" % reg) as url:
        s = url.read()		#getting dictionary
        
      region = json.loads(s.decode('utf-8'))
      #print (region['Pune']['Mawal']['Sadavali']) 
      for dis,tal in region.items():		#extracting village , district , taluka , region from dictionary
        for tal,vill in tal.items():
          for vill,k in vill.items():
            if(str(vill)==village):
              #print(reg,dis,tal,vill)
              i=0
              lsti.append(reg)
              lsti.append(dis)
              lsti.append(tal)
              lsti.append(vill)
              i=i+1
              lsto.append(lsti)
              lsti=[]
              #print(lsto)
              #print(lsti)
    if(len(lsto)==0):		#checking if village exixt
      print("No village found")
      sys.exit()
    print("Select index of  the villege you want:-")	#selecting village
    for x in range (0,len(lsto)):
      print(x,".  %s-->%s-->%s-->%s" %(lsto[x][0] ,lsto[x][1], lsto[x][2], lsto[x][3]))
    xf=int(input())
    url="https://gsda.maharashtra.gov.in/maps/%s/%s/%s/%s.pdf" %(lsto[xf][0] ,lsto[xf][1], lsto[xf][2], lsto[xf][3])
    print(url)
    response=requests.get(url, )
    with open('map.pdf','wb') as fp:	#weiting pdf file
      fp.write(response.content)

    webbrowser.open_new("map.pdf")	#open pdf  in default browser

    return

if __name__ == "__main__":
    main(sys.argv)
