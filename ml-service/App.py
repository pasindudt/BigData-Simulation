from flask import Flask, request, jsonify
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)

@app.route('/sentiment', methods=['POST'])
def get_sentiment_score():
    text = request.data.decode('utf-8')
    if not text:
        return jsonify({"error": "Please provide text in the request body."}), 400

    analyzer = SentimentIntensityAnalyzer()
    sentiment_scores = analyzer.polarity_scores(text)
    compound_score = sentiment_scores['compound']

    if compound_score >= 0.05:
        sentiment = 'Positive'
    elif compound_score <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'

    return jsonify({"text": text, "sentiment": sentiment, "score": compound_score})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8789)
