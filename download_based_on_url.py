import requests


def download_file(url: str):
    r = requests.get(url)
    filename = url.split("/")[-1]

    with open(filename, "wb") as f:
        f.write(r.content)


with open("urls_to_download_from.txt") as txt:
    urls = txt.read().splitlines()
    for url in urls:
        download_file(url)
