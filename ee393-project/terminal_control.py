import os

os.system("cd Desktop")
def takePhoto():
    os.system("raspistill -o photo.jpg -t 250")
