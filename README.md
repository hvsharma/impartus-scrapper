# Impartus Scraper

This is a scraper for the Impartus Lectures system.

This is taken from https://github.com/iamkroot/ilc-scraper . All credits to that guy! 

**Pre-Run steps! - Do all of this before running:**
1. Ensure you have [Python 3.7+](https://www.python.org/downloads/) or higher installed, and available in your system `PATH`. To check, run `python --version` from command line/terminal.
2. Install `ffmpeg` from [here](http://ffmpeg.org/download.html). Ensure it is in your PATH variable. To check, run `ffmpeg -version` from command line/terminal.
3. Install [poetry]: `pip install --user poetry`.
4. Clone this repo and extract it to some location.
5. Go to downloaded/clone directory and open terminal.
6. Run `poetry install --no-dev -E gui` for the default installation.

## Configuration
1. imp_config.json is your credential file. Replace the username and password with your own.

	 imp_config.json:

```
		{
				"creds": {
						"username": "20XXhcxxxxx@wilp.bits-pilani.ac.in",
						"password": "xxxxxxxxxx"
				}
		}
```

2. 'imp_lect_list_all.json' is your course_url file. Update the list according to the lectures you want to download. To find the URLs,
	 login to impartus in browser and check the address bar for each course.

```
		{
			"section1-math": "http://a.impartus.com/ilc/#/course/220183/706",
			"section2-math": "http://a.impartus.com/ilc/#/course/220184/706",
			"section3-math": "http://a.impartus.com/ilc/#/course/220185/706",
			"section4-math": "http://a.impartus.com/ilc/#/course/220186/706",
			"section5-math": "http://a.impartus.com/ilc/#/course/220187/706",

			"section1-coss": "http://a.impartus.com/ilc/#/course/220173/706",
			"section2-coss": "http://a.impartus.com/ilc/#/course/220174/706",
			"section3-coss": "http://a.impartus.com/ilc/#/course/220175/706",
			"section4-coss": "http://a.impartus.com/ilc/#/course/220176/706",
			"section5-coss": "http://a.impartus.com/ilc/#/course/220177/706",

			"section1-dm": "http://a.impartus.com/ilc/#/course/220168/706",
			"section2-dm": "http://a.impartus.com/ilc/#/course/220169/706",
			"section3-dm": "http://a.impartus.com/ilc/#/course/220170/706",
			"section4-dm": "http://a.impartus.com/ilc/#/course/220171/706",
			"section5-dm": "http://a.impartus.com/ilc/#/course/220172/706",

			"section1-ds": "http://a.impartus.com/ilc/#/course/220178/706",
			"section2-ds": "http://a.impartus.com/ilc/#/course/220179/706",
			"section3-ds": "http://a.impartus.com/ilc/#/course/220180/706",
			"section4-ds": "http://a.impartus.com/ilc/#/course/220181/706",
			"section5-ds": "http://a.impartus.com/ilc/#/course/220182/706",

			
			"coss-webinars": "http://a.impartus.com/ilc/#/course/206942/706",
			"ds-webinars": "http://a.impartus.com/ilc/#/course/206943/706"
		}
		
```

3. Open 'sync_videos.py' and replace the paths if required for the config files and path to download videos:

```
	with open("D:\\impartus-scrapper\\imp_lect_list_all.json", 'r') as file_obj:
    course_urls = json.load(file_obj)

	
	with open("D:\\impartus-scrapper\\imp_config.json", 'r') as file_obj:
    credentials = json.load(file_obj)

	
	download_dir = "D:\\Lectures"


	command = f"python D:\\impartus-scrapper\\ilc_scrape.py -u {username} -p {password} -o -a both -q 720p " \
              f"-d {download_dir} -w 2 -c {url} --ignore-gooey"

```

## Running

* Run following command, sit back and relax:

```
	python sync_videos.py

```