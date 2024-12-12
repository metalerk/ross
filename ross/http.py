from typing import Dict

import time
import sys

import click
import requests

from .exceptions import RossHTTPNot200
from .logger import get_logger


LOGGER = get_logger("http")

PROXIES = {
    "http": "127.0.0.1:8118",
    "https": "127.0.0.1:8118",
}


def make_request_progress_bar(
    url: str,
    proxies: Dict[str, str] = PROXIES,
    retry: int = 1,
    use_proxies: bool = True,
):

    fill_char = click.style("#", fg="yellow")
    empty_char = click.style("-", fg="white", dim=True)
    label_text = click.style(
        f"[*] Performing requests [Retries {retry}]...", fg="white"
    )

    with click.progressbar(
        iterable=range(retry),
        label=label_text,
        fill_char=fill_char,
        empty_char=empty_char,
    ) as items:
        for _ in items:
            res = requests.get(url, proxies=proxies if use_proxies else {})
            if res.status_code == 200:
                items.update(100)
                return res
            # let's not DDoS the server
            time.sleep(0.05)
        LOGGER.critical(f"Site: {url}")
        LOGGER.critical(f"Response status: {res.status_code}")
        sys.exit(0)


def make_request(
    url: str,
    proxies: Dict[str, str] = PROXIES,
    retry: int = 1,
    use_proxies: bool = True,
):
    res = None

    for _ in range(retry):
        res = requests.get(url, proxies=proxies if use_proxies else {})

        if res.status_code == 200:
            return res

    raise RossHTTPNot200(f"Response {res.status_code} after {retry} retries.")


def webserver(address, data):
    try:
        host, port = address.split(":")
    except Exception as e:
        print("[-] {}".format(e))
        sys.exit(-1)

    from flask import Flask
    from flask import render_template_string

    app = Flask(__name__)

    @app.route("/")
    def server():
        return render_template_string(data)

    app.run(host=host, port=port)
