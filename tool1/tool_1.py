import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
from subprocess import call

def CreateWidgets():
	link_Label = Label(root, text ="Select Source Directory : ",bg = "#E8D579")
	link_Label.grid(row = 1, column = 0,pady = 5, padx = 5)
	
	root.sourceText = Entry(root, width = 50,textvariable = sourceLocation)
	root.sourceText.grid(row = 1, column = 1, pady = 15, padx = 15,columnspan = 2)

	source_browseButton = Button(root, text ="Browse",command = SourceBrowse, width = 15)
	source_browseButton.grid(row = 1, column = 5, pady = 15, padx = 15,columnspan = 2)
	
	destinationLabel = Label(root, text ="Select Destination Directory : ",bg ="#E8D579")
	destinationLabel.grid(row = 2, column = 0,pady = 15, padx = 15)
	
	root.destinationText = Entry(root, width = 50,textvariable = destinationLocation)
	root.destinationText.grid(row = 2, column = 1,pady = 15, padx = 15,columnspan = 2)

	dest_browseButton = Button(root, text ="Browse",command = DestinationBrowse, width = 15)
	dest_browseButton.grid(row = 2, column = 5,pady = 15, padx = 15)
	
	ChoiceLabel = Label(root, text ="Enter Command to execute : ",bg ="#E8D579")      # /S or /E
	ChoiceLabel.grid(row = 4, column = 0,pady = 15, padx = 15)

	root.op = Entry(root, width = 50)
	root.op.grid(row = 4, column = 1,pady = 15, padx = 15)
	
	copyButton = Button(root, text ="Execute",command = CopyS, width = 15)
	copyButton.grid(row = 6, column = 1)

def SourceBrowse():

	files_list = filedialog.askdirectory(initialdir ="C:/Users/ Dell/ Desktop")
	root.sourceText.insert('1', files_list)
	
def DestinationBrowse():
	destinationdirectory = filedialog.askdirectory(initialdir ="C:/Users/ Dell/ Desktop")
	root.destinationText.insert('1', destinationdirectory)
	
def CopyS():
	cd = root.op.get()
	call(["robocopy",sourceLocation.get(), destinationLocation.get(),cd])
	messagebox.showinfo("SUCCESS", "PROCESS SUCESSFULLY COMPLETED")


root = tk.Tk()

root.geometry("680x210")
root.title("Robocopy GUI")
root.config(background = "black")
	
sourceLocation = StringVar()
destinationLocation = StringVar()
	
CreateWidgets()
root.eval('tk::PlaceWindow . center')
root.mainloop()

