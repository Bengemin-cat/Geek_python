import os
import shutil

my_project = r'C:\Users\vlad\Desktop\Python\Vladimir_Vyalkov\Geek_Python\Lesson_7\dz_2\my_project'

for root,dir,file in os.walk(my_project):
    print(dir)

