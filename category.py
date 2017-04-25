import json

f = open("business_info_cache_clean.txt")
data = json.loads(f.read())

categories = {}

for res in data:
	try:
		for cat in data[res]['businesses'][0]['categories']:
			if cat[0] not in categories:
				categories[cat[0]] = 0
			categories[cat[0]]+= 1
	except:
		continue

# print len(categories)
for cat in sorted(categories, key = lambda x: categories[x], reverse = True)[:10]:
	print cat,  categories[cat]