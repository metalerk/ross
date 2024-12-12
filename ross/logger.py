import enum
import logging
import sys

import click


class FormatterColors(enum.Enum):
    YELLOW = "yellow"
    RED = "red"
    BLUE = "blue"
    WHITE = "white"
    GREEN = "green"
    MAGENTA = "magenta"
    BRIGHT_RED = "bright_red"
    BRIGHT_YELLOW = "bright_yellow"
    BRIGHT_BLUE = "bright_blue"
    BRIGHT_WHITE = "bright_white"
    BRIGHT_GREEN = "bright_green"
    BRIGHT_MAGENTA = "bright_magenta"


class RossFormatter(logging.Formatter):

    format: str = (
        "\n%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"
    )

    FORMATS = {
        logging.DEBUG: click.style(format, fg=FormatterColors.BRIGHT_WHITE.value),
        logging.INFO: click.style(format, fg=FormatterColors.WHITE.value),
        logging.WARNING: click.style(format, fg=FormatterColors.YELLOW.value),
        logging.ERROR: click.style(format, fg=FormatterColors.RED.value),
        logging.CRITICAL: click.style(format, fg=FormatterColors.RED.value),
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def get_logger(namespace: str = "ROSS", formatter=RossFormatter()):
    logger_handler = logging.getLogger(namespace)
    logger_handler.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger_handler.addHandler(console_handler)

    return logger_handler
