from tkinter import *
from tkinter.scrolledtext import ScrolledText
import Pin as pin

# defines the root window for the program
root = Tk()
root.title('SDC B2C Fraud Pin Code Blocking')
root.resizable(False,False) # disable resizing
# set default font to Arial
root.option_add('*Font', 'Arial')
root.option_add('*Label.Font', 'Arial 12')

# Frame 1 - Pin Codes
## Must set width on both Label and Scrolledtext
## else the widgets will occupy > 50px
pinFrame = Frame(root, width=25)
## Label
pinLabel = Label(pinFrame, text='Paste pin codes here:', width=20, anchor='w')
pinLabel.grid(column=0, row=0, sticky='W')
## Scrolledtext
pinCodesTxt = ScrolledText(pinFrame, width=20)
pinCodesTxt.grid(column=0, row=1, stick='W')
## Pack pinFrame
pinFrame.grid(column=0, row=0, padx=[10, 0], pady=[5, 10])


# Frame 2 - Redeemed Pins
reFrame = Frame(root, width=20)
## Label
reLabel = Label(reFrame, text='Redeemed Pins:', width=20, anchor='w')
reLabel.grid(column=0, row=0, sticky='W')
## Scrolledtext
rePinTxt = ScrolledText(reFrame, width=20)
rePinTxt.grid(column=0, row=1, sticky='W')
## Pack reFrame
reFrame.grid(column=1, row=0, padx=[10, 0], pady=[5, 10])


# Frame 3 - Unredeemed/Blocked Pins
unFrame = Frame(root, width=20)
## Label
unLabel = Label(unFrame, text='Unredeemed/Blocked Pins:', width=25, anchor='w')
unLabel.grid(column=0, row=0, sticky='W')
## Scrolledtext
unPinTxt = ScrolledText(unFrame, width=25)
unPinTxt.grid(column=0, row=1, sticky='W')
## Pack unFrame
unFrame.grid(column=2, row=0, padx=[10, 0], pady=[5, 10])

# Frame 4 - Buttons
btnFrame = Frame(root, width=20)
## Button - Check
btnCheck = Button(btnFrame, text='Check Pins', fg='green')
btnCheck.pack(fill=X, pady=10)
## Button - Export
btnExport = Button(btnFrame, text='Export to Excel')
btnExport.pack(fill=X, pady=10)
## Button - Quit
btnQuit = Button(btnFrame, text='Quit', command=root.destroy, fg='red')
btnQuit.pack(fill=X, pady=10)
## Pack btnFrame
btnFrame.grid(column=3, row=0, padx=[0, 10], pady=[5, 10])

# execute program
root.mainloop()