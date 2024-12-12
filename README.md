# ROSS - Remote Onion Site Script

![ross_logo](https://user-images.githubusercontent.com/13503868/73587150-8e773800-447d-11ea-8848-fdde0842e946.png)

ROSS is a tool intended to make a GET request against any .onion and clearweb address.

This script allows you to make a GET request against an .onion URL.
It retrieves the HTML source code to being analyzed later.

## Usage

Just type (as superuser):

```bash
$ python ross.py
$ python ross.py https://metalerk.github.io --retry 5 --serve
```

and a prompt will ask for the URL.

# Examples

## 200 OK

![ross_cli](/_assets/ross_cli_correct.gif)

## 404 Not Found

![ross_cli](/_assets/ross_cli_error.gif)

## Webserver

![ross_cli](/_assets/ross_webserver.gif)

## Configuration

You can use [this guide](https://sinfallas.wordpress.com/2014/06/16/tor-polipo-privoxy/) to configure Tor + Polipo + Privoxy.
