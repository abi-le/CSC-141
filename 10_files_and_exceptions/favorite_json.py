#difficulty 3/10
from pathlib import Path
import json
#prompt the user for their favorite number
favorite_number = input ("Please enter favorite number:")
favorite = favorite_number

path = Path('favorite.json')
contents = json.dumps(favorite)
path.write_text(contents)