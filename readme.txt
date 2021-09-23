these are the basic instructions: 

~~~~~~~~~~~~PYTHON~~~~~~~~~~~~~~~~~

This is home to Edge Wallet app's Discord bots. Written and maintained by two newbs.
If you are reading this and don't work for Edge.... Hi....

for python based apps/bots be sure to download requirements.txt 
in your terminal run "pip install -r requirements.txt" 

also "pip3 install python-dotenv" if not included.

built off of discord.py "pip3 install discord.py" (should be included in requirements.txt)

remember to create a .env file with the these 2 keys:

# .env these are the bouncers auth stuff

DISCORD_TOKEN=''
DISCORD_GUILD=''

loaded in the .py file as 

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


-Berto

~~~~~~~~~~~~~~END PYTHON~~~~~~~~~~~


Below is the instructions for the js portion of our bots. 
Our team divided the task amongst two newbs.
One a python degen and the other commited to learning JavaScript. 


~~~~~~~~~~~~~~JavaScript~~~~~~~~~~~



~~~~~~~~~~~END JavaScript~~~~~~~~~~



