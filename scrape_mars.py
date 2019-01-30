
# coding: utf-8

# In[1]:


#importing dependensies
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd


# In[2]:


#defining the path to the directory
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


#Visit the NASA Mars News to collect News Title & Paragraph
url = 'https://mars.nasa.gov/news/'
browser.visit(url)

html = browser.html
soup = BeautifulSoup(html, 'html.parser')
#soup


# In[4]:


title = soup.find('div', class_= 'content_title').text
paragraph = soup.find('div', class_ = 'rollover_description_inner').text

print(f"Title: {title}")
print(f"Paragraph: {paragraph}")


# In[5]:


#Visit the url for JPL featured space image
url_second = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url_second)

html = browser.html
soup = BeautifulSoup(html, 'html.parser')
#soup


# In[6]:


#use splinter to find the mars featured image
img = soup.find('a', class_ = 'fancybox') ['data-fancybox-href']
img_url = 'https://www.jpl.nasa.gov'+ img
print(img_url)


# In[7]:


#Mars weather tweets
tweet_url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(tweet_url)

html = browser.html
soup = BeautifulSoup(html, 'html.parser')

#saving the tweet
mars_weather = soup.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text
print(mars_weather)


# In[8]:


#Mars facts webpage scrape
facts_url = 'https://space-facts.com/mars/'

mars_info = pd.read_html(facts_url)
mars_info


# In[9]:


mars = (mars_info[0])
mars.columns = ['Measure', 'Value']
mars


# In[10]:


mars_html = mars.to_html(classes = 'mars')
masr_html = mars_html.replace('\n', ' ')
print(mars_html)

