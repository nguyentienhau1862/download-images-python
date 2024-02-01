from os import path, makedirs
from json import loads
from lib import download_image, get_urls_from_page

def download_comic(comic = { "name": "", "url": "" }, comics_dir = ""):
	if comic["name"] and comic["url"]:
		comic_dir = path.join(comics_dir, comic["name"])

		if not path.isdir(comic_dir):
			makedirs(comic_dir)

		css_selector = "img.max-w-full.mx-auto"
		image_urls = get_urls_from_page(comic["url"], css_selector, "src")

		for image_url in image_urls:
			image_path = path.join(comic_dir, image_url.split("/").pop())
			download_image(image_url, image_path)
			print(image_path)

		with open(path.join(comic_dir, comic["name"] + ".docx"), "a") as file:
			file.close()

def download_image_from_page(page_url = "", image_dir = ""):
	if page_url:
		css_selector = ".sidebar:has(a#png) a#png, .sidebar:not(.sidebar:has(a#png)) a#highres"
		image_urls = get_urls_from_page(page_url, css_selector, "href")

		for image_url in image_urls:
			old_name_splitted = image_url.split("/").pop().split("%20")
			image_path = path.join(image_dir, old_name_splitted[2] + " " + old_name_splitted[-1])
			download_image(image_url, image_path)
			print(image_path)

if __name__ == "__main__":
	# Download Comic
	comics_dir = "D:/Private"
	comics_data_path = "./comics.json"
	file = open(comics_data_path, "r")
	comics = loads(file.read())
	file.close()

	download_comic(comics[0], comics_dir)

	# Download Images
	image_page_url_template = "https://konachan.com/post/show/"
	images_dir = "D:/Downloads"
	begin_index = 1
	end_index = 371300

	if not path.isdir(images_dir):
		makedirs(images_dir)

	for i in range(end_index - 99, end_index + 1):
		download_image_from_page(image_page_url_template + str(i), images_dir)
