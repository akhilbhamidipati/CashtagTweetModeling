# Topic Modeling and Causality Evaluation

An evaluation of how coverage of topics in tweets with cashtags ($TSLA, $PLTR, $NFLX) are causally linked to the price of the respective stock.

#### Team Members:

  **Captain -> Akhil Bhamidipati (akhilsb2)**,
  Angeeras Ramanath (ar13),
  Joshua Perakis (perakis2)
  
## Introduction

We proposed to implement the paper titled Mining Causal Topics in Text Data: Iterative Topic Modeling with Time Series Feedback. In this paper they used AAL and AAPL stock as well as Presidential Probability odds as time series data and New York Times text data. The topic modeling is generic, however, in the paper they only implement the PLSA (Probabilistic Semantic Analysis) method. The paper uses both Pearson correlation coefficient and Granger causality to quantitatively evaluate the correlations. Our project was to implement the iterative topic modeling with time series feedback (ITMTF) algorithm to identify which words from tweets are linked causally to stock price changes.

Hyun Duk Kim, Malu Castellanos, Meichun Hsu, ChengXiang Zhai, Thomas Rietz, and Daniel Diermeier. 2013. Mining causal topics in text data: Iterative topic modeling with time series feedback. In Proceedings of the 22nd ACM international conference on information & knowledge management (CIKM 2013). ACM, New York, NY, USA, 885-890. DOI=10.1145/2505515.2505612

## ITMTF Algorithm

Below is a general summarization / pseudocode of the ITMTF algorithm which helped us understand the paper: 

1. Identify our time series response data (X = x1, ..., xn) with timestamp t1, ..., tn

> 1a. Stock data

2. Identify collection of documents form same time period D = {(d1,td1), ..., (dm, tdm)}
 
> 2a. Twitter tweets

3. Use a topic modeling method to generate topics for each doc  T1, .., Ttn
 
> 3a. This topic modeling method is M
 
> 3b. Going to apply M to D, 

4. Find topics with high causality

5. For each topic apply C to find most significant causal words in the top words of the topic and get the impact of these significant words

6. Separate positive impact terms and negative impact terms

7. Assign prior probabilities according to significance level

8. Use the prior to repeat until we reach good topic quality

## Purpose

The goal of this project was to find relevant words which where causally linked with price movements so that we could use the document collection in the future to predict trends. Ultimately, what our code does is evaluate which words' coverages over time are most strongly causally linked to changed in price within a 5-day lag. Further improvements on our project will be able to more effectively find significantly causal words which are linked to movements in price and more accurately predict changes in stock prices based on the coverage of topics in tweets with the respective cashtag. 

## Implementation

1. We begin by using Tweepy, a twitter querying API to retreive tweets with the cashtags $TSLA, $PLTR, and $NFLX and format them into files with their date and the tweet.
2. Parse the files from step 1 to make document collections
3. Create corpuses to maintain a vocabulary and calculate word coverage over time in the time series
4. Use Granger Testing to test for a causality relationship where the coverage of a word over time in the given corpus "Granger causes" the change in the stock's price within a lag of 5 days.
5. Evaluate words which are significantly causal and possible implications/inferences.

## A Walk-Through of our Project

Take a look at our demo video on Youtube: 

In the file twitter_stock.py you will find the first steps of our project which involved retrieval of tweets. We then generated the tweets we retreived into the files tweet_data_tsla.txt, tweet_data_pltr.txt, and tweet_data_nflx.txt. At this point we were ready for the main portion of our project which can be found in doc_collection_topic_modeling.html or doc_collection_topic_modeling.ipynb. In this step, we first parsed the data from the previous files to create comprehensive document collections and then went ahead and intialized corpuses for all of these document collections while ignoring stopwords. After intializing these corpuses, we performed topic modeling calculations (which are further documented in doc_collection_topic_modeling.html) to understand the coverage of the most highly covered words at any point in our time series over time. Once we had narrowed down our list of words for every corpus along with their coverage over time, we converted these data frames into csv's so that we could import them in R and perform Granger tests. The final step of our project can be observed in grangertesting.html or grangertesting.Rmd and what it essentially comprises of is hand-selecting topics from the top 200 topics that we had filtered for in the previous step, and then performing a Granger test for causality from the coverage of that topic in the time series to movements in that stock's price within 5 days. After completing that last step, we were able to find a few words who's coverage over time was causally linked to changes in the stock's price.

## Contributions of Each Member

The project began with data collection by Joshua. The team decided that Twitter is a good platform to retrieve data from. After setting up a developer account, he began to pull tweets that contained PLTR, NFLX, and TSLA. 100 tweets were pulled from every day for the last month all using Twitter’s API. These tweets were written into a respective .txt file and each tweet was treated as a document. Angeeras led the algorithms for topic modeling. Akhil contributed to the topic modeling as well. On top of that, he implemented Granger tests in R. The dataset for these algorithms to be run on came from the tweets that Joshua provided as well as the stock data that Akhil provided from Yahoo Finance. Overall the project was split very well. The contributions made by all members were all equally important in completing the project and also a great learning experience in applying class material to real world analysis.


