import requests
import hashlib
import json

def send_notification(page):
	print("{} changed".format(page))

def main():
	
	try:
		with open("page_list.txt") as f:
			pages = [line.strip() for line in f.readlines()]
	except FileNotFoundError as e:
		print("page_list.txt file not found")
		exit(1)

	try:
		with open("wm_cache", "r") as f:
			data = f.read()
		saved = json.loads(data)
	except (FileNotFoundError, json.decoder.JSONDecodeError) as e:
		saved = dict()

	for page in pages:
		r = requests.get(page)

		if r.status_code == 200:
			content = ''.join([i for i in r.text if not i.isdigit()])
			m = hashlib.sha256()
			m.update(content.encode())
			page_hash = m.hexdigest()

			if page in saved:
				if saved[page] != page_hash:
					send_notification(page)

			saved[page] = page_hash

	with open("wm_cache", "w") as f:
		json.dump(saved, f)


if __name__ == "__main__":
	main()
