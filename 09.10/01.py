from tkinter import*

root=Tk()

e = Entry(root, width=200)
b = Button(root, text="Преобразовать")
l = Label(root, bg='black', fg='white', width=10)

def strToSortlist(event):
    s = e.get()
    s = e.split()
    s.sort()
    l['text'] = ' '.join(s)
    
b.bind('<Button-1>', strToSortlist)

e.pack(pady=10)
b.pack(pady=10)
l.pack(pady=10)
root.mainloop()
