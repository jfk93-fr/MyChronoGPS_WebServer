#!/usr/bin/env python3
# coding: utf8

import http.server

import os, sys

port = 8080
ip = ''
adresseserveur = (ip, port)
serveur = http.server.HTTPServer 
gestionnaire = http.server.CGIHTTPRequestHandler
gestionnaire.cgi_directories = ["/ajax"]

def main():
    try:
        httpd = serveur(adresseserveur, gestionnaire)
        print("Démarrage du serveur CGI: http://{}:{}".format(
            ip, port)
        )
        httpd.serve_forever()
    except FileNotFoundError as e:
        sys.stderr.write("ERREUR! Le fichier n'existe pas!\n")
        raise e
    except KeyboardInterrupt:
        httpd.socket.close()


if __name__ == '__main__':
    main()
