# Project Plan

## Title
<!-- Give your project a short title. -->
COVID-19: A Data Science Approach to Understanding the Pandemic

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
1. How did the COVID-19 pandemic spread and how it came to control?

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
Understanding the spread and control of the COVID-19 pandemic is a complex task. The pandemic has affected the lives of billions of people around the world. The results we find could give us insights about how it spread throughout the different countries and how it came to finally control. Furthermore, we could also look into the tweets related to COVID-19 and see different aspects of the pandemic that people are talking about.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: Coronavirus Pandemic (COVID-19)
* Metadata URL: https://github.com/owid/covid-19-data/tree/master/public/data
* Data URL: https://covid.ourworldindata.org/data/owid-covid-data.csv
* Data Type: CSV

The dataset is maintained by **Our World in Data**. It is updated daily and includes data on confirmed cases, deaths, hospitalizations, testing, and vaccinations, as well as other variables of potential interest. This project will use the snapshot of data at November 8, 2023.


### Datasource 2: COVID19 Tweets
* Metadata URL: https://www.kaggle.com/datasets/gpreda/covid19-tweets
* Data URL: https://www.kaggle.com/datasets/gpreda/covid19-tweets
* Data Type: CSV

This dataset is available in Kaggle and contains tweets related to COVID-19. It contains tweets from the date of `2020-07-25` to `2020-08-30`. 

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Preprocess both datasets and clean unwanted columns as well as try to maintain the date of both dataset same for correlation purposes. [#1][i1]
2. Plot EDA trends of cases, deaths, hospitalizations, testing, and vaccinations over time for data 1 and trend of tweets, tweet vs hour, day and so on. [#2][i2]
3. Make assumptions and try to find the correlation between the two datasets. [#3][i3]
4. Insights: Did the assumptions really work? [#4][i4]

[i1]: https://github.com/q-viper/MADE-WS23/issues/1
[i2]: https://github.com/q-viper/MADE-WS23/issues/2
[i3]: https://github.com/q-viper/MADE-WS23/issues/3
[i4]: https://github.com/q-viper/MADE-WS23/issues/4
