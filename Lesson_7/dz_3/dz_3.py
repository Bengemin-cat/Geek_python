import os
import shutil

project_name = 'my_project'

for root, dirs, files in os.walk(project_name):
    if 'templates' in dirs and root != project_name:
        for entry in os.listdir(os.path.join(root, 'templates')):
            shutil.copytree(os.path.join(root, 'templates', entry), os.path.join(os.getcwd(), 'templates', entry))

