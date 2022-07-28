import tkinter as tk
win=tk.Tk()
win.geometry("600x600")
win.title("calculator")
win.config(bg="black")
def output():
    
        if ent.get() == "":
                pass
        elif ent.get()[0] == "0":
                ent.delete(0,"end")
        else:
                cs = ent.get()
                cs = eval(cs)
                clear()
                ent.insert("end",cs)
    
def clear():
        ent.delete(0,"end")    
def de():
        a = ent.get()
        ent.delete(first=len(a)-1,last="end")
ent=tk.Entry(win,width=25,text="Enter",font=("",25))
ent.place(x=0,y=0)
lnin=tk.Button(win,width=5,text="9",font=("",25),bg="red",command=lambda : ent.insert("end","9") )
leig=tk.Button(win,width=5,text="8",font=("",25),bg="red",command=lambda : ent.insert("end","8"),)

lsev=tk.Button(win,width=5,text="7",font=("",25),bg="red",command=lambda : ent.insert("end","7") )
lsix=tk.Button(win,width=5,text="6",font=("",25),bg="red",command=lambda : ent.insert("end","6"),)
lfiv=tk.Button(win,width=5,text="5",font=("",25),bg="red",command=lambda : ent.insert("end","5") )
lfou=tk.Button(win,width=5,text="4",font=("",25),bg="red",command=lambda : ent.insert("end","4") )
lthre=tk.Button(win,width=5,text="3",font=("",25),bg="red",command=lambda : ent.insert("end","3") )
ltwo=tk.Button(win,width=5,text="2",font=("",25),bg="red",command=lambda : ent.insert("end","2") )
lone=tk.Button(win,width=5,text="1",font=("",25),bg="red",command=lambda : ent.insert("end","1"))
lze=tk.Button(win,width=5,text="0",font=("",25),bg="red",command=lambda : ent.insert("end","0") )
lent=tk.Button(win,width=5,text="=",font=("",25),bg="blue",command=output)
lcut=tk.Button(win,width=5,text="del",font=("",25),bg="blue" ,command=de)
lcl=tk.Button(win,width=5,text="Clear",font=("",25),bg="blue" ,command=clear)

lmul=tk.Button(win,width=5,text="*",font=("",25),bg="green",command=lambda : ent.insert("end","*"),)
lsub=tk.Button(win,width=5,text="-",font=("",25),bg="green",command=lambda : ent.insert("end","-") )
ladd=tk.Button(win,width=5,text="+",font=("",25),bg="green",command=lambda : ent.insert("end","+"), )
ldiv=tk.Button(win,width=5,text="/",font=("",25),bg="green",command=lambda : ent.insert("end","/"),)


lnin.place(x=0,y=50)

lsix.place(x=0,y=110)
lthre.place(x=0,y=170)
leig.place(x=110,y=50)

lfiv.place(x=110,y=110)
ltwo.place(x=110,y=170)

lsev.place(x=220,y=50)

lfou.place(x=220,y=110)
lone.place(x=220,y=170)
lze.place(x=110,y=230)
lent.place(x=0,y=230)
lcut.place(x=220,y=230)
lmul.place(x=350,y=50)
lsub.place(x=350,y=110)
ladd.place(x=350,y=170)
ldiv.place(x=350,y=230)
lcl.place(x=480,y=0)
