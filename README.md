# Data-Analysis-Visualization-and-Exploration-on-NYC-AirBnb

# Project Description

  The motivation for the project is to understand the relationship between different AirBnb’s and other attributes considered to choose an AirBnb. My interest lies in Real Estate and I wanted to understand how Data Analysis plays a role in Real Estate. Data Analysis can help investors determine how profitable a location will be in terms of occupancy rates, average rental income and even Return on Investment on the area. This helps in increasing the economy of the country. It helps in analyzing location, price, customer trends, competition etc.
  
  New York City is one of the busiest and most famous places in the world. New York City attracts almost one-third of all foreign visitors to the United States and in 2019, New York City welcomed 67 million visitors. NYC is therefore one of the hottest markets for Airbnb and hence I chose the New York AirBnb Dataset for my project. 
  
  The purpose of the project is to understand the relation between price of the AirBnb in NYC with other attributes. In this project, I have performed Data Wrangling, Data Transformation and Data Visualization using Spark RDD to benefit from parallel processing. I have then stored the clean data in MongoDB to analyse, explore and visualize pre-analyzed results of the data using an interactive UI deployed in Heroku.
  

# Architecture

![](/application/static/css/images/readme/architecture.png)


# Dataset 

For this project I am using a dataset that is hosted on Kaggle.com.

https://www.kaggle.com/dgomonov/new-york-city-airbnb-open-data

In the dataset there are 16 parameters, the parameters consists information about the AirBnb name along with the price as well as 14 other features. There are 48895 records in the dataset.

The parameters are : 
1. id :  listing ID
2. name : name of the listing
3. host_id : host ID
4. host_name : name of the host
5. neighbourhood_group : location
6. neighbourhood : area
7. latitude : latitude coordinates 
8. longitude : longitude coordinates
9. room_type : listing space type
10. price : price in dollars
11. minimum_nights : amount of nights minimum
12. number_of_reviews : number of reviews
13. last_review : latest review date
14. reviews_per_month : number of reviews per month
15. calculated_host_listings_count : amount of listing per host
16. availability_365 : number of days when listing is available for booking

![](/application/static/css/images/readme/exampleDataSet.png)


# Data Problems Addressed  

Data Cleaning/Data wrangling : The dataset has many missing values and unnecessary features. I have addressed this issue by analyzing the dataset and checked for missing values and replaced it with 0 and removed unnecessary attributes like id, host_ame, last_review. Since the dataset is large I have used Spark RDD for data cleaning to benefit from parallel processing.

Data Transformation : I have altered the structure of the data which is put to a NoSQL database using a python script for faster query execution.

Data Storage and Retrieval : For faster retrieval of search results I have uploaded the cleaned data to MongoDB (a NoSQL database) in the project. I have used indexes to make data retrieval faster by reducing the number of disk I/Os. 

Data Aggregation/Exploration : The dataset is analyzed and I have analyzed the correlation between attributes using Spark. Data exploration is performed using Spark RDD. Users can analyze and explore the data using an interactive UI implemented using Flask, Jinja2, HTML5 and CSS3. 

Data Visualization : As data plays a vital role in every industry. The presentation of data decides the fate of any industry. AirBnb uses visualization tools for enhanced customer engagement to make profitable business and so I have visualized all the attributes and their relationship using Spark RDD. The users can visualize the pre-analyzed visualization results in the UI.  


# Database 

The original data is in .csv format. After performing data cleaning and wrangling the cleaned data is stored in MongoDB. Since the data set is large and to display search (exploration) results faster a NoSQL database is used in the project. I am using MongoDB as the database because retrieval from MongoDB is faster and efficient. Using indexed fields, querying on MongoDB is faster as indexes make data retrieval faster by reducing the number of disk I/Os.

# Application URL 
https://new-york-airbnb-dsci551.herokuapp.com/ 



