import tkinter
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import cv2
import pytesseract
import os
import pyttsx3
from translate import Translator
from langdetect import detect

engine = pyttsx3.init("sapi5")
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
langc=''
langin=''
vid=''
code=''
tran=''
def langcf(r):
    global langc
    langc=r
    print(langc)
def langinf(r):
    global langin
    langin=r
    print(langin)
def voice(t):
    global tran
    tran=t
    engine.say(tran)
    engine.runAndWait()
l1='english'
l2='german'
l3='french'
l4='spanish'
l5='japanese'
l6='chinese'
l7='korean'
l8='russian'
l9='italian'
l10='portuguese'
top=Tk()
m=tkinter.Tk()


def button():
        top.button = ttk.Button(top.labelFrame, text = "Browse Image",command =lambda: fileDialog)
        top.button.grid(column = 1, row = 1)
def button1():
        top.button1 = ttk.Button(top.labelFrame, text = "English",command=lambda: langcf(l1))
        top.button1.grid(column = 1, row = 2)
def button2():
        top.button = ttk.Button(top.labelFrame, text = "German",command=lambda: langcf(l2))
        top.button.grid(column = 1, row = 3)
def button3():
        top.button1 = ttk.Button(top.labelFrame, text = "French",command = lambda: langcf(l3))
        top.button1.grid(column = 1, row = 4)
def button4():
        top.button1 = ttk.Button(top.labelFrame, text = "Spanish",command=lambda: langcf(l4))
        top.button1.grid(column = 1, row = 5)
def button5():
        top.button = ttk.Button(top.labelFrame, text = "Japanese",command=lambda: langcf(l5))
        top.button.grid(column = 1, row = 6)
def button6():
        top.button1 = ttk.Button(top.labelFrame, text = "Chinese",command=lambda: langcf(l6))
        top.button1.grid(column = 1, row = 7)
def button7():
        top.button1 = ttk.Button(top.labelFrame, text = "Korean",command=lambda: langcf(l7))
        top.button1.grid(column = 1, row = 8)
def button8():
        top.button1 = ttk.Button(top.labelFrame, text = "Russian",command=lambda: langcf(l8))
        top.button1.grid(column = 1, row = 9)
def button9():
        top.button = ttk.Button(top.labelFrame, text = "Italian",command=lambda: langcf(l9))
        top.button.grid(column = 1, row = 10)
def button10():
        top.button1 = ttk.Button(top.labelFrame, text = "Portuguese",command=lambda: langcf(l10))
        top.button1.grid(column = 1, row = 11)
    
def Button1():
        top.button1 = ttk.Button(top.labelFrame, text = "English",command=lambda: langinf(l1))
        top.button1.grid(column = 1, row = 2)
def Button2():
        top.button = ttk.Button(top.labelFrame, text = "German",command=lambda: langinf(l2))
        top.button.grid(column = 1, row = 3)
def Button3():
        top.button1 = ttk.Button(top.labelFrame, text = "French",command = lambda: langinf(l3))
        top.button1.grid(column = 1, row = 4)
def Button4():
        top.button1 = ttk.Button(top.labelFrame, text = "Spanish",command=lambda: langinf(l4))
        top.button1.grid(column = 1, row = 5)
def Button5():
        top.button = ttk.Button(top.labelFrame, text = "Japanese",command=lambda: langinf(l5))
        top.button.grid(column = 1, row = 6)
def Button6():
        top.button1 = ttk.Button(top.labelFrame, text = "Chinese",command=lambda: langinf(l6))
        top.button1.grid(column = 1, row = 7)
def Button7():
        top.button1 = ttk.Button(top.labelFrame, text = "Korean",command=lambda: langinf(l7))
        top.button1.grid(column = 1, row = 8)
def Button8():
        top.button1 = ttk.Button(top.labelFrame, text = "Russian",command=lambda: langinf(l8))
        top.button1.grid(column = 1, row = 9)
def Button9():
        top.button = ttk.Button(top.labelFrame, text = "Italian",command=lambda: langinf(l9))
        top.button.grid(column = 1, row = 10)
def Button10():
        top.button1 = ttk.Button(top.labelFrame, text = "Portuguese",command=lambda: langinf(l10))
        top.button1.grid(column = 1, row = 11)
def voicebutton():
    top.button1 = ttk.Button(top.labelFrame, text = "Voice",command=lambda: voice(tran))
    top.button1.grid(column = 1, row = 13)

def fileDialog():
    top.path = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype =(("jpg files","*.jpg"),("all files","*.*")) )
    top.label = ttk.Label(top.labelFrame)
    top.label.grid(column = 0, row = 0)
    top.label.configure(text = top.path)
    rev = top.path[::-1]
    lst=rev.split("/")
    filename=lst[0][::-1]
    return filename
def voicepath():
    global vid
    global langin
    if langin=='english':
        vid='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
    elif langin=='german':
        vid='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_DE-DE_HEDDA_11.0'
    elif langin=='french':
        vid='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_FR-FR_HORTENSE_11.0'
    elif langin=='spanish':
        vid='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'
    elif langin=='japanese':
        vid='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_JA-JP_HARUKA_11.0'
    elif langin=='chinese':
        vid='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ZH-CN_HUIHUI_11.0'
    elif langin=='korean':
        vid='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_KO-KR_HEAMI_11.0'
    elif langin=='russian':
        vid='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0'
    elif langin=='italian':
        vid='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_IT-IT_ELSA_11.0'
    elif langin=='portuguese':
        vid='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PT-BR_MARIA_11.0'


top.title("OCR Language Translator")
top.minsize(640, 400)
top.wm_iconbitmap('iconn.ico')



def run():
    global tran
    voicepath()
    engine.setProperty('voice',vid)
    engine.setProperty('rate',110)
    engine.setProperty('volume',1)


    #custom= r'--oem 3 --psm 6'
    if langc=='english':
        code='eng'
    elif langc=='german':
        code='ger'
    elif langc=='french':
        code='fre'
    elif langc=='spanish':
        code='spa'
    elif langc=='japanese':
        code='jpn'
    elif langc=='chinese':
        code='zho'
    elif langc=='korean':
        code='kor'
    elif langc=='russian':
        code='rus'
    elif langc=='italian':
        code='ita'
    txt=pytesseract.image_to_string(img,code)
    key = txt
    msg1= tkinter.Message(m, text = key)
    msg1.config(bg='white',font=('times', 14, 'normal'))
    msg1.pack()


    langd=detect(txt)

    if langd=='en':
        langdet='english'
    elif langd=='de':
        langdet='german'
    elif langd=='fr':
        langdet='french'
    elif langd=='es':
        langdet='spanish'
    elif langd=='ja':
        langdet='japanese'
    elif langd=='zh':
        langdet='chinese'
    elif langd=='ko':
        langdet='korean'
    elif langd=='ru':
        langdet='russian'
    elif langd=='it':
        langdet='italian'
    elif langd=='pt':
        langdet='portuguese'
    translator= Translator(from_lang=langdet,to_lang=langin)
    tran= translator.translate(txt)
    key = tran
    message = tkinter.Message(m, text = key)
    message.config(bg='white', font=('times', 14, 'normal'))
    message.pack()
    m.mainloop()
def submit():
    top.button = ttk.Button(top.labelFrame, text = "Submit",command =run)
    top.button.grid(column = 1, row = 12)

top.labelFrame = ttk.LabelFrame(top, text = "Select image to translate")
top.labelFrame.grid(column = 0, row = 1, padx = 20, pady = 20)
button()
img = cv2.imread(fileDialog())        
top.labelFrame = ttk.LabelFrame(top, text = "Select input language")
top.labelFrame.grid(column = 4, row = 1, padx = 20, pady = 20)
button1()
button2()
button3()
button4()
button5()
button6()
button7()
button8()
button9()
button10()
top.labelFrame = ttk.LabelFrame(top, text = "Select output language")
top.labelFrame.grid(column = 6, row = 1, padx = 20, pady = 20)
Button1()
Button2()
Button3()
Button4()
Button5()
Button6()
Button7()
Button8()
Button9()
Button10()
top.labelFrame = ttk.LabelFrame(top, text = "Result")
top.labelFrame.grid(column = 8, row = 1, padx = 20, pady = 20)
submit()
voicebutton()    
    
top.mainloop()


