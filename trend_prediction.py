from collections import Counter

def detect_trends(data):
    all_words = ' '.join(data).split()
    word_counts = Counter(all_words)
    return word_counts.most_common(10)  # Top 10 trending topics
