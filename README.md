# mitreattackbot

Mitreattackbot is a bot that searches the Mitre attack database and outputs the result in your slack chat!

We use MitreAttack: https://github.com/MalwareSoup/MitreAttack

# 	INSTALLING THE APP: 

First you have to create your Slack APP. If you are new to slack i suggest following this neat tutorial: https://www.fullstackpython.com/blog/build-first-slack-bot-python.html

After you created your app and your bot, be sure to name the bot mitreattackbot for ease of use!
If you decide for any other name, to use your bot you have to type @[YOUR BOT NAME] [tech|soft|group|searchtech] [OPTION] [NAME]

Now, if you plan on running this on a server, skip the virtualenv part. If you are running it locally, follow these steps:

# VirtualEnv:

On a shell, type:
```sh
$ virtualenv mitreattackbot
$ source mitreattackbot/bin/activate
```
To create your isolated python environment. Its better this way.

# Running the bot:

Export your bot authentication code: 
```sh
$ export SLACK_BOT_TOKEN=[YOUR BOT AUTHENTICATION CODE HERE]
```

Now to install the slack client and run your bot!

```sh
$ pip install slackclient

$ python mitreattackbot.py
```

If you want to run while checking if the process is still up and restarting it if it crashes tun the script:

```sh
$ ./start.sh 
```

To check if your bot is running, it should be in the slack workspace like this:
![](/MitreAttack/mitrebotrunning.png)

If something went wrong, and the bot is offline it will show as:
![](/MitreAttack/mitrebotnotrunning.png)

# Usage:
- In any channel the bot is on, type:
@mitreattackbot [tech|soft|group|searchtech] [OPTION] [NAME]

For example:
![](/MitreAttack/usageexample.png)

# tech: Search for a technique in Mitre's database.
- OPTION: 
	-groups: Show groups that use the technique. EX: tech groups powershell
	
	-id: Shows the technique ID. EX: tech id powershell
	
	-title: Shows the technique title. EX: tech title input capture
	
	-desc: Shows the technique technical description. EX: tech desc input capture
	
	-url: Shows the technique's URL. EX: tech url email collection
	
	-sources: Shows the data sources for the technique. EX: tech sources powershell
	
	-tactics: Shows  the technique's tactics. EX: tech tactics software packing
	
	-soft: Shows software related to the technique. EX: tech soft powershell
	
	-all: Shows every technique in the database. EX: tech all
	
	-No option: Searches for techniques with NAME in the name. Returns a list if more than one technique contains NAME or shows every detail from a Technique if it returns only one. EX: tech shell
	

# soft: Search for a software in Mitre's database.
- OPTION: 
	-groups: Show groups that use the software. EX: soft groups mivast
	
	-id: Shows the software ID. EX: soft id mivast
	
	-title: Shows the software title. EX: soft title mivast
	
	-desc: Shows the software description. EX: soft desc mivast
	
	-url: Shows the software's URL. EX: soft url sykipot
	
	-aliases: Shows the aliases for the software. EX: soft aliases sykipot
	
	-tech: Shows  the software's techniques. EX: soft tech sykipot
	
	-all: Shows every software in the database. EX: soft all
	
	-No option: Searches for softwares with NAME in the name. Returns a list if more than one software contains NAME or shows every detail from a software if it returns only one. EX: soft flipside
	
# group: Search for a group in Mitre's database.
- OPTION: 
	-soft: Show softwares that the group uses. EX: group soft taidoor
	
	-id: Shows the group's ID. EX: group id taidoor
	
	-title: Shows the group's title. EX: group title taidoor
	
	-desc: Shows the group's description. EX: group desc taidoor
	
	-url: Shows the group's URL. EX: group url taidoor
	
	-aliases: Shows the aliases for the group. EX: group aliases taidoor
	
	-tech: Shows  the group's techniques. EX: group tech taidoor
	
	-all: Shows every group in the database. EX: group all
	
	-No option: Searches for groups with NAME in the name. Returns a list if more than one group contains NAME or shows every detail from a group if it returns only one. EX: group taidoor
	
	
# searchtech: Searches for a technique with the given parameters and fields. So far it only accepts th fiels "data" e "tactics"
- USO: @mitreattackbot searchtech [FIELD] [PARAMETER] [FIELD] [PARAMETER] ... [FIELD] [PARAMETER]

	EX: searchtech data registry tactics execution
