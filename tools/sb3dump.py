import sys
import json
import zipfile
from rich import print


project_file = zipfile.ZipFile(sys.argv[1])
project_json = json.loads(project_file.read("project.json"))


blocks = project_json["targets"][1]

print(blocks)
