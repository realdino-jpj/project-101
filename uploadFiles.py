from threading import local
import time
import random
import os
import dropbox

class TransferData :
    def __init__(self,access_token) :
        self.access_token = access_token
    
    def upload_file(self,file_from,file_to):
        
        if (os.path.exists(file_to)):
            ddx = dropbox.Dropbox(self.access_token)
            f = open(file_from,"rb")
            ddx.files_upload(f.read(),file_to)
            for root, dirs, files in os.walk(file_to):
                for name in files:
                    print(os.path.join(root, name))
                for name in dirs:
                    print(os.path.join(root, name))

def main():
    access_token = ""
    transferData = TransferData(access_token)
    file_from = input("enter the file path to transfer")
    file_to = input("enter the full path to upload to dropbox")
    transferData.upload_file(file_from,file_to)
    print("file has moved")

main()
          
