# ChatBot
This repo provides an implementation for a Facebook Messenger chatbot. The bot parses through our group chat messages to find the weekly highlights of the chat, and generates leaderboards for the most interesting posts and most popular group members. It then presents its findings to the gruop chat for everyone to see.

## Getting Started
Before starting, you should already have python3 and pip installed on your machine (pip is used to install all the necessary dependencies in the setup script)

### Setup/Installation
After making sure you have Python3 and Pip installed, uncomment the 'setup()' function located at the bottom of setup/setup.pyn and run the file. This will install all the required dependencies (shown in requirements.txt), and will guide you through generating the config.txt file needed for running the chat bot

Make sure setup.py is being run while you are located in the root directory. If you are running it thru the command line, this means using a command like 'python setup/setup.py' if you are on Windows, or 'python3 setup/setup.py' if you are on Linux.

*Note: If you are using Pycharm, you can just right-click the file and hit run

After the dependencies are installed, the script will prompt you to enter all the necessary information required to run the bot, such as yout downloads directory, and the messages you want the bot to say when entering and leaving the chat.

After this is done, the config.txt file will be generated in the setup/ directory, and you should be good to go.

### Configuring chat name/URL
The default behavior for the bot is configured for personal purposes; therefore, it is harcoded to use a group chat that starts with "ORIGATO". These values can be changed via the DESTINATION_URL in 'web/message_with_media_send_logger.py', and by changing the directory manipulation functions in 'web/json_download_logger.py'
