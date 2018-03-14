# mitreattackbot

Mitreattackbot is a bot that searches the Mitre attack database and outputs the result in your slack chat!

We use MitreAttack: https://github.com/MalwareSoup/MitreAttack

# 	INSTALLING THE APP: 

First you have to create your Slack APP. If you are new to slack I suggest following this neat tutorial: https://www.fullstackpython.com/blog/build-first-slack-bot-python.html

After you created your app and your bot, be sure to name the bot mitreattackbot for ease of use!
If you decide for any other name, to use your bot you have to type @[YOUR BOT NAME] [tech|soft|group|searchtech] [OPTION] [NAME]

You can add any icon to the bot! But we suggest gladius.png included in this repo!

Then run:
```sh
$ pip install -r requirements.txt
```

To install the dependencies

Now, if you plan on running this on a server, skip the virtualenv part. If you are running it locally, follow these steps:

## VirtualEnv:

On a shell, type:
```sh
$ virtualenv mitreattackbot
$ source mitreattackbot/bin/activate
```

To create your isolated python environment. Its better this way.

PS: When running locally there is a chance the connection to slack will drop. If this is the case on your side, you may want to make a little script to check if the code is running or not. Something like:

```sh
$ while true; do
$	pgrep -f "python mitreattackbot.py" > /dev/null || python mitreattackbot.py
$ done
```

## Running the bot:

Export your bot authentication token: 
```sh
$ export SLACK_BOT_TOKEN=[YOUR BOT AUTHENTICATION TOKEN HERE]
```

Now, if you didnt install slackclient run 
```sh
$ pip install -r requirements.txt
```

 and run your bot!

```sh
$ python mitreattackbot.py
```

If you want to edit the script to auto-export your slack bot authentication token, edit start.sh and run it like this:

```sh
$ ./start.sh 
```

To check if your bot is running, it should be in the slack workspace like this:

![](/MitreAttack/mitrebotrunning.png)

If something went wrong, and the bot is offline it will show as:

![](/MitreAttack/mitrebotnotrunning.png)

# USAGE:
- In any channel the bot is on, type:
@mitreattackbot [tech|soft|group|searchtech] [OPTION] [NAME]

For example:
![](/MitreAttack/usageexample.png)

## tech: Search for a technique in Mitre's database.
- OPTION: 
	-groups: Show groups that use the technique. e.g.: tech groups powershell
	
	-id: Shows the technique ID. e.g.: tech id powershell
	
	-title: Shows the technique title. e.g.: tech title input capture
	
	-desc: Shows the technique technical description. e.g.: tech desc input capture
	
	-url: Shows the technique's URL. e.g.: tech url email collection
	
	-sources: Shows the data sources for the technique. e.g.: tech sources powershell
	
	-tactics: Shows  the technique's tactics. e.g.: tech tactics software packing
	
	-soft: Shows software related to the technique. e.g.: tech soft powershell
	
	-all: Shows every technique in the database. e.g.: tech all
	
	-No option: Searches for techniques with NAME in the name. Returns a list if more than one technique contains NAME or shows every detail from a Technique if it returns only one. e.g.: tech shell
	

## soft: Search for a software in Mitre's database.
- OPTION: 
	-groups: Show groups that use the software. e.g.: soft groups mivast
	
	-id: Shows the software ID. e.g.: soft id mivast
	
	-title: Shows the software title. e.g.: soft title mivast
	
	-desc: Shows the software description. e.g.: soft desc mivast
	
	-url: Shows the software's URL. e.g.: soft url sykipot
	
	-aliases: Shows the aliases for the software. e.g.: soft aliases sykipot
	
	-tech: Shows  the software's techniques. e.g.: soft tech sykipot
	
	-all: Shows every software in the database. e.g.: soft all
	
	-No option: Searches for softwares with NAME in the name. Returns a list if more than one software contains NAME or shows every detail from a software if it returns only one. e.g.: soft flipside
	
## group: Search for a group in Mitre's database.
- OPTION: 
	-soft: Show softwares that the group uses. e.g.: group soft taidoor
	
	-id: Shows the group's ID. e.g.: group id taidoor
	
	-title: Shows the group's title. e.g.: group title taidoor
	
	-desc: Shows the group's description. e.g.: group desc taidoor
	
	-url: Shows the group's URL. e.g.: group url taidoor
	
	-aliases: Shows the aliases for the group. e.g.: group aliases taidoor
	
	-tech: Shows  the group's techniques. e.g.: group tech taidoor
	
	-all: Shows every group in the database. e.g.: group all
	
	-No option: Searches for groups with NAME in the name. Returns a list if more than one group contains NAME or shows every detail from a group if it returns only one. e.g.: group taidoor
	
	
## searchtech: Searches for a technique with the given parameters and fields. So far it only accepts th fiels "data" e "tactics"
- USO: @mitreattackbot searchtech [FIELD] [PARAMETER] [FIELD] [PARAMETER] ... [FIELD] [PARAMETER]

	e.g.: searchtech data registry tactics execution
