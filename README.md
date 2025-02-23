# slack workflow
making a slack workflow to promote my private channel and also let people run it to join (or request to join) my otherwise private hack club slack channel :3 you can run the workflow yourself [here](https://slack.com/shortcuts/Ft08EM42TUUC/40b9b090ac9aaa29c4349fec2b1f95ef) to be added to my channel + ping group since i mostly just rant there

<img width="500" alt="image" src="https://github.com/user-attachments/assets/b4ee727d-3466-4d47-adb7-84f9d0a6675a" />
<img width="300" alt="image" src="https://github.com/user-attachments/assets/68303209-6d9d-4cd6-b4ac-6e2d9ec750da" />



i was initially super confused how to set this up and  ended up connecting my app to zapier to maybe figure out what was going on (which did not help at all) since i knew what i wanted the thing to do but wasn't seeing any options for the exact things i was looking for. no-code options have truly never worked for me but me being lazy tried it out anyway

![Screenshot 2025-02-12 195303](https://github.com/user-attachments/assets/818b9525-af9c-496b-b490-ad13734b50ec)


i then started out with the slack api (even dumber move, i know). i created an app called "test" and set permissions. i wanted to make it in a way that i would need to add all the people currently in my channel to a user group, the same user group that anyone who clicks on the said workflow is added to (inside my private channel).

![image](https://github.com/user-attachments/assets/3942a575-48b2-4fa8-8816-ca1bb21bbf03)

i then set the permissions on ouath permissions tab and then generated my token to be used in the code written on slack_groups.py but here's a preview of the code and what it was set to accomplish (or attempted to accomplish)

<img width="1051" alt="image" src="https://github.com/user-attachments/assets/fb4a0a51-9e23-40d1-bec0-c2c48ff4a254" />

```
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
```


i ran the code and ran into several errors but after debugging and rerunning and rerunning again, it finally worked (for some reason chatgpt kept telling me that the channel id needed to start with a g-id for the api to accept it but that made no sense to me since googling tells me that channels (even priv ones) stopped having g-id's in may 2021 so newer channels wouldn't have one anyway (still confused on this).

<img width="784" alt="image" src="https://github.com/user-attachments/assets/e1baf07f-aeba-4bb3-be5f-901305da191c" />

i messed around with the workflows tab on the slack and was pretty much able to understand what steps i would need to take to make it such that whoever ran the workflow was added to my channel but i took some barebones inspiration from arnav's priv channel workflow but decided i wanted something simple and direct and not messy like @ spc's simple workflow called "amethyst goblin"

<!--
<img width="299" alt="image" src="https://github.com/user-attachments/assets/1e522e21-f4c5-45fe-870c-c1dc346f19c8" />
<img width="284" alt="image" src="https://github.com/user-attachments/assets/387a0de8-0c80-45c0-a466-e0f4b5dec109" /> -->
<img width="285" alt="image" src="https://github.com/user-attachments/assets/ef525934-9e70-4da9-8677-8c244ffd6118" />

<img width="291" alt="image" src="https://github.com/user-attachments/assets/48f9d802-8e28-4d0e-b378-cf1af994ddfd" />

