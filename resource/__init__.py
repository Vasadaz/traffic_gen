def _get_lines(file_name: str) -> list[str]:
    with open('resource/data/' + file_name, 'r') as file:
        urls = []
        for url in file.readlines():
            urls.append(url.strip())

    return urls


def get_ftp_urls() -> list[str]:
    return _get_lines('ftp.txt')


def get_http_urls() -> list[str]:
    return _get_lines('http.txt')


def get_http_blocked_urls() -> list[str]:
    return _get_lines('http_blocked.txt')


def get_https_external_urls() -> list[str]:
    return _get_lines('https_external.txt')


def get_https_ru_urls() -> list[str]:
    return _get_lines('https_ru.txt')


def get_ssh_ips() -> list[str]:
    return _get_lines('https_ru.txt')


def get_telnet_ips() -> list[str]:
    return _get_lines('https_ru.txt')
