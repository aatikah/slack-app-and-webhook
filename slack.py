import requests

# Replace with your webhook URL
webhook_url = "https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX"

# Message payload
message = {"text": "Hello from my Slack app!"}

# Send the POST request
response = requests.post(webhook_url, json=message)

# Check the response
if response.status_code == 200:
    print("Message sent successfully!")
    print(response.status_code)
else:
    print(f"Failed to send message. Status code: {response.status_code}")
