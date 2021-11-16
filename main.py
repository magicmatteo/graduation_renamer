import os, sys, shutil
from datetime import datetime


### STATIC VARIABLES:
current_year = datetime.now().year
newdir = './renamed_photos/'
last_first = False
### ------------------- ###

def arg_check():
	# Check for args
	try:
		if sys.argv[1].lower() == '--help':
			print(
	'''
	Ensure program is being run in root dir of photos. It will seach for 2017, 2018, 2019
	folders etc. It will then put renamed photos into ./renamed_photos folder
	'''		)
			sys.exit()
		
		if sys.argv[1].lower() == '--last-first':
			last_first = True

	except IndexError:
		pass

def folder_names(year_):
	# Create a list of applicable folder names to store the photos in
	result = []
	for i in range(7):
		result.append(year_ - i)
	return result

## Remove spaces from names ie. Luca De Felize -> luca_de_felize
def rename_file(fn, year_):
	intab = ' -'
	outtab = '__'
	fn = fn.rsplit('.')[0] + str(year_) + ".jpg"
	translation = fn.maketrans(intab, outtab)
	return fn.translate(translation)

def clean(fn):
	intab = ' -'
	outtab = '__'
	translation = fn.maketrans(intab, outtab)
	return fn.translate(translation).lower()

def swap_first_last(fn):
	'''
	Swaps first and last names in file name. Used to do an extended match on filenames
	in the classes_database. Arthur Reed is not consistent on naming conventions over
	the years. We need to make provisions for first_last or last_first naming conventions.
	'''
	try:
		file_ext 		= fn.rsplit('.')[1]
		first_block 	= fn.rsplit('.')[0].rsplit('_')[1]
		second_block 	= fn.rsplit('.')[0].rsplit('_')[0]
		fn 				= first_block + '_' + second_block + '.' + file_ext
		return fn
	except IndexError:
		pass

def class_database():
	# Create a dict of which kids need to be in which class
	classes = {}
	if os.path.exists(str(current_year)):
		for subdir, dirs, files in os.walk(str(current_year)):
			for folder in dirs:
				class_ = folder
				for subdir, dirs, file_ in os.walk(str(current_year) + '/' + folder):
					classes[class_] = [clean(x) for x in file_]
	else: raise SystemError((f'Folder {current_year} not found. This is the current year' +\
		 ' and is needed to build class database.'))
	return classes

def main_func():
	# Main function that does the work. Renames all the files and puts them in folders
	cldb = class_database()
	folders = folder_names(current_year)
	for i in folders:
		folder = str(i)
		if os.path.exists(folder):
			for subdir, dirs, files in os.walk(folder):
				fileyear = folder
				for file in files:
					class_ = 'failures-move-manually' 	# Default folder for renamed files
														# Will be placed here without class match
					dfile = file 
					file = clean(file)
					if file == '.ds_store':
						continue
					# Search student class (dict) for class
					for item in cldb:
						if file in cldb[item]:
							class_ = str(item)
						elif swap_first_last(file) in cldb[item]:
							class_ = str(item)
							file = swap_first_last(file)
					
					# Create folder structure if it doesnt exist
					if not os.path.exists(newdir):
						os.mkdir(newdir)
					if not os.path.exists(newdir + class_):
						os.mkdir(newdir + class_)
					
					if last_first == True:
						file = swap_first_last(file)
					new_name = rename_file(file, fileyear)
					sourcefile = os.path.realpath(os.path.join(subdir ,dfile))
					shutil.copy(sourcefile, (newdir + f'/{class_}/' + new_name))
					print(dfile, 'from', folder, 'renamed to', new_name)

def main():
	arg_check()
	main_func()

if __name__ == "__main__":
	main()