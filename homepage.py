from Tkinter import *

root =Tk()

can = Canvas(root,width=400, height=400)
can.pack()

line = can.create_line(100,100,100,175,fill="#005bbb")
line = can.create_line(100,175,125,200,fill="#005bbb")
line = can.create_line(125,200,175,200,fill="#005bbb")
line = can.create_line(175,200,200,175,fill="#005bbb")
line = can.create_line(200,175,200,100,fill="#005bbb")
line = can.create_line(150,150,150,250,fill="#005bbb")
line = can.create_line(150,150,240,150,fill="#005bbb")
line = can.create_line(240,150,250,160,fill="#005bbb")
line = can.create_line(250,160,250,190,fill="#005bbb")
line = can.create_line(250,190,240,200,fill="#005bbb")
line = can.create_line(240,200,175,200,fill="#005bbb")
line = can.create_line(240,200,250,210,fill="#005bbb")
line = can.create_line(250,210,250,240,fill="#005bbb")
line = can.create_line(250,240,240,250,fill="#005bbb")
line = can.create_line(240,250,150,250,fill="#005bbb")

button = Button(root,text="get started")
button.pack(side=RIGHT)

root.mainloop()
