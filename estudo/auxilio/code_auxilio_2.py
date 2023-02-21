import tkinter as tk # Python 3
my_w = tk.Tk()
my_w.geometry("615x400") 
def my_callback(event):
     l1.config(text='Clicked at : '+ str(event.x) +","+ str(event.y))

l1=tk.Label(my_w,text='to Display',bg='yellow',font=('Times',26,'normal'))
l1.grid(row=0,column=1,padx=10,pady=10)

my_w.bind('<Button-1>',my_callback) # Mouse Left button  click <ButtonPress-1><1>

#my_w.bind('<Button-2>',my_callback) # Mouse middle button  click
#my_w.bind('<Button-3>',my_callback) # Mouse right button  click
#my_w.bind('<B1-Motion>',my_callback) # Mouse left button pressed move
#my_w.bind('<ButtonRelease-1>',my_callback) # Mouse left button  release
#my_w.bind('<Double-Button-1>',my_callback) # Mouse left button  Double click 
#l1.bind('<Enter>',lambda e:l1.config(text='Welcome')) # Mouse enters label 
#l1.bind('<Leave>',lambda e:l1.config(text='Thanks')) # Mouse leaves label 
#my_w.bind('<MouseWheel>',my_callback) # Mouse middle button  click
my_w.mainloop()