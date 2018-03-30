### title: "Create report performing EDA rendered as Rmarkdown html document with DataExplorer package"###

# Clear workspace and memory
rm(list = ls()); gc(reset = TRUE)

setwd('C:\\Users\\Desktop\\WORKING\\EDA') # change this path to your working directory #

# load dataset

data(iris)
load(iris)
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
