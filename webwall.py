from socket import *
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
import pyfiglet as fig
from colorama import init, Fore
import time
import argparse
import os
import json

# __COLOURS
init()
yellow = Fore.LIGHTYELLOW_EX
red = Fore.LIGHTRED_EX
green = Fore.LIGHTGREEN_EX
blue = Fore.LIGHTBLUE_EX
cyan = Fore.LIGHTCYAN_EX
pink = Fore.MAGENTA
reset = Fore.RESET

# __title
title = (fig.figlet_format(f"py-WALL", font='block'))
print(yellow + title[:] + reset)
print("  " * 20, f"~{cyan}*.*{red} SHY.BUG {cyan}*.*{reset}\n")

# __cmd-line arguments
argparse = argparse.ArgumentParser(description=blue + "python script to simulate web request firewall " + reset,
                                   usage=f"python3 {format(sys.argv[0])} -P or --port <{pink}port number{reset}>,"
                                         f"-r <{pink}request type POST|GET{reset}>, "
                                         f"--badkey <{pink} key to be filtered{reset}>, "
                                         f"--badvalue <{pink} value of key to be filtered{reset}"
                                         f"--keyfile <{pink} file containing bad keys tobe filtered {reset}>,"
                                         f"--badpath <{pink} path to be filtered{reset}>, "
                                         f"--error_code <{pink} error code{reset}>"
                                         f"--error_msg <{pink} error msg {reset}>")

argparse.add_argument("-P", "--port", help=green + "enter port no. after -P/--port for starting http server " + reset,
                      required=True)
argparse.add_argument("-r", "--request",
                      help=green + "enter the request type POST/GET after -r to filter out that request" + reset)
argparse.add_argument("--badkey",
                      help=green + "enter a bad key after --badkey to search and filter-out that request" + reset)
argparse.add_argument("--badvalue", help=green + "enter value of given key after --badvalue to be filtered")
argparse.add_argument("--badpath", help=green + "enter the bad request path after --badpath to be filtered out" + reset)
argparse.add_argument("--keyfile",
                      help=green + "enter the file name along with the path after --keyfile to filter keys present in that file" + reset)
argparse.add_argument("--error_code", help=green + "enter code 403/405/400 etc to be sent on filtered request" + reset,
                      required=True)
argparse.add_argument("--error_msg", help=green + "enter msg to be displayed on filtered request" + reset,
                      required=True)

args = argparse.parse_args()
port = int(args.port)
request = str(args.request)
badkey = str(args.badkey)
badvalue = str(args.badvalue)
keyfile = (args.keyfile)
badpath = str(args.badpath)
ecode = int(args.error_code)
emsg = str(args.error_msg)

#  defaults
host = 'localhost'
#print(f"request:{request},badkey:{badkey},badvalue:{badvalue},keyfile:{keyfile},badpath:{badpath},ecode:{ecode},emsg:{emsg}")

try:

    def request_blocker(self):
        print(f"{green}[+] blocking detected request{reset}")
        self.send_error(ecode, emsg)
        print(f"{green}[+] request blocked successfully.........\n\n{reset}")


    def keyfile_blocker(self):

        print(f"checking for key-value file.....")
        if os.path.isfile(keyfile):
            print(f"{green}[+] file {keyfile} found")
            with open(keyfile, 'r') as file:
                readfile = file.read()
                jsfile = json.loads(readfile)
                file_as_dict_keys = list(jsfile.keys())
                print(f"\n{blue}[+] malicious key filtering started....{reset}")
                for key in file_as_dict_keys:
                    print(f"checking for {red}{key}{reset}")
                    if key in self.headers and self.headers[key] == jsfile[key]:
                        print(f"{green}[+] malicious request detected{reset}")
                        print(f"malicious key:{key} found:{red}{jsfile[key]} \n")
                        return request_blocker(self)

                request_passer(self)
                
            try:
                file.close()
            except:
                pass

        else:
            print(f"{keyfile} does not exist")
            sys.exit()

    def path_blocker(self):

        if self.path == badpath:
            print(f"{green}[+] restiricted path access identified{reset}\n")
            return request_blocker(self)
        else:
            request_passer(self)

    def keyvalue_blocker(self):

        if badkey in self.headers and self.headers[badkey] == badvalue:
            print(f"{green}[+] malicious request detected with {red}{badkey}{reset}:{red}{badvalue}{reset}")
            return request_blocker(self)
        else:
            request_passer(self)



    def request_passer(self):
        self.send_response(200)
        self.send_header("content-type", "application/json")
        self.end_headers()



    def request_handler(self):
        if keyfile != None:
            return keyfile_blocker(self)

        elif badkey and badvalue != 'None':
            print(f"{green}[+] key-value filtering started.......{reset}")
            return keyvalue_blocker(self)

        elif badpath != 'None':
            print(f"{green}[+] path filtering started....{reset}")
            return path_blocker(self)






        # __default response
        self.send_response(200)
        self.send_header("content-type", "application/json")
        self.end_headers()


    class handler(BaseHTTPRequestHandler):
        def do_GET(self):
            if request == 'GET':
                request_blocker(self)
            else:
                request_handler(self)

        def do_POST(self):

            if request == 'POST':
                return request_blocker(self)
                pass


            else:
                request_handler(self)


    serverobj = HTTPServer((host, port), handler)
    print(f"{cyan}HTTP server started on port {port}{reset}")

    try:
        serverobj.serve_forever()

    except KeyboardInterrupt:
        serverobj.server_close()
        print(f"{red}[+] terminating the server..{reset}")
        exit(0)

except error :
	print(error)
    

