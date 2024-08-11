#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!pip install pymongo


# In[2]:


import pymongo


# ### MongoDB connection with Python

# In[5]:


# connect to mongo
# connecion = pymongo.MonogoClient("path from mongodb driver")

client = pymongo.MongoClient("mongodb+srv://KamleshKasambe:lucifer098@cluster0.2qridwe.mongodb.net/?retryWrites=true&w=majority",
                            tls=True, tlsAllowInvalidCertificates=True)
db = client.test


# In[6]:


#get a handle to the database it will create new if test datebase is not alreaady created
#mydb=connection.test
db_clients = db.clients


# In[11]:


#Cre
client_dict_one = {"name":"Sachin Lavhate", "age":"31", "job":".Net", "email":"sachin@example.com"}

client_dict_many = [{"name":"Sachin Lavhate", "age":"31", "job":"SAP", "email":"sachin@example.com"},
                    {"name":"Guru Singh", "age":"34", "job":"Crystal Record", "email":"guru@example.com"},
                    {"name":"Swaroop Bhandarkar", "age":"25", "job":"Android", "email":"swaroop@example.com"}]


# In[12]:


#insert into DB
db_clients.insert_one(client_dict_one)


# In[13]:


db_clients.insert_many(client_dict_many)


# In[14]:


#Select from Collection
records_all = db_clients.find()


# In[15]:


# Select from collection
records_all = db_clients.find()

for record in records_all:
    print(record['name'], record['age'], record['job'], record['email'])


# In[16]:


# Select from colleciton with where clause
records_all = db_clients.find({'name':"Swaroop Bhandarkar"})

for record in records_all:
    print(record['name'], record['age'], record['job'], record['email'])


# In[18]:


# Update Record
db_clients.update_one({"name": "Guru Singh"}, {"$set":{"age":"22"}})


# In[19]:


# delete record
db_clients.delete_one({"name":"Guru Singh"})


# In[20]:


get_ipython().system('pip install twython')


# In[21]:


from twython import Twython


# In[22]:


consumer_key = 'Qf3n48CQgjq20gwsZooCwpuWG'
consumer_secret = 'wFwbQ0AKOAwTfWEdalQh052hheLTxD5JiMi43bFgll6IIWaVyO'
access_token = '1595353890299461633-mNQcyCF93PxnqbcycSmu6291TtmHtr'
access_token_secret = 'gc5VKqMrfF7xK16k2VAglrswDKvcrRk0FDkcp2dcKifub'


# In[23]:


twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)


# In[24]:


result_dict = twitter.search(q='Tom and Jerry', lang = 'en', count=2, result_type='popular')
print(result_dict)


# In[25]:


list_tweets = result_dict['statuses']
for tweet in list_tweets:
    print(tweet['text'])
    print('#########################################################')


# ## Twitter to MongoDB using Python

# In[27]:


db_tweets = db.tweets


# In[28]:


db_tweets.insert_many(list_tweets)


# In[31]:


records_all = db_tweets.find()

for record in records_all:
    print(record['text'])
    print(record['entities'])
    print(record['created_at'])
    print("##################################################################")


# In[ ]:




