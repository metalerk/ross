# ROSS

Remote Onion Site Script

![ross_logo](https://user-images.githubusercontent.com/13503868/73587150-8e773800-447d-11ea-8848-fdde0842e946.png)

ROSS is a tool intended to make a GET request against any .onion and clearweb address.

This script allows you to make a GET request against an .onion URL.
It retrieves the HTML source code to being analyzed later.

## Usage

Just type (as superuser):

```
$ chmod +x ross.py
./ross.py
./ross.py http://luisesteban.mx --listen localhost:5000 --save out.html --verbose
```

and a prompt will ask for the URL.

## Configuration

You can use [this guide](https://sinfallas.wordpress.com/2014/06/16/tor-polipo-privoxy/) to configure Tor + Polipo + Privoxy.
