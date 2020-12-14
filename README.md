# Topic Modeling and Causality Evaluation

An evaluation of how coverage of topics in tweets with cashtags ($TSLA, $PLTR, $NFLX) are causally linked to the price of the respective stock.

#### Team Members:

  **Captain -> Akhil Bhamidipati (akhilsb2)**,
  Angeeras Ramanath (ar13),
  Joshua Perakis (perakis2)
  
## Introduction

We proposed to implement the paper titled Mining Causal Topics in Text Data: Iterative Topic Modeling with Time Series Feedback. In this paper they used AAL and AAPL stock as well as Presidential Probability odds as time series data and New York Times text data. The topic modeling is generic, however, in the paper they only implement the PLSA (Probabilistic Semantic Analysis) method. The paper uses both Pearson correlation coefficient and Granger causality to quantitatively evaluate the correlations. Our project was to implement the iterative topic modeling with time series feedback (ITMTF) algorithm to identify which words from tweets are linked causally to stock price changes.

## ITMTF Algorithm

Below is a general summarization / pseudocode of the ITMTF algorithm which helped us understand the paper: 

1. Identify our time series response data (X = x1, ..., xn) with timestamp t1, ..., tn
 1a. Stock data
2. Identify collection of documents form same time period D = {(d1,td1), ..., (dm, tdm)}
 2a. Twitter tweets
3. Use a topic modeling method to generate topics for each doc  T1, .., Ttn
 3a. This topic modeling method is M
 3b. Going to apply M to D, 
4. Find topics with high causality
5. For each topic apply C to find most significant causal words in the top words of the topic and get the impact of these significant words
6. Separate positive impact terms and negative impact terms
7. Assign prior probabilities according to significance level
8. Use the prior to repeat until we reach good topic quality
