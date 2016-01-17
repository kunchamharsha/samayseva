#!C:/Python27/python.exe
import urllib
from bs4 import BeautifulSoup
import urlparse
import thread
import threading
from threading import Thread
import cgi
import cgitb
cgitb.enable()


print "Content-type:text/html"
print "\n\n"
print"<head>"
print"<style>"
print"div{display:inline;position:relative;float:left;}"
print"""
#flipkart
{
display: inline-block;
margin: 12px 0px 0px 12px;
padding: 0px;
box-shadow: 8px 8px 5px #888888;
background:none repeat scroll 0% 0% rgb(241, 241, 241);
border: 1px solid rgb(229, 229, 229);
width:300px;
height:100px;
position:relative;
}"""
print"</style>"
print"</head>"
threads=[]
fopen=open('a1.txt','r')
parent=fopen.readlines()

def decode(i,string):
        a1=parent[i].encode('utf-8')
        string=string.replace(" ","+")
        a1=a1.replace("asus",string)
        return a1
        
def dataextract(a1):
         a2=urllib.urlopen(a1)
         a3=a2.read()
         soup=BeautifulSoup(a3)
         return soup
def scrapef(soup,a,b,c,d): #flipkart
        price=[]
        product=[]
        pics=[]
        for i in soup.find_all(a, {"class":b}):
                if(i.get_text(' ', strip=True)!=('Click here to send yourself a notification.') and i.get_text(' ', strip=True)!="Get the app now" and i.get_text(' ', strip=True)!="login" and i.get_text(' ', strip=True)!=("See Similar Products") and i.get_text(' ', strip=True)!=''):
                        product.append(i.get_text(' ', strip=True))
        dd=soup.find(c, {"class":d})
        if(dd!=None):
                for j in soup.find_all(c, {"class":d}):
                                price.append(j.get_text(' ', strip=True))
        else:
                for j in soup.find_all(c, {"class":"fk-font-12"}):
                                price.append(j.get_text('', strip=True))
        for m in soup.find_all("img",{"onerror":"img_onerror(this);"}):
            pics.append(m.get('data-src'))        
        print"<table id='flipkart'>"
        for t in range(0,len(price)):
                print"<tr><td>flipkart</td></tr>"
                print "<tr><td><img src='"+pics[t]+"'></td></tr>"
                print "<tr><td>"+product[t]+"</td></tr>"
                print "<tr><td>"+price[t]+"</td></tr>"
        print"</table>"


def flipkart(soup):
        scrapef(soup,"a","fk-display-block","span","fk-font-17 fk-bold")        
def fk(string):
        a1=decode(0,string)
        soup=dataextract(a1)
        flipkart(soup)
def  th(string):
        t2 = Thread(target=fk,args=(string,))
        t2.start()
        t2.join
        
        
if __name__ == "__main__":
    form = cgi.FieldStorage() 
    subject = form.getvalue('item')
    th(subject)




         

            
         
           
    
