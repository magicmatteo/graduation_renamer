import os, sys, shutil
from datetime import datetime


### STATIC VARIABLES:
current_year = datetime.now().year
newdir = './renamed_photos/'
### ------------------- ###

def help_check():
	# Check for --help as arguement and display help text
	try:
		if sys.argv[1].lower() == '--help':
			print(
	'''
	Ensure program is being run in root dir of photos. It will seach for 2017, 2018, 2019
	folders etc. It will then put renamed photos into ./renamed_photos folder
	'''		)
			sys.exit()
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

def main_func():
	# Main function that does the work. Renames all the files and puts them in folders
	folders = folder_names(current_year)
	for i in folders:
		folder = str(i)
		if os.path.exists(folder):
			for subdir, dirs, files in os.walk(folder):
				for file in files:
					if file.lower() == '.ds_store':
						continue
					if not os.path.exists(newdir):
						os.mkdir(newdir)
					new_name = rename_file(file, folder)
					sourcefile = os.path.realpath(os.path.join(folder,file))
					shutil.copy(sourcefile, (newdir + new_name))
					print(file + " renamed to " + new_name)

def main():
	help_check()
	main_func()

main()