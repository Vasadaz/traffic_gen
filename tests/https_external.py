import webbrowser

import resource


def open_urls(urls: list):
    for url in urls:
        webbrowser.open(url, new=0, autoraise=True)


def start():
    open_urls(resource.get_https_external_urls())


if __name__ == '__main__':
    start()
