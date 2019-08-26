import sys;
import getpass;
import re;
#import time
import requests;
import bs4;

def start_moodle_session():
  login_url="http://moodle.iitb.ac.in/login/index.php"
  #user=input('username:')
  #passwd=getpass.getpass()
  user=sys.argv[2]
  passwd=sys.argv[3]
  session=requests.session()
  result=session.post(login_url, data={'username':user,'password':passwd})
  if result.status_code != 200:
    print ("Error status", result.status_code, "when logging", login_url)

  return session


def get_page(url, session):
  result = session.get(url)
  if result.status_code != 200:
    print ("Error status", result.status_code, "when fetching", url)

  content=bs4.BeautifulSoup(result.text,'html.parser')

  return content

def threadsn(url,session):
  content = get_page(url, session)
  #p=re.findall(r'+1',str(content))
  pat = content.findAll("div", {"class":"posting fullpost"})
  ipatt=sys.argv[1]
  temp= re.findall(r'> *'+re.escape(ipatt)+' *(?:<br|<div|</p)',str(pat))
  print ("Number of occurance of pattern(in the line by itself in this thread)are:- ",len(temp))
  #for p in pat:
   #tt=bs4.BeautifulSoup(str(p),'html.parser')
   #pattern=tt.find('p')
   #n=tt.find_all(r'\+1')
   #print(p)



#login and get my moodle landing page
start_url ="http://moodle.iitb.ac.in/my"

def main(argv):
    session = start_moodle_session()
    #print(sys.argv[1])
    
    # find the url for course on landing page
    content = get_page(start_url, session)
    tag = content.find("a", text=re.compile('699'))
    #print (text)
    print (tag.text)
    course_url = tag['href']
    print ("Course Link:-"+str(course_url))

    # find the url for discussion on course page
    content = get_page(course_url, session)
    tag = content.find("a", href=re.compile('forum'))
    print (tag.text)
    discuss_url = tag['href']
    print ("News Forum Link:-"+str(discuss_url))
    


    # find the urls for discussion threads on discussion forum page
    content=get_page(discuss_url,session)
    #print (content.text	)

    #time.sleep(2)
    #text_file = open("Output.txt", "w")
    #text_file.write(str(content.txt))
    #text_file.close()
    #tag = content.find("a", text="Unix")
    tag = content.find("table", {"class":"forumheaderlist"})
    lists =tag.findAll("td",{"class":"topic starter"})
    
    i=0
    for a in lists:
      ll=bs4.BeautifulSoup(str(a),'html.parser')
      links=ll.find("a")
      i=i+1
      print("\nIterating on discussion thread number :-",i)
      print(links['href'])
      # iterate through threads and find the counts for patterns
      threadsn(links['href'],session)
      
      #links=lists.find("a")
      #tag3 =tag2.findAll("a",)
      #tag = content.find("a", {"href":"http://moodle.iitb.ac.in/mod/forum/discuss.php?d=61140"})
      #print (links)
    
    
    

    return


if __name__ == "__main__":
     main(sys.argv)
