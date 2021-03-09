# ADMChatBot
## ADM-ChatBot McHacks21
A simple AI ChatBot built during McHacks21
ADM Team Members: Ayübuke E., David P., Magnus G.
Beta Site on AWS: http://3.23.186.95

# What it does
Based on the user input into the form, the AI chatbot tokenizes the sentence and find out what kind of message it is. Currently there are 8 categories of messages supported. Then the bot replies with a message from the tag with the highest probability.

## Special Thanks
Great thanks to Tech With Tim for his tutorial on the ChatBot
Back-end using Flask, AWS Configuration using Gunicorn and Nginx
Libraries used: `TFLearn`, `Tensorflow`, `Numpy`

# Building Process
  1. AI Model inspired by Tech With Tim
  2. Intents.json file expanded by the ADM team
  3. Back-end, using Flask, implemented by Magnus Gao
  4. Deployed on AWS (with `Nginx` and `Gunicorn` as interface) by Magnus Gao 

## Deployment Options
  1. The first option was Google Cloud. However, deploying on App Engine is more complicated than delploying using other platforms. Considering the complexity of the project, the team decided to use other platforms. (Special thanks to GCP and GCP engineers for supporting MLH!)
  2. The second option was PythonAnywhere. It allows 500MB of hard disk space, which wasn't enough to install our virtual environment.
  3. AWS EC2 was chosen at the end, since its console is similar to Mac's Terminal. 
 
## Known deployment problems
  1. Tensorflow 2.0.0b cannot automatically be installed via pip3 install -r requirements.txt. Solution: remove Tensorflow from requirements.txt, and install mannually using `pip3 install --no-cache-dirtensorflow` on the command line
 

## Side Note: Useful Commands
- `sudo service nginx restart` to restart nginx
- `sudo service gunicorn3 restart` to restart gunicorn3
- `/etc/nginx/sites-enabled` is some of the places where we need to change the Nginx configuration after receiving a new IP address
- .socks file from Gunicorn



# To Work On:
  1. Route AWS to the domain
  2. Make changes to CSS to improve UI/UX
