from os import path, makedirs
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

if __name__ == "__main__":
	comics_dir = "D:/Private"

	download_comic({
		"name": "Fuck Buddies With My Girlfriend's Mom Chapter 1 - Maimu Maimu",
		"url": "https://lxmanga.net/truyen/fuck-buddies-with-my-girlfriend-s-mom/chapter-1"
	}, comics_dir)
