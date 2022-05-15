import os
import time
from tkinter import *
from tkinter.filedialog import askopenfile
from tkinter.scrolledtext import ScrolledText
from tkinter.messagebox import *

tk = Tk()
tk.title(".py -> .exe")
tk.resizable(0, 0)

f = None

def browse():
    global f, btn
    try:
        f = askopenfile().name # get the py file
        btn["text"] = os.path.basename(f)
    except:
        f = None

def convert():
    global f, btn, ver, des
    OK = False
    try:
        dots = 0
        for x in ver.get(): # check the number of dots in version
            if x == ".":
                dots += 1
            else:
                x = int(x)
        if dots < 4:
            OK = True
    except:
        showwarning("","The version must be int.int.int... with max 3 dots.")
    if OK:
        try:
            if f is None:
                showwarning("","You must choose a file to convert.")
                btn.focus()
            elif ver.get() == "":
                showwarning("","You must enter a version.")
                ver.focus()
            else:
                with open("setup.py", "w") as f_: # fill a new file setup.py (installer)
                    f_.write("NAME = '" + f +
                        "'\nVERSION = '" + ver.get() +
                        "'\nDESCRIPTION = \"\"\"" + des.get(1.0, "end") +
                        "\"\"\"\nFILENAME = '" + f +
                        "'\n\nfrom cx_Freeze import setup, Executable\nsetup(name = NAME, version = VERSION, description = DESCRIPTION, executables = [Executable(FILENAME)])")
                with open("setup.bat", "w") as f_: # fill a new file setup.bat (installation launcher)
                    f_.write("py setup.py build")
                os.system("setup.bat")
                btn["text"] = "Browse..."
                f = None
                os.remove("setup.py")  # remove files created in this script
                os.remove("setup.bat") #
                showinfo("Information","End. Your exe file is in folder 'build'.")
        except:
            showerror("Error","Error detected.")


# create GUI

Label(text="File to convert").grid(column=0, row=0, sticky="w")

btn = Button(text="Browse...", command=browse)
btn.grid(column=1, row=0)

Label(text="Version").grid(column=0, row=2, sticky="w")

ver = Entry()
ver.grid(column=1, row=2, padx=5)

Label(text="Description").grid(column=0, row=3, sticky="w")

des = ScrolledText(width=15, height=5, wrap=WORD)
des.grid(column=1, row=3)

Label(text="Convert to .exe").grid(column=0, row=4, sticky="w")

Button(text="Convert", command=convert).grid(column=1, row=4, pady=5)

tk.mainloop()
