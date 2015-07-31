import yaml
import json

my_list = range(5)
my_list.append({})
my_list[-1]['element1'] = 'one'
my_list[-1]['element2'] = 2
my_list.append({})
my_list[-1]['ip_addr'] = '192.168.75.1'
my_list[-1]['hostname'] = 'me'


print my_list

#Write yaml
with open("my_file.yml","w") as f:
	f.write(yaml.dump(my_list, default_flow_style=False))

#Write json
with open("my_file.json","w") as g:
	json.dump(my_list,g)


