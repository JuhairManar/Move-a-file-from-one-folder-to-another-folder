""" processes

1.initialize the source path
2.get the source files with location
3.copy the source file to the server directory
 """
import glob
import shutil
import os

source_path='..\source\*'
destination_path='..\destination'

postfix_1=[1,2,3]

source_object=glob.glob(source_path) #file names with sources (,) for multiple files

object_path=source_object[0]

print(source_path) #..\source\*
print(source_object) #['..\\source\\some.txt']
shutil.copy(object_path,'.') #copying the file to this directory
print(source_object[0]) #..\source\some.txt
print(object_path) #..\source\some.txt
#object_name=object_path.split('\\')[-1] #split #some.txt
object_name=object_path.split('\\')[-1].split('.') #some txt
print(object_name) #some txt
print(type(object_name))
prefix=object_name[0] #some
postfix_2=object_name[1]
for i in range(3):
    filename=prefix+'_'+str(i+1)+'.'+postfix_2    #naming the files #some_1 string
    print(filename)
    #shutil.copy(object_path,filename)  #object path info in file 
    shutil.copy(object_path,f'{destination_path}\{filename}') 
"""     f = open(filename, 'r+')
    f.truncate(0) """ 

os.remove(object_path)   
os.remove(object_path.split('\\')[-1]) 