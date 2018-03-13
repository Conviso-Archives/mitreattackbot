# -*- coding: utf-8 -*-
import os
import time
import re
from slackclient import SlackClient
from MitreAttack import Attack
att = Attack()

# instantiate Slack client
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
# starterbot's user ID in Slack: value is assigned after the bot starts up
starterbot_id = None

# constants
RTM_READ_DELAY = 1 # 1 second delay between reading from RTM
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"

def parse_bot_commands(slack_events):
	"""
		Parses a list of events coming from the Slack RTM API to find bot commands.
		If a bot command is found, this function returns a tuple of command and channel.
		f its not found, then this function returns None, None.
	"""
	for event in slack_events:
		if event["type"] == "message" and not "subtype" in event:
			user_id, message = parse_direct_mention(event["text"])
			if user_id == starterbot_id:
				return message, event["channel"]
	return None, None

def parse_direct_mention(message_text):
	"""
		Finds a direct mention (a mention that is at the beginning) in message text
		and returns the user ID which was mentioned. If there is no direct mention, returns None
	"""
	matches = re.search(MENTION_REGEX, message_text)
	# the first group contains the username, the second group contains the remaining message
	return (matches.group(1), matches.group(2).strip()) if matches else (None, None)

def handle_command(command, channel):
	"""
		Executes bot command if the command is known
	"""
	# Default response is help text for the user
	#default_response = "Not sure what you mean. Try *{}*.".format(EXAMPLE_COMMAND)
	default_response = "I could not understand your command, i think you may have given me too few parameters or maybe you typed something wrong. Try again using: [tech|soft|group|searchtech] [Option] [Name]"
	# Finds and executes the given command, filling in response
	response = None
	
	cmd_list = str(command.encode('ascii', 'replace')).split()

	if cmd_list[0] == 'help':
		response = "To use me, type in channel i am currently on:\n@mitreattackbot [tech|group|soft|searchtech] [OPTION] [NAME]\n For example: tech desc powershell\n Typing this will make me show you the technical description of the PowerShell technique!"

	if cmd_list[0] == 'searchtech':
		pre_return_str = None
		if len(cmd_list) > 1:
			if len(cmd_list)%2 == 1:
				cmd_list.remove("searchtech")
				search_list = []
				for i in range(0, len(cmd_list), 2):
					search_list.append({'field': cmd_list[i], 'value': cmd_list[i+1]})
				response = str(att.search(search_list))
			else:
				response = "To use the searchtech option i must have a field and a value, if you dont tell me a field and a value i cannnot search things for you. Try searchtech [FIELD] [VALUE]"
			
	if cmd_list[0] == 'tech':
		pre_return_str = None
		if len(cmd_list) > 1:
			if cmd_list[1] == 'groups':
				if len(cmd_list) > 2:
					cmd_list.remove("tech")
					cmd_list.remove("groups")
					search_str = str(" ".join(cmd_list))
					data_returned = att.findTechnique(search_str)
					if type(data_returned) is list:
						pre_return_str = None
						default_response = "Your request returned more than one technique and i dont know from which you want the data of. Please be more specific. If you need, find out the full name of the technique by typing \"tech NAME\" and redo the question using the full name please."
					else:
						pre_return_str = str(data_returned.groups)
			elif cmd_list[1] == 'id':
				if len(cmd_list) > 2:
					cmd_list.remove("tech")
					cmd_list.remove("id")
					search_str = str(" ".join(cmd_list))
					data_returned = att.findTechnique(search_str)
					if type(data_returned) is list:
						pre_return_str = None
						default_response = "Your request returned more than one technique and i dont know from which you want the data of. Please be more specific. If you need, find out the full name of the technique by typing \"tech NAME\" and redo the question using the full name please."
					else:
						pre_return_str = str(data_returned.ID)
			elif cmd_list[1] == 'title':
				if len(cmd_list) > 2:
					cmd_list.remove("tech")
					cmd_list.remove("title")
					search_str = str(" ".join(cmd_list))
					data_returned = att.findTechnique(search_str)
					if type(data_returned) is list:
						pre_return_str = None
						default_response = "Your request returned more than one technique and i dont know from which you want the data of. Please be more specific. If you need, find out the full name of the technique by typing \"tech NAME\" and redo the question using the full name please."
					else:
						pre_return_str = str(data_returned.displaytitle)
			elif cmd_list[1] == 'desc':
				if len(cmd_list) > 2:
					cmd_list.remove("tech")
					cmd_list.remove("desc")
					search_str = str(" ".join(cmd_list))
					data_returned = att.findTechnique(search_str)
					if type(data_returned) is list:
						pre_return_str = None
						default_response = "Your request returned more than one technique and i dont know from which you want the data of. Please be more specific. If you need, find out the full name of the technique by typing \"tech NAME\" and redo the question using the full name please."
					else:
						pre_return_str = str(data_returned.technical_description)
			elif cmd_list[1] == 'url':
				if len(cmd_list) > 2:
					cmd_list.remove("tech")
					cmd_list.remove("url")
					search_str = str(" ".join(cmd_list))
					data_returned = att.findTechnique(search_str)
					if type(data_returned) is list:
						pre_return_str = None
						default_response = "Your request returned more than one technique and i dont know from which you want the data of. Please be more specific. If you need, find out the full name of the technique by typing \"tech NAME\" and redo the question using the full name please."
					else:
						pre_return_str = str(data_returned.full_url)
			elif cmd_list[1] == 'sources':
				if len(cmd_list) > 2:
					cmd_list.remove("tech")
					cmd_list.remove("sources")
					search_str = str(" ".join(cmd_list))
					data_returned = att.findTechnique(search_str)
					if type(data_returned) is list:
						pre_return_str = None
						default_response = "Your request returned more than one technique and i dont know from which you want the data of. Please be more specific. If you need, find out the full name of the technique by typing \"tech NAME\" and redo the question using the full name please."
					else:
						pre_return_str = str(data_returned.data_sources)
			elif cmd_list[1] == 'tactics':
				if len(cmd_list) > 2:
					cmd_list.remove("tech")
					cmd_list.remove("tactics")
					search_str = str(" ".join(cmd_list))
					data_returned = att.findTechnique(search_str)
					if type(data_returned) is list:
						pre_return_str = None
						default_response = "Your request returned more than one technique and i dont know from which you want the data of. Please be more specific. If you need, find out the full name of the technique by typing \"tech NAME\" and redo the question using the full name please."
					else:
						pre_return_str = str(data_returned.tactics)
			elif cmd_list[1] == 'soft':
				if len(cmd_list) > 2:
					cmd_list.remove("tech")
					cmd_list.remove("soft")
					search_str = str(" ".join(cmd_list))
					data_returned = att.findTechnique(search_str)
					if type(data_returned) is list:
						pre_return_str = None
						default_response = "Your request returned more than one technique and i dont know from which you want the data of. Please be more specific. If you need, find out the full name of the technique by typing \"tech NAME\" and redo the question using the full name please."
					else:
						pre_return_str = str(data_returned.software)
			elif cmd_list[1] == 'all':
				pre_return_str = str(att.findTechnique(''))
			else:
				cmd_list.remove("tech")
				search_str = str(" ".join(cmd_list))
				data_returned = att.findTechnique(search_str)
				if type(data_returned) is list:
					pre_return_str = str(data_returned)
				else:
					pre_return_str = str(data_returned) + "\n\nID: " + str(data_returned.ID) + "\n\nTitle:" + str(data_returned.displaytitle) + "\n\nTechnical Description: " + str(data_returned.technical_description) + "\n\nURL: " + str(data_returned.full_url) + "\n\nGroups: " + str(data_returned.groups).replace("u'", "") + "\n\nSoftware: " + str(data_returned.software).replace("u'", "") + "\n\nTactics: " + str(data_returned.tactics).replace("u'", "") + "\n\nData Source: " + str(data_returned.data_sources).replace("u'", "") + "\n"
			response = pre_return_str

	if cmd_list[0] == 'group':
		pre_return_str = None
		if len(cmd_list) > 1:
			if cmd_list[1] == 'techniques':
				if len(cmd_list) > 2:
					cmd_list.remove("group")
					cmd_list.remove("techniques")
					search_str = str(" ".join(cmd_list))
					data_returned = att.findGroup(search_str)
					if type(data_returned) is list:
						pre_return_str = None
						default_response = "Your request returned more than one group and i dont know from which you want the data of. Please be more specific. If you need, find out the full name of the group by typing \"group NAME\" and redo the question using the full name please."
					else:
						pre_return_str = str(data_returned.techniques)
			elif cmd_list[1] == 'id':
				if len(cmd_list) > 2:
					cmd_list.remove("group")
					cmd_list.remove("id")
					search_str = str(" ".join(cmd_list))
					data_returned = att.findGroup(search_str)
					if type(data_returned) is list:
						pre_return_str = None
						default_response = "Your request returned more than one group and i dont know from which you want the data of. Please be more specific. If you need, find out the full name of the group by typing \"group NAME\" and redo the question using the full name please."
					else:
						pre_return_str = str(data_returned.ID)
			elif cmd_list[1] == 'title':
				if len(cmd_list) > 2:
					cmd_list.remove("group")
					cmd_list.remove("title")
					search_str = str(" ".join(cmd_list))
					data_returned = att.findGroup(search_str)
					if type(data_returned) is list:
						pre_return_str = None
						default_response = "Your request returned more than one group and i dont know from which you want the data of. Please be more specific. If you need, find out the full name of the group by typing \"group NAME\" and redo the question using the full name please."
					else:
						pre_return_str = str(data_returned.displaytitle)
			elif cmd_list[1] == 'desc':
				if len(cmd_list) > 2:
					cmd_list.remove("group")
					cmd_list.remove("desc")
					search_str = str(" ".join(cmd_list))
					data_returned = att.findGroup(search_str)
					if type(data_returned) is list:
						pre_return_str = None
						default_response = "Your request returned more than one group and i dont know from which you want the data of. Please be more specific. If you need, find out the full name of the group by typing \"group NAME\" and redo the question using the full name please."
					else:
						pre_return_str = str(data_returned.description)
			elif cmd_list[1] == 'url':
				if len(cmd_list) > 2:
					cmd_list.remove("group")
					cmd_list.remove("url")
					search_str = str(" ".join(cmd_list))
					data_returned = att.findGroup(search_str)
					if type(data_returned) is list:
						pre_return_str = None
						default_response = "Your request returned more than one group and i dont know from which you want the data of. Please be more specific. If you need, find out the full name of the group by typing \"group NAME\" and redo the question using the full name please."
					else:
						pre_return_str = str(data_returned.fullurl)
			elif cmd_list[1] == 'aliases':
				if len(cmd_list) > 2:
					cmd_list.remove("group")
					cmd_list.remove("aliases")
					search_str = str(" ".join(cmd_list))
					data_returned = att.findGroup(search_str)
					if type(data_returned) is list:
						pre_return_str = None
						default_response = "Your request returned more than one group and i dont know from which you want the data of. Please be more specific. If you need, find out the full name of the group by typing \"group NAME\" and redo the question using the full name please."
					else:
						pre_return_str = str(data_returned.aliases)
			elif cmd_list[1] == 'soft':
				if len(cmd_list) > 2:
					cmd_list.remove("group")
					cmd_list.remove("soft")
					search_str = str(" ".join(cmd_list))
					data_returned = att.findGroup(search_str)
					if type(data_returned) is list:
						pre_return_str = None
						default_response = "Your request returned more than one group and i dont know from which you want the data of. Please be more specific. If you need, find out the full name of the group by typing \"group NAME\" and redo the question using the full name please."
					else:
						pre_return_str = str(data_returned.software)
			elif cmd_list[1] == 'all':
				pre_return_str = str(att.findGroup(''))
			else:
				cmd_list.remove("group")
				search_str = str(" ".join(cmd_list))
				data_returned = att.findGroup(search_str)
				if type(data_returned) is list:
					pre_return_str = str(data_returned)
				else:
					pre_return_str = str(data_returned) + "\n\nID: " + str(data_returned.ID) + "\n\nTitle:" + str(data_returned.displaytitle) + "\n\nTechnical Description: " + str(data_returned.description) + "\n\nURL: " + str(data_returned.fullurl) + "\n\nTechniques: " + str(data_returned.techniques).replace("u'", "") + "\n\nSoftware: " + str(data_returned.software).replace("u'", "") + "\n\nAliases: " + str(data_returned.aliases).replace("u'", "") + "\n"
			response = pre_return_str
			
	if cmd_list[0] == 'soft':
		pre_return_str = None
		if len(cmd_list) > 1:
			if cmd_list[1] == 'techniques':
				if len(cmd_list) > 2:
					cmd_list.remove("soft")
					cmd_list.remove("techniques")
					search_str = str(" ".join(cmd_list))
					data_returned = att.findSoftware(search_str)
					if type(data_returned) is list:
						pre_return_str = None
						default_response = "Your request returned more than one software and i dont know from which you want the data of. Please be more specific. If you need, find out the full name of the software by typing \"soft NAME\" and redo the question using the full name please."
					else:
						pre_return_str = str(data_returned.techniques)
			elif cmd_list[1] == 'id':
				if len(cmd_list) > 2:
					cmd_list.remove("soft")
					cmd_list.remove("id")
					search_str = str(" ".join(cmd_list))
					data_returned = att.findSoftware(search_str)
					if type(data_returned) is list:
						pre_return_str = None
						default_response = "Your request returned more than one software and i dont know from which you want the data of. Please be more specific. If you need, find out the full name of the software by typing \"soft NAME\" and redo the question using the full name please."
					else:
						pre_return_str = str(data_returned.ID)
			elif cmd_list[1] == 'title':
				if len(cmd_list) > 2:
					cmd_list.remove("soft")
					cmd_list.remove("title")
					search_str = str(" ".join(cmd_list))
					data_returned = att.findSoftware(search_str)
					if type(data_returned) is list:
						pre_return_str = None
						default_response = "Your request returned more than one software and i dont know from which you want the data of. Please be more specific. If you need, find out the full name of the software by typing \"soft NAME\" and redo the question using the full name please."
					else:
						pre_return_str = str(data_returned.displaytitle)
			elif cmd_list[1] == 'desc':
				if len(cmd_list) > 2:
					cmd_list.remove("soft")
					cmd_list.remove("desc")
					search_str = str(" ".join(cmd_list))
					data_returned = att.findSoftware(search_str)
					if type(data_returned) is list:
						pre_return_str = None
						default_response = "Your request returned more than one software and i dont know from which you want the data of. Please be more specific. If you need, find out the full name of the software by typing \"soft NAME\" and redo the question using the full name please."
					else:
						pre_return_str = str(data_returned.description)
			elif cmd_list[1] == 'url':
				if len(cmd_list) > 2:
					cmd_list.remove("soft")
					cmd_list.remove("url")
					search_str = str(" ".join(cmd_list))
					data_returned = att.findSoftware(search_str)
					if type(data_returned) is list:
						pre_return_str = None
						default_response = "Your request returned more than one software and i dont know from which you want the data of. Please be more specific. If you need, find out the full name of the software by typing \"soft NAME\" and redo the question using the full name please."
					else:
						pre_return_str = str(data_returned.fullurl)
			elif cmd_list[1] == 'aliases':
				if len(cmd_list) > 2:
					cmd_list.remove("soft")
					cmd_list.remove("aliases")
					search_str = str(" ".join(cmd_list))
					data_returned = att.findSoftware(search_str)
					if type(data_returned) is list:
						pre_return_str = None
						default_response = "Your request returned more than one software and i dont know from which you want the data of. Please be more specific. If you need, find out the full name of the software by typing \"soft NAME\" and redo the question using the full name please."
					else:
						pre_return_str = str(data_returned.aliases)
			elif cmd_list[1] == 'groups':
				if len(cmd_list) > 2:
					cmd_list.remove("soft")
					cmd_list.remove("groups")
					search_str = str(" ".join(cmd_list))
					data_returned = att.findSoftware(search_str)
					if type(data_returned) is list:
						pre_return_str = None
						default_response = "Your request returned more than one software and i dont know from which you want the data of. Please be more specific. If you need, find out the full name of the software by typing \"soft NAME\" and redo the question using the full name please."
					else:
						pre_return_str = str(data_returned.groups)
			elif cmd_list[1] == 'all':
				pre_return_str = str(att.findSoftware(''))
			else:
				cmd_list.remove("soft")
				search_str = str(" ".join(cmd_list))
				data_returned = att.findSoftware(search_str)
				if type(data_returned) is list:
					pre_return_str = str(data_returned)
				else:
					pre_return_str = str(data_returned) + "\n\nID: " + str(data_returned.ID) + "\n\nTitle:" + str(data_returned.displaytitle) + "\n\nTechnical Description: " + str(data_returned.description) + "\n\nURL: " + str(data_returned.fullurl) + "\n\nTechniques: " + str(data_returned.techniques).replace("u'", "") + "\n\nGroups: " + str(data_returned.groups).replace("u'", "") + "\n\nAliases: " + str(data_returned.aliases).replace("u'", "") + "\n"
			response = pre_return_str

	# Sends the response back to the channel
	slack_client.api_call(
		"chat.postMessage",
		channel=channel,
		text=response or default_response
	)


if __name__ == "__main__":
	if slack_client.rtm_connect(with_team_state=False):
		print("MitreAttackBot connected and running!")
		# Read bot's user ID by calling Web API method `auth.test`
		starterbot_id = slack_client.api_call("auth.test")["user_id"]
		while True:
			command, channel = parse_bot_commands(slack_client.rtm_read())
			if command:
				handle_command(command, channel)
			time.sleep(RTM_READ_DELAY)
	else:
		print("Connection failed. Exception traceback printed above.")

