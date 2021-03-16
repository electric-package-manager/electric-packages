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

# RUN PACKAGE TESTS
# for pkg in packages:
#     ec1 = os.system(f'electric install {pkg}')
#     ec2 = os.system(f'electric uninstall {pkg}')
#     if ec1 and ec2 == 0:
#         print(f'Passed Test : {pkg} Installation And Uninstallation')
