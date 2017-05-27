# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 15:32:02 2017

@author: Harsh Kevadia
"""

from bs4 import BeautifulSoup
import re
import time
import requests


def run(url):

    pageNum=1 # number of pages to collect

    fw=open('questions.txt','w') # output file
	
    for p in range(1,pageNum+1): # for each page 

        print ('page',p)
        html=None

        if p==1: pageLink=url # url for page 1
        else: pageLink=url+'?n='+str(p) # make the page url
		
        for i in range(5): # try 5 times
            try:
                #use the browser to access the url
                response=requests.get(pageLink,headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })
                html=response.content # get the html
                break # we got the file, break the loop
            except Exception as e:# browser.open() threw an exception, the attempt to get the response failed
                print ('failed attempt',i)
                #time.sleep(2) # wait 2 secs
				
		
        if not html:continue # couldnt get the page, ignore
        
        soup = BeautifulSoup(html.decode('ascii', 'ignore'),'lxml') # parse the html 

        questions=soup.findAll('li', {'class':re.compile('question')}) # get all the review divs

        for question in questions:
            tag = {}
            vote,text='NA','NA' # initialize critic and text 
            text = question.find('p').text.replace("\r", " ").replace("\n", " ")
            tagsHTML = question.findAll('span', {'class':re.compile("tags")}).findAll('a')
            for tagHTML in tagsHTML:
                tag.append(tagHTML.text)
            print(tag + "\t\t\t\t\t" + text +'\n\n')
            #time.sleep(2)	# wait 2 secs 
            fw.write(tag + "\t\t\t\t\t" + text +'\n\n')
    fw.close()

if __name__=='__main__':
    url='https://www.careercup.com/page'
    run(url)
