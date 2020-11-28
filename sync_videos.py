import subprocess
import shlex
import json


with open("D:\\impartus-scrapper\\imp_lect_list_all.json", 'r') as file_obj:
    course_urls = json.load(file_obj)

with open("D:\\impartus-scrapper\\imp_config.json", 'r') as file_obj:
    credentials = json.load(file_obj)

username = credentials['creds']['username']
password = credentials['creds']['password']
download_dir = "D:\\Lectures"

for name, url in course_urls.items():
    print(f"Downloading {str(name).upper()}")
    command = f"python D:\\\impartus-scrapper\\\ilc_scrape.py -u {username} -p {password} -o -a both -q 720p " \
              f"-d {download_dir} -w 2 -c {url} --ignore-gooey"
    print(command)
    command = shlex.split(command)
    subprocess.run(command)
