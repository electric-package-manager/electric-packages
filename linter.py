import os
import json

os.chdir(r'C:\Users\xtrem\Desktop\Electric\Electric Packages\packages')

for f in os.listdir():
    if f.endswith('.json'):
        with open(f, 'r') as file:
            data = json.loads(file.read())
    
    # Reconstruct the data
    new = {}

    new['display-name'] = data['display-name']
    new['package-name'] = data['package-name']

    
    version = ''
    if 'is-portable' not in list(data.keys()):
        new['latest-version'] = data['latest-version']

    elif 'is-portable' in list(data.keys()):
        if data['is-portable']:
            new['is-portable'] = True

    if 'auto-update' in list(data.keys()):
        new['auto-update'] = data['auto-update']

    if not 'is-portable' in list(new.keys()):
        new[new['latest-version']] = {}
    elif 'is-portable' in list(new.keys()):
        new['portable'] = {}
    
    if 'portable' in list(new.keys()):
        if 'auto-update' in list(data['portable'].keys()):
            new['portable']['auto-update'] = data['portable']['auto-update']

    version = new['latest-version'] if 'latest-version' in list(new.keys()) else 'portable'
    
    if 'latest-version' not in list(data[version].keys()):

        if 'portable' in list(data.keys()):
            new['portable'][new['portable']['latest-version']]['url'] = data['portable'][new['portable']['latest-version']]['url']

        if 'url' in list(data[version].keys()):
            new[version]['url'] = data[version]['url']

        if 'checksum' in list(data[version].keys()):
            new[version]['checksum'] = data[version]['checksum']

        if 'file-type' in list(data[version].keys()):
            new[version]['file-type'] = data[version]['file-type']
        
        if 'install-switches' in list(data[version].keys()):
            new[version]['install-switches'] = data[version]['install-switches']
        
        if 'uninstall-switches' in list(data[version].keys()):
            new[version]['uninstall-switches'] = data[version]['uninstall-switches']
        
        if 'custom-location' in list(data[version].keys()):
            new[version]['custom-location'] = data[version]['custom-location']
      
        if 'dependencies' in list(data[version].keys()):
            new[version]['dependencies'] = data[version]['dependencies']
    else:
        # Portable
        pass

    print(new)
