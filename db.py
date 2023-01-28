import json

# Read the JSON file
with open('data.json', 'r') as file:
    data = json.load(file)

# Access the data for a specific user
username = "newton"
for user_data in data['users']:
    if user_data["name"] == username:
        break

# Access the messages for the user
messages = user_data["messages"]

# Iterate through the messages
for message in messages:
    print(message["message"])
    
