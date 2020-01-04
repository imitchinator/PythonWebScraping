#!python3
#Mitchell Petras


import webbrowser, sys


if len(sys.argv) > 1:
    address = ''.join(sys.argv[1:])

webbrowser.open('https://google.com/maps/place/' + address)