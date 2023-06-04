# json file

import json

def tab_padding(level):
    tab_pad = ''
    for i in range(level):
        tab_pad = tab_pad + '\t'
    return tab_pad

def print_end_dev(level, device):
    padding = tab_padding(level)
    print("{}{} {} {}".format(padding, device['dev'], device['part'], device['addr']))

def search_switch_type(level, device):
    padding = tab_padding(level)
    keys = device.keys()
    for k in keys:
        if k.startswith('ch'):
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
            search_switch_type(level, device)

# open json file
f = open('file.json')

# returns json object as a dictionary
data = json.load(f)

# At bus, level 0
level = 0
print_all_dev_in_list(level, data['KEY'])        

# close file
f.close()
