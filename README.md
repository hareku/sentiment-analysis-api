# Japanese Text Sentiment Analysis API

This is Japanese Text Sentiment Analysis API.
The sentiment score is calculated by **Multinomial Naive Bayes**.

```bash
curl http://localhost:3000/?sentence=この映画は最高です
# {"result": {"Positive": 0.7202986438902886, "Negative": 0.05249962331310942, "Neutral": 0.22720173279659972}}
```

You can deploy to AWS (API Gateway + Lambda).

## Prepare the dataset

This app uses [Twitter日本語評判分析データセット](http://www.db.info.gifu-u.ac.jp/data/Data_5d832973308d57446583ed9f) for training, that includes about 500k tweets and their sentiment labels.

But **dataset doesn't include tweet text to obey Twitter Terms of Service**. So you have to download tweet texts yourself via Twitter API and store CSV to `sentiment_api/data/tweets_dataset.csv`.

## Local development

```bash
# install dependencies
pip3 install -r requirements.txt
pip3 install -r sentiment_api/requirements.txt

# execute `sentiment_api/training.ipynb`, it trains dataset and create models.

# this command invokes ./sentiment_api/Makefile.
sam build

# you can see http://localhost:3000/?sentence=xxx
sam local start-api
```

## Deploy to AWS

```bash
sam deploy --guided
```
