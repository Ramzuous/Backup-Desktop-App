import tkinter as tk

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
        
        settingsWindow = tk.Tk()
        
        settingsWindow.title(settingsName)
        
        settingsWindow.geometry("400x300")

        settingsWindow.resizable(0,0)
    
        inputExtensionLabel = tk.Label(self, text="This is a new window")
    
        #Label(settingsWindow, text ="This is a new window").pack()
    
        #print("Open Settings, name: ", settingsName)
        
        
    def runBackup(self):
        print("Run Backup")
            

# Variables

appName = "Backup"

settingsName = "Settings"

runBackupName = "Run Backup"

###############################            
w = Window(appName, settingsName, runBackupName)