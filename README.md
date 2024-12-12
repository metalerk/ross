# ROSS - Remote Onion Site Script

![ross_logo](/_assets/ross_logo.jpg)

**ROSS** is a tool intended to make a GET request against any .onion and clearweb address.

This script allows you to make a GET request against an .onion URL.
It retrieves the HTML source code to being analyzed later.
For scraping the Tor network, Polipo and Tor proxies must be set beforehand.

## Polipo + Tor Configuration

You can use [this guide](https://sinfallas.wordpress.com/2014/06/16/tor-polipo-privoxy/) to configure Tor + Polipo + Privoxy.

## Usage

Just type:

```bash
# help menu
$ python ross.py -h

# set 5 retries
$ python ross.py https://metalerk.github.io --retry 5 --serve

# start local webserver (images with relative paths are not shown)
$ python ross.py https://metalerk.github.io --serve
```

## Tests

Run tests:

```bash
python -m unittest discover -s tests
```

## Examples

### **Help Menu**

```bash
Usage: ross.py [OPTIONS] URL

Options:
  --retry INTEGER  Number of retries.
  --serve          Start webserver.
  --port INTEGER   Local webserver port.
  --use-proxies    Start webserver.
  --save BOOLEAN   Save to file.
  -h, --help       Show this message and exit.
```

### 200 OK Response

![ross_cli](/_assets/ross_cli_correct.gif)

### 404 Not Found Response

![ross_cli](/_assets/ross_cli_error.gif)

### Start Webserver

![ross_cli](/_assets/ross_webserver.gif)
