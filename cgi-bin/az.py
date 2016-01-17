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
print"""
#posts
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
print"div{display:inline;position:relative;float:left;}"
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

def scrapea(soup,a,b,c,d): #amazon
        price=[]
        product=[]
        pics=[]
        for i in soup.find_all(a, {"class":b}):
                product.append(i.get_text(' ', strip=True))
        for j in soup.find_all(c, {"class":d}):
            price.append(j.get_text(' ', strip=True))
        for m in soup.find_all("img",{"class":"s-access-image cfMarker"}):
            pics.append(m.get('src'))
        print"<div style='width=25%;'>"
        print"<table id='amazon'>"
        for t in range(0,len(product)):
            print"<tr><td>amazon</td></tr>"
            print "<tr><td>"+"<img src='"+pics[t]+"'>"+"</td></tr>"
            print "<tr><td>"+product[t]+"</td></tr>"      
            print "<tr><td>"+price[t]+"</td></tr>"           
        print"</table>"
        print"</div>"

def amazon(soup):
        scrapea(soup,"h2","a-size-medium a-color-null s-inline s-access-title a-text-normal","span","a-size-base a-color-price s-price a-text-bold")         

def az(string):
        a1=decode(2,string)
        soup=dataextract(a1)
        amazon(soup)
def  th(string):
        t2 = Thread(target=az,args=(string,))
        t2.start()
        t2.join
        
        
if __name__ == "__main__":
    form = cgi.FieldStorage() 
    subject = form.getvalue('item')
    th(subject)




         

            
         
           
    
