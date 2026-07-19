# script to make XOSS settings json
# interactive use or command line parameters to set each variable
# output is Setting.json or settings.json

# import modules
import argparse
import json
import re
import os
import datetime
from datetime import datetime
import time

# get arguments
def parse_args():
	parser = argparse.ArgumentParser(description="Configure XOSS GPS settings that are stored in settings.json file with command line parameters.")
	# name for input settings json file
	parser.add_argument("--input_settings_json",required=True,default="settings.json",help="Filename for original XOSS GPS settings JSON to configure.")
	# name for output settings json file
	parser.add_argument("--output_settings_json",required=True,default="settings.json",help="Filename for output edited XOSS GPS settings JSON.")
	# specify language as two letter string or pair of two letter strings; limit choices to those in documentation
	parser.add_argument("--language",choices=["en","it","ko","ja","de","es","fr","zh-cn","zh-hk","zh-tw","pt-pt","pt-br"],default="en",type=str,help="Default language for GPS based on i18n standard two-letter codes (e.g., \"en\" for English) documented at https://www.w3.org/International/O-charset-lang.html. Available choices based on XOSS developer documentation provided.")
	# include possible choices, default choices, and argument for following entries in settings
	parser.add_argument("--unit_type",choices=[0,1],default=0,type=int,help="(Distance) unit type - 0 for metric (e.g., km) or 1 for imperial (miles).")
	parser.add_argument("--temperature_unit",choices=[0,1],default=0,type=int,help="Temperature unit - 0 for Celsius or 1 for Fahrenheit.")
	parser.add_argument("--time_format",choices=[0,1],default=0,type=int,help="Time format - 0 for 24 hours or 1 for 12 hours.")
	parser.add_argument("--backlight",choices=[0,1,2],default=0,type=int,help="Backlight - 0 for auto, 1 for always on, or 2 for always off.")
	parser.add_argument("--pause",choices=[0,1],default=0,type=int,help="Pause GPS when not moving - 0 for auto or 1 for off.")
	parser.add_argument("--overwrite",choices=[0,1],default=0,type=int,help="Automatic overwrite when memory full - 0 for on or 1 for off.")
	# note that keytone has a boolean argument
	parser.add_argument("--keytone",choices=[True,False],default=True,type=bool,help="Keytone - 'true' for on or 'false' for off.")
	# return arguments
	return parser.parse_args()

if __name__ == "__main__":
	args = parse_args()
	# check that language code specified is no more than two letters
	# never mind, set choices in options above
	# load original settings.json
	print("Loading original settings JSON file.")
	with open(args.input_settings_json, "r") as file:
		input_settings_json_dict = json.load(file)
	# define json based on argument list
	# just make python dictionary
	output_settings_dict = {
		"language_i18n" : args.language,
		"unit" : args.unit_type,
		"temperature_unit" : args.temperature_unit,
		"time_formatter" : args.time_format,
		"backlight" : args.backlight,
		"logo_light" : args.backlight,
		"auto_pause" : args.pause,
		"overwrite" : args.overwrite,
		"keytone" : args.keytone
	}
	# add this to "settings" subdictionary of settings.json
	input_settings_json_dict['settings']=output_settings_dict
	# add timestamp of when json updated
	input_settings_json_dict['updated_at']=int(time.time())
	# save new settings json to specified output filename
	with open(args.output_settings_json, "w") as outfile:
		json.dump(input_settings_json_dict, outfile, indent=4)
	# print confirmation
	print("Saved updated settings json to",args.output_settings_json)
