import os
os.chdir(r'C:\Users\xtrem\Desktop\coding\electric-packages\packages')
for package in os.listdir():
    print(package)
    if package.endswith('.json'):
        os.system(f'au update {package}')
    os.system('git add .')
    os.system(f'git commit -m "Updated {package} to Latest Version"')

os.system('git add .')
os.system('git commit -m "Updated Packages"')
os.system('git push -u origin master')
