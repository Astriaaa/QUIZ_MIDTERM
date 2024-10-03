import requests
import json


access_token = "ZjdkMDJlMDAtYjg2MC00ODhjLTljZDMtODJjOWRiMWZkOGIxYTdlOTNjYmUtZDcz_P0A1_60c4241b-f916-4111-96c4-b4c6eecaa22e"


meeting_title = "Marcoso Meeting"
start_time = "2024-10-15T14:00:00Z"
end_time = "2024-10-17T15:00:00Z"


room_name = "Marcoso Room"
participant_email = "dennissegailfrancisco@baliuagu.edu.ph"


message_text = "SHESH"


url = "https://webexapis.com/v1/"
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}


meeting_data = {
    "title": meeting_title,
    "start": start_time,
    "end": end_time
}
response = requests.post(url + "meetings", headers=headers, json=meeting_data)


if response.status_code == 200:
    print("Meeting created successfully!")
    meeting_id = response.json()["id"]
    print(f"Meeting ID: {meeting_id}")
else:
    print("Failed to create meeting.")


room_data = {
    "title": room_name
}
response = requests.post(url + "rooms", headers=headers, json=room_data)


if response.status_code == 200:
    print("Room created successfully!")
    room_id = response.json()["id"]
    print(f"Room ID: {room_id}")
else:
    print("Failed to create room.")


membership_data = {
    "roomId": room_id,
    "personEmail": participant_email,
    "isModerator": False
}
response = requests.post(url + "memberships", headers=headers, json=membership_data)


if response.status_code == 200:
    print("Participant added successfully!")
else:
    print("Failed to add participant.")


message_data = {
    "roomId": room_id,
    "text": message_text
}
response = requests.post(url + "messages", headers=headers, json=message_data)


if response.status_code == 200:
    print("Message sent successfully!")
    message_id = response.json()["id"]
    print(f"Message ID: {message_id}")
else:
    print("Failed to send message.")


response = requests.get(url + f"messages?roomId={room_id}", headers=headers)


if response.status_code == 200:
    print("Messages retrieved successfully!")
    messages = response.json()["items"]
    for message in messages:
        print(f"Message ID: {message['id']}, Text: {message['text']}")
else:
    print("Failed to retrieve messages.")


def delete_message(message_id):
    response = requests.delete(url + f"messages/{message_id}", headers=headers)
    if response.status_code == 204:
        print("Message deleted successfully!")
    else:
        print("Failed to delete message.")


delete_message(message_id)