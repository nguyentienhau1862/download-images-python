from bs4 import BeautifulSoup
from urllib import request, error

def write_log(data):
	logs_data_path = "./logs.txt"

	with open(logs_data_path, "a") as file:
		file.write(f"{data}\n")
		file.close()

def download_image(image_url = "", image_path = ""):
	try:
		opener = request.URLopener()
		opener.addheader("User-Agent", "Mozilla/5.0")
		opener.retrieve(image_url, image_path)
		opener.close()
	except error.HTTPError as err:
		write_log(f"Error When Downloading Image - {image_path} - {err.code} - {err.reason}")

def get_urls_from_page(page_url = "", css_selector = "", attribute = ""):
	urls = []

	try:
		page_request = request.Request(url=page_url, headers={"User-Agent": "Mozilla/5.0"})
		response = request.urlopen(page_request)
		tags = BeautifulSoup(response.read(), "html.parser").select(css_selector)
		response.close()
		for tag in tags:
			urls.append(tag.attrs.get(attribute))
	except error.HTTPError as err:
		write_log(f"Error When Going To Page - {page_url} - {err.code} - {err.reason}")

	return urls
