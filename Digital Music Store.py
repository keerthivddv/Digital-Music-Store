from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from time import strftime
import mysql.connector

dms=Tk()
dms.title("Digital Music Store")
dms.geometry("1100x575")
dms.configure(background="purple")
Label(dms,text="Digital Music Store",font = ('monotype corsiva',35,"italic"), background = 'purple', foreground = 'white').place(x=385,y=100)
s=Entry(dms)
s.place(x=5,y=5,height=26,width=300)
# Digital Clock
def time(): 
    string = strftime('%H:%M:%S IST %n(UTC +05:30)') 
    lbl.config(text = string) 
    lbl.after(1000, time)
    
lbl = Label(dms, font = ('arial',13,"italic"), background = 'purple', foreground = 'white') 
lbl.pack(anchor = 'ne') 
time() 

#Toplevel for search button
def display_s():
    sd=Toplevel(dms)
    sd.title("Songs Display")
    tree = ttk.Treeview(sd)
    tree = ttk.Treeview(sd, columns=("SNo","Song_Album_Name","Artist","Duration"), show='headings')
    tree.heading("SNo", text="SNo",anchor=CENTER)
    tree.heading("Song_Album_Name", text="Song_Album_Name",anchor=CENTER)
    tree.heading("Artist", text="Artist",anchor=CENTER)
    tree.heading("Duration", text="Duration",anchor=CENTER)
    tree.pack()
    def show():
        Song_Album_Name=s.get()
        Artist=s.get()
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="",database="dmsdb")
        mycursor = mysqldb.cursor()
        q="SELECT * FROM songs WHERE Song_Album_Name=%s OR Artist=%s;"
        val=(Song_Album_Name,Artist,)
        mycursor.execute(q,val)
        records = mycursor.fetchall()
        for i, (SNo,Song_Album_Name,Artist,Duration) in enumerate(records, start=1):
            tree.insert("", 'end', values=(SNo,Song_Album_Name,Artist,Duration))
        mysqldb.close()
    show()
    sd.mainloop()
#Showing all songs
def display_sas():
    sd=Toplevel(dms)
    sd.title("Songs Display")
    tree = ttk.Treeview(sd)
    tree = ttk.Treeview(sd, columns=("SNo","Song_Album_Name","Artist","Duration"), show='headings')
    tree.heading("SNo", text="SNo",anchor=CENTER)
    tree.heading("Song_Album_Name", text="Song_Album_Name",anchor=CENTER)
    tree.heading("Artist", text="Artist",anchor=CENTER)
    tree.heading("Duration", text="Duration",anchor=CENTER)
    tree.pack()
    def show_sas():
        Song_Album_Name=s.get()
        Artist=s.get()
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="",database="dmsdb")
        mycursor = mysqldb.cursor()
        q="SELECT * FROM songs"
        mycursor.execute(q)
        records = mycursor.fetchall()
        for i, (SNo,Song_Album_Name,Artist,Duration) in enumerate(records, start=1):
            tree.insert("", 'end', values=(SNo,Song_Album_Name,Artist,Duration))
        mysqldb.close()
    show_sas()
    sd.mainloop()

def artist():
    a=Toplevel(dms)
    a.geometry("270x300")
    Label(a,text="Artist Name").place(x=15,y=110)
    a1=Entry(a)
    a1.place(x=135,y=110)
    def display_a():
        sd=Toplevel(dms)
        sd.title("Songs Display")
        tree = ttk.Treeview(sd)
        tree = ttk.Treeview(sd, columns=("SNo","Song_Album_Name","Artist","Duration"), show='headings')
        tree.heading("SNo", text="SNo",anchor=CENTER)
        tree.heading("Song_Album_Name", text="Song_Album_Name",anchor=CENTER)
        tree.heading("Artist", text="Artist",anchor=CENTER)
        tree.heading("Duration", text="Duration",anchor=CENTER)
        tree.pack()
        def show_a():
            Artist=a1.get()
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="",database="dmsdb")
            mycursor = mysqldb.cursor()
            q="SELECT * FROM songs WHERE Artist=%s;"
            val=(Artist,)
            mycursor.execute(q,val)
            records = mycursor.fetchall()
            for i, (SNo,Song_Album_Name,Artist,Duration) in enumerate(records, start=1):
                tree.insert("", 'end', values=(SNo,Song_Album_Name,Artist,Duration))
            mysqldb.close()
        show_a()
        sd.mainloop() 
    Button(a,text="Search",command=display_a).place(x=110,y=220)
    a.mainloop()
 
def ta():
    b=Toplevel(dms)
    b.geometry("270x300")
    Label(b,text="Song/Album Name").place(x=15,y=70)
    Label(b,text="Artist Name").place(x=15,y=110)
    b1=Entry(b)
    b1.place(x=135,y=70)
    b2=Entry(b)
    b2.place(x=135,y=110)
    def display_ta():
        sd=Toplevel(dms)
        sd.title("Songs Display")
        tree = ttk.Treeview(sd)
        tree = ttk.Treeview(sd, columns=("SNo","Song_Album_Name","Artist","Duration"), show='headings')
        tree.heading("SNo", text="SNo",anchor=CENTER)
        tree.heading("Song_Album_Name", text="Song_Album_Name",anchor=CENTER)
        tree.heading("Artist", text="Artist",anchor=CENTER)
        tree.heading("Duration", text="Duration",anchor=CENTER)
        tree.pack()
        def show_ta():
            Song_Album_Name=b1.get()
            Artist=b2.get()
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="",database="dmsdb")
            mycursor = mysqldb.cursor()
            q="SELECT * FROM songs WHERE Song_Album_Name=%s OR Artist=%s;"
            val=(Song_Album_Name,Artist,)
            mycursor.execute(q,val)
            records = mycursor.fetchall()
            for i, (SNo,Song_Album_Name,Artist,Duration) in enumerate(records, start=1):
                tree.insert("", 'end', values=(SNo,Song_Album_Name,Artist,Duration))
            mysqldb.close()
        show_ta()
        sd.mainloop()
    Button(b,text="Search",command=display_ta).place(x=110,y=220)
    b.mainloop()
   
Button(dms,text="Search",command=display_s).place(x=320,y=5)
Button(dms,text="Artist",command=artist).place(x=120,y=250,height=100,width=170)
Button(dms,text="Tracks/Album",command=ta).place(x=470,y=250,height=100,width=170)
Button(dms,text="Show All Songs",command=display_sas).place(x=850,y=250,height=100,width=170)
dms.mainloop()