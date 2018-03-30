# EDA

Like any aspiring data scientist out there, i also started my journey mostly doing Exploratory Data Analysis (EDA). 
Let us understand one thing very clearly that, before we talk about AI or infact any machine learning stuff, Data Analysis plays a very important role in the entire Data Science Workflow. In fact, it takes most of the time of the entire Workflow.

EDA is the initial and an important phase of the workflow. It helps, to get a first look of the data, and help generate relevant hypothesis and decide next steps. However, the EDA process could be a hassle most of the times.

There are many libraries & packages for Python & R with which most basic data analysis can be done.

But, i would like to share 2 interesting ones which i feel is the most suitable for quick analysis. This is my personal opinion. I am not saying that the others are not good. I acknowledge the authors for their wonderful contribution to the community.

Python EDA package:-
--------------------
pandas-profiling

It generates profile reports from a pandas DataFrame. 

----------------------------------------------------------
For each relevant column based on the column type an descriptive statistics is presented in an interactive HTML report along with the following features:-

Essentials: type, unique values, missing values
Quantile statistics: like minimum value, Q1, median, Q3, maximum, range, interquartile range

Descriptive statistics: like mean, mode, standard deviation, sum, median absolute deviation, coefficient of variation, kurtosis, skewness

Most frequent values

Histogram

Correlations: highlighting of highly correlated variables, Spearman and Pearson matrixes

Installation:-
-------------

pip install pandas-profiling
 or 
conda install pandas-profiling

R EDA package:-
---------------
DataExplorer

Creates report performing the entire EDA rendered as Rmarkdown html document.

Installation:-
--------------

install.packages("DataExplorer")

--------------------------------------------------------

Now let us go through a simple exercise for the usage of these libraries & packages individually.

Dataset: IRIS 
(This data sets consists of 3 different types of iris flowers mainly Setosa, Versicolour, and Virginica)

Note:- For the sake of simplicity & clear understanding i sticked to this dataset, but all the above steps will work for any dataset.

Python code:-
-------------

# Import pandas & pandas_profiling libraries

import pandas as pd

import pandas_profiling

# For IRIS dataset import the datasets from sklearn
from sklearn import datasets

# import data 
iris = datasets.load_iris()

# check type 
type(iris)

# Converting to pandas dataframe
iris_data = pd.DataFrame(iris.data, columns=iris.feature_names)

# labeling the target
iris_data['target'] = iris['target']

# get the number of rows and columns
iris_data.shape

# list the columns
iris_data.columns

# rename columns
iris_data.columns=['sepal_length', 'sepal_width', 'petal_length','petal_width', 'class']

iris_data.columns

# see few records
iris_data.head()

# check the distribution of the class 
iris_data['class'].value_counts()

# To generate Inline report without saving object
pandas_profiling.ProfileReport(iris_data)

# To retrieve the list of variables which are rejected due to high correlation

profile = pandas_profiling.ProfileReport(iris_data)

# Rejected variables
rejected_variables = profile.get_rejected_variables(threshold=0.9)

rejected_variables

# To Generate a HTML report file
profile = pandas_profiling.ProfileReport(iris_data)

# output to html file
profile.to_file(outputfile="../profiling_iris.html")


R code:-
--------
### title: "Create report performing EDA rendered as Rmarkdown html document with DataExplorer package"###

# Clear workspace and memory
rm(list = ls()); gc(reset = TRUE)

setwd('C:\\Users\\Desktop\\WORKING\\EDA') # change this path to your working directory #

# load dataset

data(iris)

load(iris)

# set seed for reproducibility 
set.seed(250)

#Let us begin our Exploratory Data Analysis by loading the library:
library(DataExplorer)

# Variables
# The very first thing that you'd want to do in your EDA is checking the dimension of the input dataset.
plot_str(iris)

# Looking for Missing Values
plot_missing(iris)

# Histogram of Continuous Variables
plot_histogram(iris)

# Density plot
plot_density(iris)

# Colorful Correlation Plot
plot_correlation(iris, type = 'all','Species')

# plot Categorical Variables - Barplots!
plot_bar(iris) 

# Finally,create consolidated report with create_report()
create_report(iris) #comment this if you're not rendering this entire rmarkdown

Conclusion
----------
We see that both the packages aims to automate most of data handling and visualization stuff, so that users could focus on studying the insights.


Acknowledgment
--------------
[1] Author: Jos Polfliet
https://pypi.python.org/pypi/pandas-profiling

[2] Author: Boxuan Cui
https://cran.r-project.org/web/packages/DataExplorer/index.html


