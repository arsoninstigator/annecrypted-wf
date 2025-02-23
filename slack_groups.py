import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

def get_channel_members(client, channel_id):
    """
    get all existing members from private channel
    """
    try:
        result = client.conversations_members(channel=channel_id)
        return result["members"]
    except SlackApiError as e:
        print(f"Error getting channel members: {e.response['error']}")
        return None

def get_usergroup_id(client, usergroup_handle):
    """
    get usergroup id from handle
    """
    try:
        result = client.usergroups_list()
        
        for group in result["usergroups"]:
            if group["handle"] == usergroup_handle:
                return group["id"]
        
        print(f"Usergroup with handle '{usergroup_handle}' not found")
        return None
    except SlackApiError as e:
        print(f"Error getting usergroup ID: {e.response['error']}")
        return None

def add_users_to_group(client, usergroup_id, user_ids):
    """
    add list of users to a usergroup
    """
    try:
        users_string = ",".join(user_ids)
        
        result = client.usergroups_users_update(
            usergroup=usergroup_id,
            users=users_string
        )
        return result["ok"]
    except SlackApiError as e:
        print(f"Error adding users to group: {e.response['error']}")
        return False

def main():
    slack_token = os.environ.get("SLACK_BOT_TOKEN")
    if not slack_token:
        print("Error: SLACK_BOT_TOKEN environment variable not set")
        return
    
    client = WebClient(token=slack_token)

    # enter channel + userid (annecrypted-ping) information 
    channel_id = input("Enter channel ID (e.g., C0123456789): ")
    usergroup_handle = input("Enter usergroup handle (without @): ")
    
    members = get_channel_members(client, channel_id)
    if not members:
        return
    
    print(f"Found {len(members)} members in the channel")
    
    usergroup_id = get_usergroup_id(client, usergroup_handle)
    if not usergroup_id:
        return
    
    # adding the current members to my user group
    success = add_users_to_group(client, usergroup_id, members)
    
    if success:
        print(f"Successfully added {len(members)} members to the usergroup")
    else:
        print("Failed to add members to the usergroup")

if __name__ == "__main__":
    main()