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
#sd
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

def scrapes(soup,a,b,c,d): #snapdeal
        price=[]
        product=[]
        pics=[]
        for i in soup.find_all(a, {"class":b}):
                if(i!=None):
                        product.append(i.get_text(' ', strip=True))
        for j in soup.find_all(c, {"class":d}):
                if(j!=None):
                        price.append(j.get_text(' ', strip=True))
        for m in soup.find_all("img",{"class":"product-image"}):
                if(m!=None):
                        pics.append(m.get('src'))
        print"<div>"
        print"<table id='sd' style='width=30%;'>"
        for t in range(0,len(pics)):        
                if(pics[t]!=None):
                    print"<tr><td>snapdeal</td></tr>"
                    print "<tr><td>"+"<img src='"+pics[t]+"'>"+"</td></tr>"
                    print "<tr><td>"+product[t]+"</td></tr>"      
                    print "<tr><td>"+price[t]+"</td></tr>"           
        print"</table>"
        print"</div>"


def snapdeal(soup):
        scrapes(soup,"p","product-title","span","product-price")


def sd(string):
        a1=decode(1,string)
        soup=dataextract(a1)
        snapdeal(soup)

def  th(string):
        t2 = Thread(target=sd,args=(string,))
        t2.start()
        t2.join
     
        
        
if __name__ == "__main__":
    form = cgi.FieldStorage() 
    subject = form.getvalue('item')
    print subject
    th(subject)




         

            
         
           
    
