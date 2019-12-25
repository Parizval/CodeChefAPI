import glob,os
import requests
from mdutils.mdutils import MdUtils

mdFile = MdUtils(file_name='README',title='Markdown File Example')
mdFile.new_header(level=3,title="Problems Solved")

directory = "."
os.chdir(directory)
files = [file for file in glob.glob("*.py")]
print(files)
count = 0 
errors = []
for i in files:
    link = "https://www.codechef.com/problems/{}".format(i.strip(".py"))
    request = requests.get(link)
    if request.status_code == 200:
        print("- [{}](https://www.codechef.com/problems/{})\n".format(i.strip(".py"),i.strip(".py")))
        mdFile.write("- [{}](https://www.codechef.com/problems/{})\n\n".format(i.strip(".py"),i.strip(".py")))

    else: 
        count += 1
        errors.append(i) 
print("Error Count {}".format(count))
print(errors)

mdFile.create_md_file()
print("Code Executed")