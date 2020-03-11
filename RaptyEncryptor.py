#!/usr/bin/python
#-*-coding:utf-8 -*
from tkinter import *
from tkinter import filedialog
import os, webbrowser, shutil
import pyAesCrypt
"""
RatpyEncryptor is a program that allows encryption (and therefore protection) of files and folders using a password. 
It is compatible with all operating systems that include Python (with the Tkinter and Cryptography libraries installed)

For the prerequisites, refer to the README file.

Version 1.0

"""
######################################################################################################################################################################
########################################################################## GUI POP-UP FUNCTIONS DEFINITION ###########################################################
######################################################################################################################################################################
bufferSize = 64 * 1024
def howToWork():
    webbrowser.open('https://github.com/Guezone/RatpyEncryptor/', new=2)
def popUpBadType():
    BadTypePopUP = Tk()
    BadTypePopUP.geometry("450x100")
    # Gets the requested values of the height and widht.
    windowWidth = BadTypePopUP.winfo_reqwidth()
    windowHeight = BadTypePopUP.winfo_reqheight()
    # Gets both half the screen width/height and window width/height
    positionRight = int(BadTypePopUP.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(BadTypePopUP.winfo_screenheight()/2 - windowHeight/2)
    # Positions the window in the center of the page.
    BadTypePopUP.geometry("+{}+{}".format(positionRight, positionDown))

    BadTypePopUP.wm_title("Error")
    label = Label(BadTypePopUP, text="The file selected is not a enrypted directory."+"\n"+"Please select old directory with name directory.enc.")
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(BadTypePopUP, text="OK", command = BadTypePopUP.destroy)
    B1.pack()
    BadTypePopUP.mainloop()

def popUpFailedToDecrypt():
    failedPopUP = Tk()
    failedPopUP.geometry("600x100")
    # Gets the requested values of the height and widht.
    windowWidth = failedPopUP.winfo_reqwidth()
    windowHeight = failedPopUP.winfo_reqheight()
    # Gets both half the screen width/height and window width/height
    positionRight = int(failedPopUP.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(failedPopUP.winfo_screenheight()/2 - windowHeight/2)
    # Positions the window in the center of the page.
    failedPopUP.geometry("+{}+{}".format(positionRight, positionDown))

    failedPopUP.wm_title("Failed")
    label = Label(failedPopUP, text="The file was not decrypted because you have enter a bad password.")
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(failedPopUP, text="OK", command = failedPopUP.destroy)
    B1.pack()
    failedPopUP.mainloop()

def popUpSuccessToDecrypt():
    donePopUP = Tk()
    donePopUP.geometry("300x100")
    # Gets the requested values of the height and widht.
    windowWidth = donePopUP.winfo_reqwidth()
    windowHeight = donePopUP.winfo_reqheight()
    # Gets both half the screen width/height and window width/height
    positionRight = int(donePopUP.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(donePopUP.winfo_screenheight()/2 - windowHeight/2)
    # Positions the window in the center of the page.
    donePopUP.geometry("+{}+{}".format(positionRight, positionDown))

    donePopUP.wm_title("Done")
    label = Label(donePopUP, text="The file was successfuly decrypted.")
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(donePopUP, text="OK", command = donePopUP.destroy)
    B1.pack()
    donePopUP.mainloop()

def popUpSuccessToEncrypt():
    done2PopUP = Tk()
    done2PopUP.geometry("300x100")
    # Gets the requested values of the height and widht.
    windowWidth = done2PopUP.winfo_reqwidth()
    windowHeight = done2PopUP.winfo_reqheight()
    # Gets both half the screen width/height and window width/height
    positionRight = int(done2PopUP.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(done2PopUP.winfo_screenheight()/2 - windowHeight/2)
    # Positions the window in the center of the page.
    done2PopUP.geometry("+{}+{}".format(positionRight, positionDown))

    done2PopUP.wm_title("Done")
    label2 = Label(done2PopUP, text="The file was successfuly encrypted.")
    label2.pack(side="top", fill="x", pady=10)
    B2 = Button(done2PopUP, text="OK", command = done2PopUP.destroy)
    B2.pack()
    done2PopUP.mainloop()

def popUpWarning():
    warningPopUP = Tk()
    warningPopUP.geometry("500x100")
    # Gets the requested values of the height and widht.
    windowWidth = warningPopUP.winfo_reqwidth()
    windowHeight = warningPopUP.winfo_reqheight()
    # Gets both half the screen width/height and window width/height
    positionRight = int(warningPopUP.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(warningPopUP.winfo_screenheight()/2 - windowHeight/2)
    # Positions the window in the center of the page.
    warningPopUP.geometry("+{}+{}".format(positionRight, positionDown))

    warningPopUP.wm_title("Warning")
    label = Label(warningPopUP, text="Please, use a strong password for encrypting your files"+"\n"+"Low password would allow someone malicious to easily decrypt your files.")
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(warningPopUP, text="OK", command = warningPopUP.destroy)
    B1.pack()
    warningPopUP.mainloop()

def popUpEmptyPassword():
    emptyPasswordPopUP = Tk()
    emptyPasswordPopUP.geometry("450x100")
    # Gets the requested values of the height and widht.
    windowWidth = emptyPasswordPopUP.winfo_reqwidth()
    windowHeight = emptyPasswordPopUP.winfo_reqheight()
    # Gets both half the screen width/height and window width/height
    positionRight = int(emptyPasswordPopUP.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(emptyPasswordPopUP.winfo_screenheight()/2 - windowHeight/2)
    # Positions the window in the center of the page.
    emptyPasswordPopUP.geometry("+{}+{}".format(positionRight, positionDown))

    emptyPasswordPopUP.wm_title("Empty password")
    label = Label(emptyPasswordPopUP, text="The password for encrypting process cannot be empty.")
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(emptyPasswordPopUP, text="OK", command = emptyPasswordPopUP.destroy)
    B1.pack()
    emptyPasswordPopUP.mainloop()

def popUpLoading():
    LoadingPopUP = Tk()
    LoadingPopUP.geometry("450x100")
    # Gets the requested values of the height and widht.
    windowWidth = LoadingPopUP.winfo_reqwidth()
    windowHeight = LoadingPopUP.winfo_reqheight()
    # Gets both half the screen width/height and window width/height
    positionRight = int(LoadingPopUP.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(LoadingPopUP.winfo_screenheight()/2 - windowHeight/2)
    # Positions the window in the center of the page.
    LoadingPopUP.geometry("+{}+{}".format(positionRight, positionDown))

    LoadingPopUP.wm_title("Loading")
    label = Label(LoadingPopUP, text="Operation in progress... Please wait.")
    label.pack(side="top", fill="x", pady=10)
    LoadingPopUP.mainloop()

def popUpNoFileSelected():
    noFileSelectedPopUP = Tk()
    noFileSelectedPopUP.geometry("450x100")
    # Gets the requested values of the height and widht.
    windowWidth = noFileSelectedPopUP.winfo_reqwidth()
    windowHeight = noFileSelectedPopUP.winfo_reqheight()
    # Gets both half the screen width/height and window width/height
    positionRight = int(noFileSelectedPopUP.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(noFileSelectedPopUP.winfo_screenheight()/2 - windowHeight/2)
    # Positions the window in the center of the page.
    noFileSelectedPopUP.geometry("+{}+{}".format(positionRight, positionDown))

    noFileSelectedPopUP.wm_title("Error")
    label = Label(noFileSelectedPopUP, text="No file or directory selected.")
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(noFileSelectedPopUP, text="OK", command = noFileSelectedPopUP.destroy)
    B1.pack()
    noFileSelectedPopUP.mainloop()

######################################################################################################################################################################
###########################################################FOLDERS/FILES ENCRYPTION/DESENCRYPTION FUNCTIONS###########################################################
######################################################################################################################################################################

def encryptFolder():
    gui_passwd = pwd_input.get()
    if gui_passwd == "":
        popUpEmptyPassword()
    else:
        passwd = str(gui_passwd)
        filename = str(filedialog.askdirectory())
        gui.update()
        if filename:
            if os.path.isfile(filename+".zip"):
                os.remove(filename+".zip")
            shutil.make_archive(filename, 'zip', filename)
            zip_filename = filename + '.zip'
            pyAesCrypt.encryptFile(zip_filename, filename+".enc", passwd, bufferSize)

            
            os.remove(zip_filename)
            shutil.rmtree(filename, ignore_errors=True)
            popUpSuccessToEncrypt()
        else:
            popUpNoFileSelected()

def decryptFolder():
    filename = str(filedialog.askopenfilename())
    gui.update()
    gui_passwd = pwd_input.get()
    if gui_passwd == "":
        popUpEmptyPassword()
    else:
        passwd = str(gui_passwd)

        if filename:
            zip_filename = filename.replace(".enc",".zip")

            pyAesCrypt.decryptFile(filename, zip_filename, passwd, bufferSize)
            try:
                shutil.unpack_archive(zip_filename,zip_filename.replace(".zip",""))
                os.remove(filename)
                os.remove(zip_filename)
                popUpSuccessToDecrypt()
            except:
                popUpBadType()
            

        else: 
            popUpNoFileSelected()

def encryptFiles():
    gui_passwd = pwd_input.get()
    if gui_passwd == "":
        popUpEmptyPassword()
    else:
        passwd = str(gui_passwd)

        filename = str(filedialog.askopenfilename())
        gui.update()
        if filename:
            pyAesCrypt.encryptFile(filename,filename+".enc", passwd, bufferSize)

            os.remove(filename)
            popUpSuccessToEncrypt()

        else:
            popUpNoFileSelected()

def decryptFiles():    
    gui_passwd = pwd_input.get()
    filename = str(filedialog.askopenfilename())
    gui.update()
    if filename:
        passwd = str(gui_passwd)
        
        destination_filename = filename.replace(".enc","")
        
        try:
            pyAesCrypt.decryptFile(filename, destination_filename, passwd, bufferSize)
            os.remove(filename)

            popUpSuccessToDecrypt()
        except:
            popUpFailedToDecrypt()
    else:
        popUpNoFileSelected()

######################################################################################################################################################################
####################################################################### MAIN SECTION BUILDING GUI ####################################################################
######################################################################################################################################################################

popUpWarning()
gui = Tk()
gui.title("Ratpy Encryptor V1.0")
gui.geometry("290x230")


windowWidth = gui.winfo_reqwidth()
windowHeight = gui.winfo_reqheight()
positionRight = int(gui.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(gui.winfo_screenheight()/2 - windowHeight/2)
gui.geometry("+{}+{}".format(positionRight, positionDown))
how_to_work_button = Button(text="HOW TO WORKS RATPY ENCRYPTOR", command=howToWork, width=50, justify="left")
how_to_work_button.pack()
pwd_label = Label(gui, width=20, justify="left")
pwd_label.pack()
pwd_label.config(text="Enter your password :")
pwd = StringVar()
pwd_input = Entry(gui, textvariable=pwd,width=20, show="*")
pwd_input.pack()
encrypt_button = Button(text="Encrypt file", command=encryptFiles, width=50)
encrypt_button.pack()
encryptDir_button = Button(text="Encrypt folder", command=encryptFolder, width=50)
encryptDir_button.pack()
decrypt_button = Button(text="Decrypt file", command=decryptFiles, width=50)
decrypt_button.pack()
decryptDir_button = Button(text="Decrypt folder", command=decryptFolder, width=50)
decryptDir_button.pack()
exit_button = Button(text="Quit", command=gui.destroy, width=50)
exit_button.pack()
license_label = Label(gui, width=20, justify="left")
license_label.config(text="By Guezone - GNU GPLv3")
license_label.pack()
gui.mainloop()
