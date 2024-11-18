import http.server
import socket
import socketserver
import webbrowser
import pyqrcode
from pyqrcode import QRCode
import png
import os

PORT = 8010
b_drive_path = "B:\\LFSA"
os.environ['B_DRIVE_PATH'] = b_drive_path

desktop = os.path.join(b_drive_path, 'LFSA')
# os.chdir(desktop)

try:
    os.chdir(desktop)
except FileNotFoundError:
    os.makedirs(desktop)
    os.chdir(desktop)

Handler = http.server.SimpleHTTPRequestHandler
hostname = socket.gethostname()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IP = "http://" + s.getsockname()[0] + ":" + str(PORT)
link = IP

url = pyqrcode.create(link)
url.svg("server-qr.svg", scale=8)
webbrowser.open('server-qr.svg')

with socketserver.TCPServer(("", PORT), Handler) as httpd:
	print("serving at port", PORT)
	print("Type this in your Browser", IP)
	print("or Use the QRCode")
	httpd.serve_forever()
