import sys
import requests
import click
from ross import Ross


def write_file(filename, data, v=False):
    try:
        with open(filename, 'w') as f:
            f.write(data)
        if v: print('[+] Created {}.'.format(filename))
        return True
    except Exception as e:
        if v: print('[-] {}.'.format(e))
        return False

def webserver(address, data):
    try:
        host, port = address.split(':')
    except Exception as e:
        print('[-] {}'.format(e))
        sys.exit(-1)

    from flask import Flask
    from flask import render_template_string

    app = Flask(__name__)
    @app.route('/')
    def server():
        return render_template_string(data)
        
    app.run(host=host, port=port)

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('--listen', default='localhost:5000', type=str, help="Start webserver.")
@click.option('--verbose', '-v', is_flag=True, help="Verbose mode.")
@click.option('--save', type=str, help="Save to file.")
@click.argument('url')
def main(listen, save, url, verbose):
    ross = Ross(url)
    ross.make_request()
    response = ross.get_response()
    if save:
        write_file(save, response, v=True)
    if verbose: click.echo()
    if listen: webserver(listen, response)

if __name__ == "__main__":
    main()
