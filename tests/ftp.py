import webbrowser

import resource


def download_files(urls: list):
    for url in urls:
        print(url)


def start():
    download_files(resource.get_ftp_urls())


if __name__ == '__main__':
    start()
