#difficulty 4/10
#previous info in json.dictionary
from pathlib import Path
import json

#read back using json.loads
path = Path ('dictionary.json')
contents = path.read_text()
info = json.loads(contents)

#print summary showing exactly what my program remembers about the user
print (info)