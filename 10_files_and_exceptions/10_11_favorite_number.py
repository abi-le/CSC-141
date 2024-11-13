#difficultly 4/10
#remembering the favorite number
from pathlib import Path
import json

path = Path ('favorite.json')
contents = path.read_text()
favorite = json.loads(contents)

print(f"I know your favorite number! It's {favorite}!")