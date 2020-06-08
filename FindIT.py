from tkinter import *
import wikipedia
from tkinter import filedialog
from tkinter import messagebox
import os,platform
from tkinter import colorchooser
from tkinter import ttk


root = Tk()
root.title("FIND IT")


root.maxsize(width=700,height=440)

#file for functioning of Save & Save AS
current_file = "no_file"



def front_colr():
    clr = colorchooser.askcolor(title="Front color")
    text_1.config(fg=clr[1])
def back_colr():
    clr = colorchooser.askcolor(title="BackGround color")
    text_1.config(bg=clr[1])

def open_file(event=""):
    try:
        file1 = filedialog.askopenfile(initialdir="",filetypes=(("txt files(*.txt)", "*.txt"), ("all files(*.*)", "*.*")))
        if file1 is None:
            return
        else:
            text_1.delete(1.0, END)

            for i in file1:
                text_1.insert(INSERT, i)
            global current_file
            current_file = file1.name

        file1.close()

    except:
        popup = messagebox.showerror("File Selection","Please Choose a valid file")
root.bind('<Control-o>',open_file)

def new_file():
    text_1.delete(1.0,END)
    global current_file
    current_file = "no_file"
root.bind('<Control-N>',new_file)


def copy_text():
    text_1.clipboard_clear()
    text_1.clipboard_append(text_1.selection_get())
root.bind('<Control-C>',copy_text)
def cut_text():
    copy_text()
    text_1.delete("sel.first","sel.last")
root.bind('<Control-X>',cut_text)
def paste_text():
    text_1.insert(INSERT,text_1.clipboard_get())
root.bind('Control-V',paste_text)
def save_as():
    try:
        savethefile = filedialog.asksaveasfile(mode="w",defaultextension=".txt",filetypes=(("text file(*.txt)",".txt"),
                                                                                           ("html file(*.html)","*.html"),
                                                                                           ("javascript file(*.js)","*.js"),
                                                                                           ("python file(*.py)","*.py"),
                                                                                           ("ruby file(*.rb)","*.rb"),
                                                                                           ("perl file(*.pl)","*.pl"),
                                                                                           ("php file(*.php)",".php"),
                                                                                           ("bash file(*.sh)","*.sh"),
                                                                                           ("batch file(*.bat)","*.bat"),
                                                                                           ("All files","*.*")))
        if savethefile is None:
            return
        else:
            save2file = text_1.get(1.0,END)
            global current_file
            current_file = savethefile.name
            savethefile.write(save2file)
            savethefile.close()
    except:
        return


def save_file(event=""):
    if current_file == "no_file":
        save_as()
    else:
        f = open(current_file, "w+")
        f.write(text_1.get(1.0, END))
        f.close()
root.bind('<Control-s>',save_file)

def bing():
    try:
        message = "Sorry This feature not available for your device"
        if platform.system() == 'Windows':
            os.system(' "C:\Program Files\Internet Explorer\iexplore.exe" https://www.bing.com/search?q={}&form=NPCTXT'.format(entry.get()))
        else:
            try:
               os.system("open https://www.google.co.in/ ")
            except:
                text_1.delete(1.0, END)
                text_1.insert(INSERT, message)
    except:
        messagebox.showerror("Internet Issue","Check Internet")

def youtube():
    try:
        if platform.system() == 'Windows':
            os.system(' "C:\Program Files\Internet Explorer\iexplore.exe" https://www.youtube.com/results?search_query={}'.format(entry.get()))
        elif platform.system() == 'Darvin':
            try:
               os.system("open  https://www.youtube.com/results?search_query={}".format(entry.get()))
            except:
                message = "Sorry This feature not available for your device"
                text_1.delete(1.0,END)
                text_1.insert(INSERT,message)
        else:
            os.system("firefox https://www.youtube.com/results?search_query={}".format(entry.get()))
    except:
        messagebox.showerror(("Internet Issue","Check Internet"))
main_menu = Menu(root)
root.config(menu=main_menu)

#file_menu
file_open = Menu(main_menu,tearoff=False)
main_menu.add_cascade(label="File",menu=file_open)
file_open.add_command(label="New                     Ctrl+N",command=new_file)
file_open.add_command(label="Open                   Ctrl+O",command=open_file)
file_open.add_separator()
file_open.add_command(label="Save As               Ctrl+S",command=save_as)
file_open.add_command(label="Save                    Ctrl+S",command=save_file)
file_open.add_separator()
file_open.add_command(label="Exit",command=root.destroy)

#Edit menu
edit_menu = Menu(main_menu,tearoff=False)
main_menu.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="Copy         Ctrl+C",command=copy_text)
edit_menu.add_command(label="Cut            Ctrl+X",command=cut_text)
edit_menu.add_command(label="Paste         Ctrl+V",command=paste_text)

#View menu
view_menu = Menu(main_menu,tearoff=False)
main_menu.add_cascade(label="view",menu=view_menu)
view_menu.add_command(label="front color",command=front_colr)
view_menu.add_command(label="Background Color",command=back_colr)

#Advance menu
advance_menu = Menu(main_menu,tearoff=False)
main_menu.add_cascade(label="Advance",menu=advance_menu)
advance_menu.add_command(label="Search with bing",command=bing)
advance_menu.add_command(label="Search on Youtube",command=youtube)

#Exit menu
exit_menu = Menu(main_menu,tearoff=False)
main_menu.add_cascade(label="Exit",menu=exit_menu)
exit_menu.add_command(label="EXIT",command=root.quit)

def search_func(event=""):
    try:
        if entry.get() != "":
            entry_value = entry.get()
            text_value = wikipedia.summary(entry_value)
            text_1.delete(1.0, END)
            text_1.insert(INSERT, text_value)


    except:
        popup = messagebox.showerror("ERROR", "Please Check Your Internet Connection or Type Right Word")

root.bind('<Return>',search_func)

frame_1 = Frame(root,borderwidth=3)
frame_2 = Frame(root,borderwidth=4)
entry = Entry(frame_1,width=120,bg="blue",fg="white")
entry.pack()
scroll = Scrollbar(frame_2)
button = Button(frame_1,text="SEARCH",width=100,height=2,bg="red",fg="black",command=search_func).pack()
text_1 = Text(frame_2,bg="yellow",wrap=WORD,width=85,height=80,undo=True,yscrollcommand=scroll.set)
text_1.pack(side=LEFT)
scroll.config(command=text_1.yview)
scroll.pack(side=RIGHT,fill=Y)
frame_1.pack()
frame_2.pack()

mainloop()