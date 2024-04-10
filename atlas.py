import json
import random

# Opens the file and loads the json

f = open("atlas.json", "r")
content = json.loads(f.read())
f.close()


country_list = []
probes_per_country = {}
random_ids = []

for object in content["objects"]:
	if object["country_code"] not in country_list:
		country_list.append(object["country_code"])
		
for country in country_list:
	probes_per_country[country] = []


for probe in content["objects"]:
	if probe["is_public"] is True:
		if 'system-ipv6-works' in probe["tags"]:
			if 'system-ipv4-works' in probe["tags"]:
				probes_per_country[probe['country_code']].append(probe["id"])

for country in country_list:
	if len(probes_per_country[country]) != 0:
		for i in range(10):
			random_ids.append(random.choice(probes_per_country[country]))

random_ids = set(random_ids)
print(*random_ids, sep = ",")
