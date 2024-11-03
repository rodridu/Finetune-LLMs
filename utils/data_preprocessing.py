import os
import pandas as pd
import json

# Set the working directory
def set_directory(path):
    os.chdir(path)

# Load and preprocess the data
def load_and_preprocess_data(filename):
    df = pd.read_csv(filename)
    df = df[['text', 'sentiment']]
    sentiment_mapping = {0: 'Neutral', 1: 'Positive', -1: 'Negative'}
    df['sentiment'] = df['sentiment'].map(sentiment_mapping)
    return df

# Convert the DataFrame to the new JSONL format
def convert_to_new_format(old_data):
    new_data = []
    for _, row in old_data.iterrows():
        new_entry = {
            "messages": [
                {"role": "system", "content": 'Would the sentence positively, negatively, or neutrally influence the stock price?'},
                {"role": "user", "content": row["text"]},
                {"role": "assistant", "content": row["sentiment"]}
            ]
        }
        new_data.append(new_entry)
    return new_data

# Save the converted data to a JSONL file
def save_to_jsonl(data, file_path):
    with open(file_path, 'w') as file:
        for record in data:
            json_record = json.dumps(record)
            file.write(json_record + '\n')

# Main processing function
def main():
    # Change to your directory path
    set_directory('/content/drive/MyDrive/xian')
    
    # Load and preprocess data
    df = load_and_preprocess_data('sentences_with_sentiment.csv')
    
    # Convert the data to the new format
    converted_data = convert_to_new_format(df)
    
    # Specify the file path to save
    file_path = 'train_gpt_trust_issue.jsonl'  # or other filenames for validation/test sets
    
    # Save the processed data
    save_to_jsonl(converted_data, file_path)
    print(f"Data saved to {file_path}")

# Execute the main function
if __name__ == "__main__":
    main()