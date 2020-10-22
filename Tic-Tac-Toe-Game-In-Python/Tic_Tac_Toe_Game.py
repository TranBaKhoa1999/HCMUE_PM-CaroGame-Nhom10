from tkinter import *
from tkinter import ttk
from tkinter import font
import tkinter as tk
import tkinter.messagebox
# from tkinter import font as tkFont

root=tk.Tk()
# style button
style = ttk.Style()
style.configure('TButton', background = 'purple', foreground = 'white',width=20 ,borderwidth=5, focusthickness=0, focuscolor='none',font = ('Sans','10','bold'))
style.map('TButton', background=[('active','purple')])
# end style button
# font style
myFont = font.Font(family = 'Helvetica', size = 20)
# end font style

root.title("Tic Tac Toe")
# helv36 = tkFont.Font(family='Helvetica', size=36, weight='bold')
#add Buttons
bu1=ttk.Button(root,text=' ')
bu1.pack()
bu1.grid(row=0,column=0,sticky='snew',ipadx=40,ipady=40)
bu1.config(command=lambda: ButtonClick(1))


bu2=ttk.Button(root,text=' ')
bu2.grid(row=0,column=1,sticky='snew',ipadx=40,ipady=40)
bu2.config(command=lambda: ButtonClick(2))

bu3=ttk.Button(root,text=' ')
bu3.grid(row=0,column=2,sticky='snew',ipadx=40,ipady=40)
bu3.config(command=lambda: ButtonClick(3))

bu4=ttk.Button(root,text=' ')
bu4.grid(row=1,column=0,sticky='snew',ipadx=40,ipady=40)
bu4.config(command=lambda: ButtonClick(4))

bu5=ttk.Button(root,text=' ')
bu5.grid(row=1,column=1,sticky='snew',ipadx=40,ipady=40)
bu5.config(command=lambda: ButtonClick(5))

bu6=ttk.Button(root,text=' ')
bu6.grid(row=1,column=2,sticky='snew',ipadx=40,ipady=40)
bu6.config(command=lambda: ButtonClick(6))

bu7=ttk.Button(root,text=' ')
bu7.grid(row=2,column=0,sticky='snew',ipadx=40,ipady=40)
bu7.config(command=lambda: ButtonClick(7))

bu8=ttk.Button(root,text=' ')
bu8.grid(row=2,column=1,sticky='snew',ipadx=40,ipady=40)
bu8.config(command=lambda: ButtonClick(8))

bu9=ttk.Button(root,text=' ')
bu9.grid(row=2,column=2,sticky='snew',ipadx=40,ipady=40)
bu9.config(command=lambda: ButtonClick(9))

# Text range
vsbotButton_text = tk.StringVar()
vsbotButton_text.set("Change Type To: Player vs Bot")

description_text = tk.StringVar()
description_text.set("You Are Fighting With Friend")

playerdetails_text =tk.StringVar()
playerdetails_text.set("    Player 1 is X\n\n    Player 2 is O")
# end text range
playerturn=ttk.Label(root,text="   Player 1 turn!  ",background='yellow3',font = ('Sans','13','bold'))
playerturn.grid(row=3,column=0,sticky='snew',ipadx=40,ipady=40)

playerdetails=ttk.Label(root,textvariable=playerdetails_text,background='cyan', font = ('Sans','15','italic'))
playerdetails.grid(row=3,column=2,sticky='snew',ipadx=40,ipady=40)

res=ttk.Button(root,text='Restart')
res.grid(row=3,column=1,sticky='snew',ipadx=40,ipady=40)
res.config(command=lambda: restartbutton())
 
vsbotButton=ttk.Button(root,textvariable=vsbotButton_text)
vsbotButton.grid(row=4,column=0,sticky='snew',ipadx=40,ipady=40)
vsbotButton.config(command=lambda: ChangeType())

description=ttk.Label(root,textvariable=description_text,background='green3', font = ('Sans','20','italic'),width=30)
description.grid(row=4,column=1,columnspan = 2,sticky='snew',ipadx=40,ipady=40)

PlayerTurn =1
b=0
IsWin=0
IsWithBot=0
def ChangeType():
  global PlayerTurn,b,IsWin
  restartbutton()
  if vsbotButton_text.get() =="Change Type To: Player vs Bot":
    vsbotButton_text.set("Change Type To: P vs P")
    description_text.set("You Are Fighting With Bot")
    playerdetails_text.set("    You is X\n\n    Bot is O")
  elif vsbotButton_text.get() =='Change Type To: P vs P':
    vsbotButton_text.set("Change Type To: Player vs Bot")
    description_text.set("You Are Fighting With Friend")
    playerdetails_text.set("    Player 1 is X\n\n    Player 2 is O")
def restartbutton():
    global PlayerTurn,b,IsWin
    PlayerTurn =1
    b=0
    IsWin=0
    playerturn['text']="   Player 1 turn!   "
    bu1['text']=' '
    bu2['text']=' '
    bu3['text']=' '
    bu4['text']=' '
    bu5['text']=' '
    bu6['text']=' '
    bu7['text']=' '
    bu8['text']=' '
    bu9['text']=' '
    bu1.state(['!disabled'])
    bu2.state(['!disabled'])
    bu3.state(['!disabled'])
    bu4.state(['!disabled'])
    bu5.state(['!disabled'])
    bu6.state(['!disabled'])
    bu7.state(['!disabled'])
    bu8.state(['!disabled'])
    bu9.state(['!disabled'])
    
#after getting result(win or loss or draw) disable button
def disableButton():
    bu1.state(['disabled'])
    bu2.state(['disabled'])
    bu3.state(['disabled'])
    bu4.state(['disabled'])
    bu5.state(['disabled'])
    bu6.state(['disabled'])
    bu7.state(['disabled'])
    bu8.state(['disabled'])
    bu9.state(['disabled'])


def ButtonClick(id):
    global PlayerTurn,b,IsWin
    print("ID:{}".format(id))

    #for player 1 turn
    if id==1 and bu1['text']==' ' and PlayerTurn==1:
        bu1['text']="X"
        PlayerTurn =0
        b+=1
    if id==2 and bu2['text']==' ' and PlayerTurn==1:
        bu2['text']="X"
        PlayerTurn =0
        b+=1
    if id==3 and bu3['text']==' ' and PlayerTurn==1:
        bu3['text']="X"
        PlayerTurn =0
        b+=1
    if id==4 and bu4['text']==' ' and PlayerTurn==1:
        bu4['text']="X"
        PlayerTurn =0
        b+=1
    if id==5 and bu5['text']==' ' and PlayerTurn==1:
        bu5['text']="X"
        PlayerTurn =0
        b+=1
    if id==6 and bu6['text']==' ' and PlayerTurn==1:
        bu6['text']="X"
        PlayerTurn =0
        b+=1
    if id==7 and bu7['text']==' ' and PlayerTurn==1:
        bu7['text']="X"
        PlayerTurn =0
        b+=1
    if id==8 and bu8['text']==' ' and PlayerTurn==1:
        bu8['text']="X"
        PlayerTurn =0
        b+=1
    if id==9 and bu9['text']==' ' and PlayerTurn==1:
        bu9['text']="X"
        PlayerTurn =0
        b+=1
    #for player 2 turn
    if id==1 and bu1['text']==' ' and PlayerTurn==0:
        bu1['text']="O"
        PlayerTurn =1
        b+=1
    if id==2 and bu2['text']==' ' and PlayerTurn==0:
        bu2['text']="O"
        PlayerTurn =1
        b+=1
    if id==3 and bu3['text']==' ' and PlayerTurn==0:
        bu3['text']="O"
        PlayerTurn =1
        b+=1
    if id==4 and bu4['text']==' ' and PlayerTurn==0:
        bu4['text']="O"
        PlayerTurn =1
        b+=1
    if id==5 and bu5['text']==' ' and PlayerTurn==0:
        bu5['text']="O"
        PlayerTurn =1
        b+=1
    if id==6 and bu6['text']==' ' and PlayerTurn==0:
        bu6['text']="O"
        PlayerTurn =1
        b+=1
    if id==7 and bu7['text']==' ' and PlayerTurn==0:
        bu7['text']="O"
        PlayerTurn =1
        b+=1
    if id==8 and bu8['text']==' ' and PlayerTurn==0:
        bu8['text']="O"
        PlayerTurn =1
        b+=1
    if id==9 and bu9['text']==' ' and PlayerTurn==0:
        bu9['text']="O"
        PlayerTurn =1
        b+=1
        
    #checking for winner   
    if( bu1['text']=='X' and bu2['text']=='X' and bu3['text']=='X' or
        bu4['text']=='X' and bu5['text']=='X' and bu6['text']=='X' or
        bu7['text']=='X' and bu8['text']=='X' and bu9['text']=='X' or
        bu1['text']=='X' and bu4['text']=='X' and bu7['text']=='X' or
        bu2['text']=='X' and bu5['text']=='X' and bu8['text']=='X' or
        bu3['text']=='X' and bu6['text']=='X' and bu9['text']=='X' or
        bu1['text']=='X' and bu5['text']=='X' and bu9['text']=='X' or
        bu3['text']=='X' and bu5['text']=='X' and bu7['text']=='X'):
            disableButton()
            IsWin=1
            tkinter.messagebox.showinfo("Tic Tac Toe","Winner is player 1")
    elif( bu1['text']=='O' and bu2['text']=='O' and bu3['text']=='O' or
        bu4['text']=='O' and bu5['text']=='O' and bu6['text']=='O' or
        bu7['text']=='O' and bu8['text']=='O' and bu9['text']=='O' or
        bu1['text']=='O' and bu4['text']=='O' and bu7['text']=='O' or
        bu2['text']=='O' and bu5['text']=='O' and bu8['text']=='O' or
        bu3['text']=='O' and bu6['text']=='O' and bu9['text']=='O' or
        bu1['text']=='O' and bu5['text']=='O' and bu9['text']=='O' or
        bu3['text']=='O' and bu5['text']=='O' and bu7['text']=='O'):
            disableButton()
            IsWin=1
            tkinter.messagebox.showinfo("Tic Tac Toe","Winner is player 2")
    elif b==9:
            disableButton()
            IsWin=1
            tkinter.messagebox.showinfo("Tic Tac Toe","Match is Draw.")

    if PlayerTurn ==1 and IsWin==0:
        playerturn['text']="   Player 1 turn!   "
    elif PlayerTurn ==0 and IsWin==0:
        playerturn['text']="   Player 2 turn!   "
            
root.mainloop()

