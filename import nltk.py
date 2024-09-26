import re
from nltk.corpus import stopwords

# Function to remove emojis
def remove_emojis(text):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

# **New Part** Function to remove URLs
def remove_urls(text):
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    return url_pattern.sub(r'', text)

# Function to remove stop words, emojis, and URLs
def preprocess_file(file_path):
    # Load stop words
    stop_words = set(stopwords.words('english'))

    processed_lines = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Remove URLs
            line = remove_urls(line)  # **New Part**
            
            # Remove emojis
            line = remove_emojis(line)

            # Remove 'deleted' text or any other specific patterns you want to remove
            line = re.sub(r'\bdeleted\b', '', line)

            # Remove stop words
            words = line.split()
            line = ' '.join([word for word in words if word.lower() not in stop_words])

            processed_lines.append(line)

    # You can either return the processed lines or write them to a new file
    return processed_lines

# Example of writing the processed lines to a new file
def write_processed_lines(processed_lines, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as file:
        for line in processed_lines:
            file.write(line + '\n')


# Usage
file_path = '/Users/sunidhijain13/Desktop/SMDM Project/reddit_data.csv'
processed_lines = preprocess_file(file_path)
output_file_path = '/Users/sunidhijain13/Desktop/SMDM Project/SMDM Processed file  - Sheet1.csv'
write_processed_lines(processed_lines, output_file_path)



