
# coding: utf-8

# In[1]:

# Import pandas & pandas_profiling libraries
# For IRIS dataset import the datasets from sklearn
import pandas as pd
import pandas_profiling
from sklearn import datasets


# In[2]:

# import data 
iris = datasets.load_iris()


# In[3]:

# check type 
type(iris)


# In[4]:

# Converting to pandas dataframe
iris_data = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_data['target'] = iris['target']


# In[5]:

# get the number of rows and columns
iris_data.shape


# In[6]:

# list the columns
iris_data.columns


# In[7]:

# rename columns
iris_data.columns=['sepal_length', 'sepal_width', 'petal_length',
       'petal_width', 'class']


# In[8]:

iris_data.columns


# In[9]:

# see few records
iris_data.head()


# In[10]:

# check the distribution of the class 
iris_data['class'].value_counts()


# In[11]:

# To generate Inline report without saving object
pandas_profiling.ProfileReport(iris_data)


# In[12]:

# To retrieve the list of variables which are rejected due to high correlation

profile = pandas_profiling.ProfileReport(iris_data)
rejected_variables = profile.get_rejected_variables(threshold=0.9)


# In[13]:

rejected_variables


# In[15]:

# To Generate a HTML report file
profile = pandas_profiling.ProfileReport(iris_data)
profile.to_file(outputfile="../profiling_iris.html")


# In[ ]:



