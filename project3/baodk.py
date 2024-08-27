from os import listdir, path, mkdir
from shutil import move

def file_category(file_name):
	"""
	function returns category name of file extension which extracted from file name
	"""
	nameParts = file_name.lower().split('.')
	if len(nameParts)<2:
		raise Exception("file name has no extension!")
	typeDict = {\
		"audio files": ["3gpp","3gpp2","aac","ac3","aptx","asc", "dvi4","eac3","flac","flexfec","fwdred","matroska","mhas","mp3","mpa","mpeg","ogg","opus","rtploopback","rtx","scip","sofa","speex","t140c","t38", "tone","ulpfec","usac"],
		"compressed files": ["7z","bz2","cab","deb","dmg","gz","rar","tar","xz","zip"],
		"documents": ["docx","pptx","ppt","pps","show","odp","pot","otp","xlsb","xlsx","xls","ods","ots","tsv","tab","gsheet","odt","rtf","doc", "csv", "json", "xml", "html", "css", "js","markdown", "md", "pdf", "dif", "eps", "ai", "psd", "ico"],
		"images": ["aces","apng","avci","avcs","avif","bmp","cgm","dpx","emf","example","fits","g3fax","gif","heic","heif","hej2k","hsj2","ief","j2c","jls","jp2","jpg","jpeg","jph","jphc","jpm","jpx","jxl","ktx","ktx2","naplps","png","svg","svg+xml","t38","tiff","webp","wmf"],
		"emails": ["eml", "emlx", "msg", "msg"],
		"executable files": ["8bf","apk","exe","app","com","dll","ipa","iso","msi","o"],
		"fonts": ["abf", "bdf", "fnt", "otf", "pcf", "fond", "sfnt", "ttc", "ttf", "woff"],
		"link and shortcut": ["lnk", "url", "nal", "sym", "webloc"],
		"videos": ["3gp","aaf","avi","flv","m4v","mp4","wmv"]
		}
	for tName, tExts in typeDict.items():
		if nameParts[-1] in tExts:
			return tName
	return "uncategorized files"

def list_all_files(dir_path):
	"""
	function return list all files in directory
	"""
	listFiles = listdir(dir_path)
	return [{"filepath":f"{dir_path}/{f}", "filename": f, "category": file_category(f)} for f in listFiles if path.isfile(f"{dir_path}/{f}")]

def move_categorized_files(list_files, dir_path):
	categories = {}
	for fileInfo in list_files:
		cat = fileInfo.get("category")
		if isinstance(categories.get(cat), list):
			categories[cat].append(fileInfo)
		else:
			categories[cat] = [fileInfo]
		destinationPath = f"{dir_path}/{cat}"
		if not path.exists(destinationPath):
			mkdir(destinationPath)
		move(fileInfo.get('filepath'), destinationPath)
	return categories

def print_categories(categories):
	if len(list(categories.keys()))==0:
		print('We never sort any file in your folder.')
		return
	print('We sorted files with following categories:')
	for catName, catFiles in categories.items():
		print(f"'{catName}' contains:")
		print("\n".join(" {:02d}. '{:s}'".format(i+1,fi.get('filename')) for i, fi in enumerate(catFiles)))


def file_sorting():
	input_dir_path = input("Put the folder path you want to sort files inside: ").strip()	
	if not path.isdir(input_dir_path):
		print(f"[!]'{input_dir_path}' is not a folder!")
		return
	listCategorizedFiles = list_all_files(input_dir_path)
	try:
		categories = move_categorized_files(listCategorizedFiles, input_dir_path)
		print_categories(categories)
	except Exception as e:
		print(f"[!]{e}")

if __name__ == '__main__':
	file_sorting()

# Review:
# Good job on completing this project, you nailed it, here are some points you can consider to improve your code:
'''
Consider using os.path.join() for constructing file paths, which handles different path separators across operating systems. This will make the code more portable.
Instead of listing all files and then filtering them, you could directly filter files using os.scandir() which might be more efficient, especially in directories with a large number of files.
'''