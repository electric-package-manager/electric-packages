import json
import os

os.chdir(r'C:\Users\xtrem\Desktop\electric\Electric Packages\packages')
packages = [ f.replace('.json', '') for f in os.listdir(r'C:\Users\xtrem\Desktop\electric\Electric Packages\packages') ]
print(packages)
data = {
    'packages': packages,
}

with open(r'C:\Users\xtrem\Desktop\electric\Electric Packages\package-list.json', 'w+') as f:
    f.write(json.dumps(data, indent=4))
os.system('powershell.exe deploy "Update Package List"')
