
# coding: utf-8

# # Data Science Masters :Assignment 13
Read the following data set:
https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data
Task:
1. Create an sqlalchemy engine using a sample from the data set
2. Write two basic update queries
3. Write two delete queries
4. Write two filter queries
5. Write two function queries
# In[73]:


import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data",header=None, names = ['age','workclass','fnlwgt','education','educationnum','maritalstatus','occupation','relationship','race','sex','capitalgain','capitalloss','hoursperweek','nativecountry','prob'])
df = df.drop(['prob'],axis=1)
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)


# In[83]:


# 1. Create an sqlalchemy engine using a sample from the data set
engine = create_engine('sqlite://', echo=False)
df.head(10).to_sql('adultdb', con=engine)
engine.execute("SELECT * FROM adultdb;").fetchall()


# In[84]:


#2. Write two basic update queries
# Solution
# Update 1 query - Updating Male and Female to M and F resepectively... 
engine.execute("""
UPDATE adultdb 
SET sex = CASE
              WHEN sex='Male' THEN 'M'
              WHEN sex='Female' THEN 'F'
              ELSE sex
          END
""")
engine.execute("Select * from adultdb LIMIT 5;").fetchall()


# In[85]:


# Update 2 Query -  Updating Bachelors as BE...
engine.execute("""
UPDATE adultdb
SET education = 'BE'
WHERE education = 'Bachelors';
""")
engine.execute("Select * FROM adultdb LIMIT 5;").fetchall()


# In[86]:


# 3. Write two delete queries
# Solution
# Delete 1 Query - Deleting records for country Cuba
engine.execute("""
DELETE FROM adultdb WHERE nativecountry = 'Cuba';
""")
engine.execute("Select * FROM adultdb;").fetchall()


# In[87]:


# Delete 2 Query -  Deleting a row where race is black and age above 50
engine.execute("""
DELETE FROM adultdb WHERE race = 'Black' AND age > 50;
""")
engine.execute("Select * FROM adultdb;").fetchall()


# In[88]:


# 4. Write two filter queries
# Solution
# Filter 1 Query - Filtering private secotor employees
engine.execute("SELECT * FROM adultdb WHERE workclass = 'Private';").fetchall()


# In[89]:


# Filter 2 Query - Filtering based on age <40
engine.execute("SELECT workclass,age,education FROM adultdb WHERE age < 40;").fetchall()


# In[90]:


# 5. Write two function queries
# Solution
# Function 1 Query - Calculating Mean value for age.. 
engine.execute("SELECT AVG(age) as Avg_ageValue FROM adultdb;").fetchone()


# In[91]:


# Function 2 Query -  Finding edcuation distribution 
engine.execute("""SELECT education, COUNT(education) FROM adultdb GROUP BY education;""").fetchall()

