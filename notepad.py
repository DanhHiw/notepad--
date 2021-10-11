from tkinter import *
cal=Tk()
cal.title("NotePad --")
operator=""
text_Input=StringVar()
txtDispaly=Entry(cal,width=80,font=('arial',18,'bold'),textvariable=text_Input,bd=10,insertwidth=3,bg='white',justify='left').grid(columnspan=5)
bt1=Button(cal,padx=90,bd=8,fg="black",font=('arial',18,'bold'),text="save file",bg="silver").grid(row=1,column=2)
bt2=Button(cal,padx=0,bd=8,fg="black",font=('arial',18,'bold'),text="more...",bg="silver").grid(row=1,column=4)
cal.mainloop()