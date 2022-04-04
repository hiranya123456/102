import dropbox
import cv2
import time
import random

start_time=time.time()

def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time = time.time
        result = False
    return img_name   
    print("Snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()


def upload_file(img_name):
    access_token = "sl.BFHE1Xp7E3GoUdGeYyr27a6ROk0yjbTrFkRDWul6Odg1mlHTm9GfgaZt9WoWOcLM6U3zODlb9dk_fNNATPP3JNKz3OirG636f5-H6juxfSQeZvjovUbSR01FoVbXezFlb26ldRU7dc0s"
    file =img_name
    file_from = file
    file_to="/myimages/"+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("pic uploaded")


def main():
    while(True):
        if ((time.time() - start_time) >= 10):
            name = take_snapshot()
            upload_file(name)

main()
