# ChatBot
This repo provides an implementation for a Facebook Messenger chatbot. The bot parses through our group chat messages to find the weekly highlights of the chat, and generates leaderboards for the most interesting posts and most popular group members. It then presents its findings to the gruop chat for everyone to see.

## Getting Started
Before starting, you should already have <b>python3</b> and <b>pip</b> installed on your machine (pip is used to install all the necessary dependencies in the setup script)

### Setup/Installation
After making sure you have <b>python3</b> and <b>pip</b> installed, uncomment the <i>setup()</i> function located at the bottom of <b><i>setup/setup.py</i></b> and run the file. This will install all the required dependencies (shown in <b><i>requirements.txt</i></b>), and will guide you through generating the <b><i>config.txt</i></b> file needed for running the chat bot

Make sure <b><i>setup.py</i></b> is being run while you are located in the root directory. If you are running it thru the command line, run:
<br>
<br>
```python setup/setup.py``` on <b>Windows</b>
<br>
```python3 setup/setup.py``` on <b>Linux</b>

<b><i>*Note: If you are using Pycharm, you can just right-click the file and hit run</i></b>

After the dependencies are installed, the script will prompt you to enter all the necessary information required to run the bot, such as yout downloads directory, and the messages you want the bot to say when entering and leaving the chat.

After this is done, the <b><i>config.txt</i></b> file will be generated in the <b><i>setup/</i></b> directory, and you should be good to go

### Configuring chat name/URL
The default behavior for the bot is configured for personal purposes; therefore, it is harcoded to use a group chat that starts with <i>ORIGATO</i>. These values can be changed via the DESTINATION_URL in <b><i>web/message_with_media_send_logger.py</i></b>, and by changing the directory manipulation functions in <b><i>web/json_download_logger.py</i></b>
