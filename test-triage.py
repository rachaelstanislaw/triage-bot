import slack
import ssl
import os
from pathlib import Path
from dotenv import load_dotenv

# rachael: U0536MSTVBR
# zach: U053J9Z6EAH

env_path = Path('.') / '.env'
load_dotenv(dotenv_path = env_path)
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

client = slack.WebClient(token = os.environ['SLACK_TOKEN'], ssl=ssl_context)

# print(client)

client.usergroups_users_update(usergroup="S053D0FJW2K", users="U053J9Z6EAH")
