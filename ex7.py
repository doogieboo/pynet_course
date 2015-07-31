import yaml
import json

my_yaml = "my_file.yml"
my_json = "my_file.json"

with open(my_json) as f:
	json_list = json.load(f)

with open(my_yaml) as f:
	yaml_list = yaml.load(f)

print "json list: " 
print json_list

print "yaml list: " 
print yaml_list


