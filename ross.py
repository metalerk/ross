#################################################################
###                                                           ###
###          ROSS: Request Onion Site Script                  ###
###                                                           ###
###    ROSS es una micro herramienta destinada a ejecutar     ###
###    una peticion GET contra una direccion .onion aunque    ###
###    tambien funciona contra direcciones de la clear web.   ###
###                                                           ###
###    Para que funcione correctamente deberas tener en       ###
###    funcionamiento privoxy + polipo + tor.                 ###
###                                                           ###
###    En el caso de que tengas otra configuracion personal   ###
###    de tus proxies o algun puerto diferente solo edita     ###
###    los valores del diccionario de proxies.                ###
###                                                           ###
###                                                           ###
###    Puedes usar, distribuir, modificar y extender esta     ###
###    herramienta siempre que respetes mi autoria.           ###
###                                                           ###
###    Coded by: Metalerk                                     ###
###                                                           ###
#################################################################

import sys
import requests
from colorama import Fore, init
from subprocess import call

# Proxies conectados a privoxy + polipo + Tor

proxies = {
    'http':'127.0.0.1:8118',
    'https':'127.0.0.1:8118'
}

#url = 'http://h5vz7zqlnkaq4ruz.onion'

clear = call("clear", shell=True)

init()

print("\n")
print("""
          ##################################################
         ###      ROSS: Request Onion Site Script       ###
        ###                                            ###
       ###             Coded by: Metalerk             ###
      ##################################################
""")

url = input(Fore.YELLOW + "\t[+] Introduce la url: " + Fore.RESET)

if url:
    if not url.startswith("http"): url = "http://" + url
    print(Fore.YELLOW + "\t[+] Ejecutando request a: %s\n" %(url))
    r = requests.get(url, proxies=proxies)
    print("\t[+] Listo.\n")
    print("\t[+] Datos: \n\n" + Fore.RESET)
    print(Fore.WHITE + r.text.strip('\n').strip('\t') + Fore.RESET)
    print("\n")
else:
    print(url and noturl.startswith("http"))
    sys.exit(1)
