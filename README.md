# Facebook-Sentiment-Analysis
Simple basic script to retrieve and perform Sentiment Analysis on Facebook Posts.


<b>Dependencies</b>
* facebook-sdk
* NLTK
* TextBlob
* Facebook Access Token

<b>Setup</b>

* Install NLTK: 
 - http://www.nltk.org/install.html
 
* Download the corpora files and trained model:
```bash
$ python
>>> import nltk
>>> nltk.download('all')
```

* install facebook-sdk and TextBlob:
```bash
$ sudo pip install facebook-sdk TextBlob
```

* Get your ACCESS_TOKEN:
https://developers.facebook.com/docs/graph-api/overview

<b>Usage</b>
```bash
$ python simple_facebook_sentiment_analysis.py --access_token YOUR_ACCESS_TOKEN --profile=profilename
