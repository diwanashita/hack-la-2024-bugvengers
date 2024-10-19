import json
import pandas as pd

# Load JSON data
with open("../data/hack-la-24-banksy-discussions.json") as jsonfile:
    data = json.load(jsonfile)

# Create a list to hold the parsed data
parsed_data = []

# Extract discussion topic
for item in data:
    discussion_topic = item['discussion_topic']
    # Append the main discussion topic
    main_topic = {
        'discussion_id': discussion_topic['id'],
        'title': discussion_topic['title'],
        'message': discussion_topic['message'],
        'posted_at': discussion_topic['posted_at'],
        'user_name': discussion_topic['user_name']
    }
    parsed_data.append(main_topic)

    # Extract replies
    for reply in discussion_topic['replies']:
        reply_data = {
            'discussion_id': discussion_topic['id'],
            'reply_id': reply['id'],
            'user_name': reply['user_name'],
            'message': reply['message'],
            'created_at': reply['created_at']
        }
        parsed_data.append(reply_data)

# Create DataFrame
df = pd.DataFrame(parsed_data)

csv_file_path = 'data/discussion_data.csv'
df.to_csv(csv_file_path, index=False)
