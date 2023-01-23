import os 
import shutil 
to_dir =" C:/Users/Krish/Desktop/C102_assets-main"
from_dir = 'C:/Users/Krish/Desktop/100'

list_of_files =os.listdir(from_dir)
print(list_of_files)



for file_ in list_:
	name, ext = os.path.splitext(file_)

	ext = ext[1:]

	if ext == '':
		continue

	# This will move the file to the directory
	# where the name 'ext' already exists
	if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+file_, path+'/'+ext+'/'+file_)

	# This will create a new directory,
	# if the directory does not already exist
	else:
		os.makedirs(path+'/'+ext)
		shutil.move(path+'/'+file_, path+'/'+ext+'/'+file_)
