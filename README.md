# ROSS - Remote Onion Site Script

![ross_logo](/_assets/ross_logo.jpg)

**ROSS** is a tool intended to make a GET request against any .onion and clearweb address.

This script allows you to make a GET request against an .onion URL.
It retrieves the HTML source code to being analyzed later.

## Usage

Just type (as superuser):

```bash
$ python ross.py
$ python ross.py https://metalerk.github.io --retry 5 --serve
```

and a prompt will ask for the URL.

## Tests

Run tests:

```bash
python -m unittest discover -s tests
```


## Examples

### 200 OK

![ross_cli](/_assets/ross_cli_correct.gif)

### 404 Not Found

![ross_cli](/_assets/ross_cli_error.gif)

### Webserver

![ross_cli](/_assets/ross_webserver.gif)

## Configuration

You can use [this guide](https://sinfallas.wordpress.com/2014/06/16/tor-polipo-privoxy/) to configure Tor + Polipo + Privoxy.
