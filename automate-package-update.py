import os

for file in os.listdir('packages'):
    if file.endswith('.json'):
        pid = os.system(f'au update packages/{file}')

        if pid != 0:
            print(f'Failed to update: {file}')
        else:
            print(f'Successfully updated: {file}')
            name = file.replace('.json', '')
            os.system(f'git commit -am "Automated update: {name}"')
