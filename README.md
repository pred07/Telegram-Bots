Telegram Bot Setup and Deployment on PythonAnywhere

1. Create a Bot Using BotFather
   
Open Telegram and search for BotFather.
Start a chat and use the following commands:
/newbot – Create a new bot.
Provide a name for your bot (e.g., "MyAssistantBot").
Provide a username (must end with bot, e.g., my_assistant_bot).
BotFather will generate a Token (e.g., 123456789:ABC-DEF1234ghIkl-zyx57W2v1u123ew11).
Save this token securely. It will be used in your Python script.

2. Write the Bot Script
Install the python-telegram-bot library:
pip install python-telegram-bot
Create a Python script (main.py):

3. Test the Script Locally
Run the script:
python main.py
Test the bot by sending /start or /help commands on Telegram.

4. Deploy the Bot on PythonAnywhere
Sign Up/Log In at PythonAnywhere.
Upload Your Script:
Go to the "Files" section.
Upload main.py and any dependencies.
Install Dependencies:

Open a Bash console on PythonAnywhere.
Install python-telegram-bot:
pip install --user python-telegram-bot
Run the Script:

Open a Bash console and run:
python main.py
