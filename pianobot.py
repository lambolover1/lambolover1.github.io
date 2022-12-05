# Hier werden die Bibliotheken importiert
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con, win32gui
from pyWinActivate import win_activate, win_wait_active
from time import sleep

#Aktiviert das Fenster, anhand des Titel
win_activate(window_title="Edge", partial_match=True)
sleep(0.5)
hwnd = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)

# Die nachfolgenden Zeilen definieren was beim Aufruf der Funktion "Click" passiert
# Der Cursor geht auch die mitgegbene x-y Position und machen einen Mausklick
def click(x,y): 
      win32api.SetCursorPos((x,y)) 
      win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
      time.sleep(0.03) #mimipause zwischen dem drücken und loslassen 
      win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0) 
      
# Hier werden die viel Spalten nach den schwarzen Feldern geprüft
# sobald schwarz detektiert wurde wird die Maus an dieser Position geklickt
while keyboard.is_pressed ("q") == False: #wiederhole solange q nicht gedrückt ist 
    if pyautogui.pixel (401, 485) [2] == 0:   # [0]rd [1]gn [2]bl -> weil schwarz -> nur ein Wert  auf 0 prüfen 
        click (401, 485)  # entsprechende MausFunktion mit  X Y aufrufen 
    if pyautogui.pixel (538, 485) [2] == 0:    #dito wie oben für Spalte 2
        click (538, 485) 
    if pyautogui.pixel (673, 485) [2] == 0:    #dito wie oben für Spalte 3
        click (673, 485) 
    if pyautogui.pixel (794, 485) [2] == 0:    #dito wie oben für Spalte 4
        click (794, 485) 
    
