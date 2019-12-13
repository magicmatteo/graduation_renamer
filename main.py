import os, sys, shutil, time

try:
	if sys.argv[1].lower() == '--help':
		print(
'''
Ensure program is being run in root dir of photos. It will seach for 2017, 2018, 2019
folders etc. 
'''		)
		sys.exit()
except IndexError:
	pass

## Get date and set applicable years for folder names
current_year = 2019#int(input("Please enter graduation year: "))

allowed_folder_names = []
for i in range(7):
	allowed_folder_names.append(current_year - i)

print(allowed_folder_names)

## Remove spaces from names ie. Luca De Felize -> luca_de_felize


## Rename Phase
newdir = './renamed_photos/'

for i in allowed_folder_names:
	folder = str(i)
	if os.path.exists(folder):
		for subdir, dirs, files in os.walk(folder):
			for file in files:
				if not os.path.exists(newdir):
					os.mkdir(newdir)
				new_name = file.rsplit('.')[0] + str(i) + "_.jpg"
				print(file + " renamed to " + new_name)
				sourcefile = os.path.realpath(os.path.join(folder,file))
				shutil.copy(sourcefile, (newdir + new_name))

