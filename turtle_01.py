import turtle as t
list_color = ['red', 'green', 'blue', 'yellow']
t.pensize(10)
t.shape('turtle')
for i in list_color:
    t.color(i)
    t.begin_fill()
    t.fd(100)
    t.lt(90)
    t.end_fill()

t.mainloop()