import requests
from bs4 import BeautifulSoup
import shutil
import argparse

# Code to add the cli
parser = argparse.ArgumentParser()
parser.add_argument("-l", "--issue", required=True, help="Comics Issue Number")
args = vars(parser.parse_args())

# Complete url for the issue
url = f"https://xkcd.com/{args['issue']}"

response = requests.get(url)

# Checking if we can fetch the url or not
if response.status_code != 200:
    print("Issue number is invalid")
    exit()
soup = BeautifulSoup(response.content, 'html.parser')
image_link = soup.find_all('img')[2]['src']
image_name = image_link.split('/')[-1]
image_url = "https:" + image_link
r = requests.get(image_url, stream=True)
if r.status_code == 200:
    # This ensures the image file is loaded correctly
    r.raw.decode_content = True

    # Creating the image file
    with open(image_name, 'wb') as f:
        shutil.copyfileobj(r.raw, f)

    print('Image successfully Downloaded: ', image_name)
else:
    print("Image Couldn't be retrieved")
