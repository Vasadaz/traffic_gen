import webbrowser

import resource


def connect_ips(urls: list):
    for url in urls:
        webbrowser.open(url, new=0, autoraise=True)


def start():
    connect_ips(resource.get_ssh_ips())


if __name__ == '__main__':
    start()
