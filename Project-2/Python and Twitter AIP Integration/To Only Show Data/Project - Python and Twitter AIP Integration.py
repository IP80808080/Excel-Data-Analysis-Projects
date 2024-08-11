#!/usr/bin/env python
# coding: utf-8

# # Twitter connection with Python

# In[1]:


#!pip install twython


# In[2]:


from twython import Twython


# In[3]:


consumer_key = 'Qf3n48CQgjq20gwsZooCwpuWG'
consumer_secret = 'wFwbQ0AKOAwTfWEdalQh052hheLTxD5JiMi43bFgll6IIWaVyO'
access_token = '1595353890299461633-mNQcyCF93PxnqbcycSmu6291TtmHtr'
access_token_secret = 'gc5VKqMrfF7xK16k2VAglrswDKvcrRk0FDkcp2dcKifub'


# In[9]:


twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)


# In[10]:


result_dict = twitter.search(q='Tom and Jerry', lang = 'en', count=2, result_type='popular')
print(result_dict)


# In[11]:


list_tweets = result_dict['statuses']
for tweet in list_tweets:
    print(tweet['text'])
    print('#########################################################')

