# Achilles, Neural Network to Predict Commodities 
Integration with Trading Bot for Automatic Trading 🖤🤖🖤     💲Ready to Predict the Future?💲

Achilles Is a LSTM (Long Short Term Memory) Architecture made and optimized to predict GOLD Vs USD. For this implementation we take the power of LSTM, we process our data with two techinal indicators (EMA, RSI)
We make predictions with our model. Then we scrapt the news from 3 different websites, Implementing sentiment analysis and Forward Prediction we integrate these components in a trading bot for automatic trading

After a one-month period testing our model had 162% return in capital. Demostrating that Machine Learning with LSTM Can predict the stock market and can be integrated into automatic trading without human intervention.


----->> First Component: (Achilles) LSTM Neural Network trained on seasonal Times Frames 15 Minutes, 5 Minutes and 1 Minute data of the S&P500 Market, with this model we'll try to predict the future market during 30 days or 33000 minutes
We're getting the estimate prices of the market and we'll save this into a CSV file for our trading bot

----->>Second Component: FINbert Sentiment Analysis to scratch and estimate the news in 3 different WebSites:

  -https://www.benzinga.com (XAU-USD)
  
  -https://www.investing.com (XAU-USD)
  
  -https://www.ft.com (General Market News)

----->> Third Component: Trading bot Used in mt5 in a Paper account. Based on the predictions made by Achilles and the real-time sentiment news the model trades, sending buy and sell orders. The bot runs each minute since the predictions are in a minute-by-minute timeframe. This allows our model to take profit fast in the market and reduce large fluctuations. 

You can see the paper we have on this link:   https://arxiv.org/pdf/2410.21291
(Working in a Journal Paper for Updated Version of Achilles)
