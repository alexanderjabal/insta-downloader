import os
import urllib
from urllib.request import urlretrieve
import requests
import argparse

def download(url, sessionid, output, filename=""):
	cookies = {"sessionid": sessionid}

	video_urls = []
	r = requests.get(url, cookies=cookies)
	for line in r.text.splitlines(): 
		
		if "video_url" in line: # Find the line with "video_url" strings
			for item in line.split(","): # Split line into list for indexing video urls
				if item.startswith('"video_url":'): # Loop through all items and find all video urls
					video_urls.append(item.replace('"video_url":"', '').replace("\\", "/").replace("/u0026", "&")) # Format urls

	end = url.find(".mp4") + 4
	if len(video_urls) > 1: # More than 1 video in post
		download_choice = int(input(f"Which video do you want to download? (1-{len(video_urls)}): " ))
		url = video_urls[download_choice - 1]
		end = url.find(".mp4") + 4
		if not filename:
			urlretrieve(video_urls[download_choice - 1], args.path + url[55:end]) # No filename specified, use default filename

		else:
			urlretrieve(video_urls[download_choice - 1], args.path + filename) # Save video to specified filename

	else:
		url = video_urls[0]
		end = url.find(".mp4") + 4

		if not filename:
			urlretrieve(url, args.path + url[55:end]) # No filename specified, use default filename

		else:
			urlretrieve(url, args.path + filename) # Save video to specified filename


	# pprint(video_urls)
	print(f"\nSuccesfully saved to {output}")

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Instagram video downloader")
	parser.add_argument("-u", "--url", type=str, help="URL of the post you want to download. Usage: -u|--url <url>")
	parser.add_argument("-s", "--sessionid", type=str, help="Current session ID. Usage: -s|--sessionid <id>")
	parser.add_argument("-p", "--path", type=str, help="Path of folder to output to, optional. Defaults to downloads folder. Usage: -p|--path <filepath>")
	parser.add_argument("-o", "--output", type=str, help="File to output to, optional. Defaults to original filename. Usage: -o <filename>.mp4")

	args = parser.parse_args()
	if not args.url:
		print("\nURL is required, pass URL with -u|--url <url>")
		exit()

	elif not args.sessionid:
		print("\nSession ID is required, pass session ID with -s|--sessionid <id>")
		exit()

	if not args.path:
		args.path = os.getenv("USERPROFILE") + "\\Downloads\\"

	if not args.path[-1] == "\\":
		args.path += "\\"



	download(args.url, args.sessionid, args.path, args.output)