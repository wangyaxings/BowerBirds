#Find twinkle things For Ali net pan

# -*- coding: utf-8 -*-
import PySimpleGUI as sg
from FindAlyShareLinks import FindAlyShareLinks
import pyperclip

# Convert Share links to str like this

def ConvertShareLinksListToStr(linksList):
    ret = ""
    for item in linksList:
        if item["code"] == "":
            ret = ret + item["link"] + "\n"
        else:
            ret = ret + item["link"] + "  提取码:" + item["code"] + "\n"
    return ret

# Create some widgets
text = sg.Text("Web site:")
text_entry = sg.InputText()
ok_btn = sg.Button('OK')
cancel_btn = sg.Button('Cancel')
layout = [[text, text_entry],
          [ok_btn, cancel_btn]]
 
# Create the Window
window = sg.Window('Aly BowerBird', layout)
 
# Create the event loop
while True:
    event, values = window.read()
    content = ""
    for key,value in values.items():
        #print(key,value)
        content = value
    if event in (None, 'Cancel'):
        # User closed the Window or hit the Cancel button
        break
    else:
       pyperclip.copy(ConvertShareLinksListToStr(FindAlyShareLinks(content)))
 
window.close()