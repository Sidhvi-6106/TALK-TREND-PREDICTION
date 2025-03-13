from flask import Flask, request, render_template
from data_collection import fetch_twitter_data, fetch_reddit_data, fetch_news_data
from data_preprocessing import preprocess_text
from trend_detection import detect_trends
from predictive_model import train_model
from visualization import plot_trends

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    query = request.form['query']
    
    # Fetch data from APIs
    twitter_data = fetch_twitter_data(query)
    reddit_data = fetch_reddit_data(query)
    news_data = fetch_news_data(query)

    # Preprocess and combine data
    combined_data = twitter_data + reddit_data + news_data
    processed_data = [preprocess_text(text) for text in combined_data]

    # Detect trends
    trends = detect_trends(processed_data)

    # Plot trends (optional)
    plot_trends(trends)

    return render_template('results.html', trends=trends)

if __name__ == '__main__':
    app.run(debug=True)
