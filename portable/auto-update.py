
import os
os.chdir(r'C:\Users\xtrem\Desktop\Electric\Electric Packages\portable')
for package in os.listdir(r'C:\Users\xtrem\Desktop\Electric\Electric Packages\portable'):
    os.system(f'au update {package}')
