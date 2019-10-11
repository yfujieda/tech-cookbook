# import json library
import json

# load a dummy json file from sample.json
json_file = open('sample.json').read()

# convert the json_file to json (dict) which was originally string
d = json.loads(json_file)

# print the value of title in glossary > GlossDiv > title
print d['glossary']['GlossDiv']['title']

for i in d['glossary']['GlossDiv']['GlossList']['GlossEntry']:
    # list down all the available entities under 
    # ['glossary']['GlossDiv']['GlossList']['GlossEntry']
    print i