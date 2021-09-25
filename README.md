# Instaloader

A simple, lightweight Python 3 command line application to download private Instagram videos. Supports posts with single and multiple videos.

## Usage

```bash
python3 instaloader.py -u <url> -s <session id> -p <output folder> -o <output filename>
```

To download a private video a valid session ID cookie value of a user that follows the private account must be supplied using the `-s` or `--sessionid` flag. The only required arguments are the URL and the session ID. The output folder defaults to the current user's downloads folder and the filename defaults to the original filename of the video.

## Requirements

This program is largely built using built-in modules. The only third party module used is the [requests](https://pypi.org/project/requests/) module which is used for conveniently handling the authentication needed for accessing the private post.
