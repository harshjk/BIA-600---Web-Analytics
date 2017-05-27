# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 16:26:44 2017

@author: Harsh Kevadia
"""


from selenium import webdriver
import time


url='https://twitter.com/SHAQ'

#open the browser and visit the url
driver = webdriver.Chrome('chromedriver.exe')
driver.get(url)

#scroll down twice to load more tweets
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)

#find all elements with a class that ends in 'tweet-text'
tweets=driver.find_elements_by_css_selector("[data-item-type=tweet]")

"""
for tweet in tweets:
    print (tweet.find_element_by_css_selector("[class$=tweet-text"))
"""

#write the tweets to a file
fw=open('tweets.txt','w')
for tweet in tweets:
    txt,retweets,favorite,reply,tweetDate='NA','NA','NA','NA','NA'
    
    try: txt=tweet.find_element_by_css_selector("[class$=tweet-text]").text
    except: print ('no text')

    try:
        retweetElement=tweet.find_element_by_css_selector("[class$=js-actionRetweet]")
        retweets=retweetElement.find_element_by_css_selector('[class=ProfileTweet-actionCountForPresentation]').text                                      
    except:
        print ('no retweets')
    
    try:
        favoriteElement=tweet.find_element_by_css_selector("[class$=js-actionFavorite]")
        favorite=favoriteElement.find_element_by_css_selector('[class=ProfileTweet-actionCountForPresentation]').text                                      
    except:
        print ('no favorite')
        
    try:
        replyElement=tweet.find_element_by_css_selector("[class$=js-actionReply]")
        reply=replyElement.find_element_by_css_selector('[class=ProfileTweet-actionCountForPresentation]').text                                      
    except:
        print ('no Reply')
    
    try:
        tweetDate=tweet.find_element_by_css_selector("[data-long-form=true]").text
        #tweetDate = tweetDateElement.find_element_by_css_selector('[class$=js-short-timestamp]').text 
    except:
        print ('no short dates')

    fw.write(txt.replace('\n',' ')+'\t'+str(retweets)+'\t'+str(favorite)+'\t'+str(reply)+'\t'+str(tweetDate)+'\n')


fw.close()


driver.quit()#close the browser