import matplotlib.pyplot as plt

def plot_trends(trends):
    topics, counts = zip(*trends)
    plt.figure(figsize=(10, 5))
    plt.bar(topics, counts)
    plt.title('Trending Topics')
    plt.xlabel('Topics')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('static/trends.png')  # Save the plot as an image
