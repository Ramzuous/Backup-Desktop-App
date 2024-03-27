import tkinter as tk
from tkinter import Tk, Toplevel
from tkinter.ttk import Label, Button

class Window:

    def __init__(self, appName, settingsName, runBackupName):
    
        self.root = tk.Tk()
        self.root.title(appName)
        
        self.root.geometry("250x100")

        self.root.resizable(0,0)

        #inputLabel = tk.Label(self, text=lableInputName)
        #inputLabel.pack()

        #operationPath = tk.Entry(self)
        #operationPath.pack()

        #inputExtensionLabel = tk.Label(self, text=labelInputExtension)
        #inputExtensionLabel.pack()
        
        #inputExtension = tk.Entry(self)
        #inputExtension.pack()
        
        #outputExtensionLabel = tk.Label(self, text=labelOutputExtension)
        #outputExtensionLabel.pack()
        
        #outputExtension = tk.Entry(self)
        #outputExtension.pack()

        self.settings_button = tk.Button(text=settingsName, command=self.openSettings)
        self.settings_button.pack(pady=10)

        self.runBackup_button = tk.Button(text=runBackupName, command=self.runBackup)
        self.runBackup_button.pack(pady=10)

        self.root.mainloop()

    def openSettings(self):
        
        settingsWindow = Toplevel()
        
        settingsWindow.title(settingsName)
        
        settingsWindow.geometry("400x300")
        
        settingsWindow.resizable(0,0)
        
        settingsWindow.grab_set() # block main window
        
        Label(settingsWindow, text ="This is a new window").pack() 
        
        #self.runBackup_button = tk.Button(text=runBackupName, command=self.runBackup)
        
        #Button(settingsWindow, text=saveButton, command=saveSettings).pack()
    
    def saveSettinga(self):
        print("Save Settings")
    
    def runBackup(self):
        print("Run Backup")
            

# Variables

appName = "Backup"

settingsName = "Settings"

runBackupName = "Run Backup"

saveButton="Save"

###############################            
w = Window(appName, settingsName, runBackupName)