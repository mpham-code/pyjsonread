# json file

import json
import getopt, sys

def tab_padding(level):
    tab_pad = ''
    for i in range(level):
        tab_pad = tab_pad + '\t'
    return tab_pad

def print_end_dev(level, device):
    padding = tab_padding(level)
    print("{}{} {} {}".format(padding, device['dev'], device['part'], device['addr']))

def search_switch_dev(level, device):
    padding = tab_padding(level)
    keys = sorted(device)
    for k in keys:
        if k.startswith('CH'):
            print("{}{} {} {} Channel {}".format(padding, device['dev'], device['part'], device['addr'], k))
            print_all_dev_in_list(level + 1, device[k])

def print_all_dev_in_list(level, list):
    # iterating through the json list
    for device in list:
        # print each element in list 'data'
        # print(i)

        # if end device, print
        if (device['type'] == 'end'):
            print_end_dev(level, device)

        # if switch device, go deeper
        if (device['type'] == 'switch'):
            search_switch_dev(level, device)

# global var
input_file = ''

# Remove 1st argument from the
# list of command line arguments
argumentList = sys.argv[1:]

# Options
options = "hi:"

# Long options
long_options = ["help", "input="]

try:
    # Parsing argument
    arguments, values = getopt.getopt(argumentList, options, long_options)
     
    # checking each argument
    for currentArgument, currentValue in arguments:
 
        if currentArgument in ("-h", "--help"):
            print ("Displaying Help")
             
        elif currentArgument in ("-i", "--input"):
            input_file = currentValue
            print ("Displaying file_name: {}".format(input_file))
         
except getopt.error as err:
    # output error, and return with an error code
    print (str(err))

# open json file
f = open(input_file)

# returns json object as a dictionary
data = json.load(f)

# print all busses
# get all keys and sort them
keys = sorted(data)
for k in keys:
    print(k)
    # At bus, level 1
    level = 1
    print_all_dev_in_list(level, data[k])

# close file
f.close()
