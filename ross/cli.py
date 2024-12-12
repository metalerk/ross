import click

from pprint import pformat

from .http import (
    webserver,
    make_request_progress_bar,
)
from .logger import get_logger
from .utils import write_file


LOGGER = get_logger("main")


def run_cli(
    url: str, save: bool, serve: bool, port: int, use_proxies: bool, retry: int
):
    LOGGER.info("Scraper started...")
    response = make_request_progress_bar(url=url, use_proxies=use_proxies, retry=retry)
    data = response.text
    if save:
        filename = input("Introduce file name [press enter for default]: ")
        if filename == "":
            filename = "output.ross"
        write_file(filename=filename, data=data)
    else:
        if input(click.style("\nShow data[y/n]: ", fg="bright_green")).lower() == "y":
            LOGGER.debug("Data: \n%s", pformat(data))

    if serve:
        webserver(f"127.0.0.1:{port}", data)


CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option("--retry", default=10, type=int, help="Number of retries.")
@click.option("--serve", is_flag=True, type=bool, help="Start webserver.")
@click.option("--port", default=6060, type=int, help="Local webserver port.")
@click.option("--use-proxies", is_flag=True, type=bool, help="Use Polipo + Tor proxies.")
@click.option("--save", default=False, type=bool, help="Save to file.")
@click.argument("url")
def start(retry: int, serve: str, port: int, save: str, url: str, use_proxies: bool):
    try:
        run_cli(
            url=url,
            save=save,
            serve=serve,
            port=port,
            use_proxies=use_proxies,
            retry=retry,
        )
    except Exception as e:
        LOGGER.critical(e)
