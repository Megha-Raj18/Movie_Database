from tkinter import *
from Movie_Backend import Movie_Directory_backend as backend

def get_row(event):
    try:
        global selected_row
        index=viewbox.curselection()[0]
        selected_row=viewbox.get(index)
        
        e1.delete(0,END)
        e1.insert(END,selected_row[1])
        e2.delete(0,END)
        e2.insert(END,selected_row[2])
        e3.delete(0,END)
        e3.insert(END,selected_row[3])
        e4.delete(0,END)
        e4.insert(END,selected_row[4])
        e5.delete(0,END)
        e5.insert(END,selected_row[5])
        
    except:
        pass
    
def display_button():
    viewbox.delete(0,END)
    for row in backend.view():
        viewbox.insert(END,row)
        
def search_button():
    viewbox.delete(0,END)
    for row in backend.search(movie_title_text.get(),director_text.get(),YOR_text.get(),category_text.get(),duration_text.get()):
        viewbox.insert(END,row)
        
def add_button():
    viewbox.delete(0,END)
    backend.insert(movie_title_text.get(),director_text.get(),int(YOR_text.get()),category_text.get(),int(duration_text.get()))
    viewbox.insert(END,"Successfully Added")
    
    
def delete_button():
    index=selected_row[0]
    backend.delete(index)
    viewbox.delete(0,END)
    viewbox.insert(END,"Successfully Deleted")
    
def update_button():
    backend.update(selected_row[0],movie_title_text.get(),director_text.get(),YOR_text.get(),category_text.get(),duration_text.get())
    viewbox.delete(0,END)
    viewbox.insert(END,"Successfully Updated")
window=Tk()

window.wm_title("Movie Directory")
l1=Label(window,text='Movie Title')
l1.grid(row=0,column=0)

l2=Label(window,text='Director')
l2.grid(row=1,column=0)

l3=Label(window,text='Year of Release')
l3.grid(row=2,column=0)

l4=Label(window,text='Category')
l4.grid(row=3,column=0)

l5=Label(window,text='Duration')
l5.grid(row=4,column=0)

movie_title_text=StringVar()
e1=Entry(window,textvariable=movie_title_text)
e1.grid(row=0,column=1)

director_text=StringVar()
e2=Entry(window,textvariable=director_text)
e2.grid(row=1,column=1)

YOR_text=StringVar()
e3=Entry(window,textvariable=YOR_text)
e3.grid(row=2,column=1)

category_text=StringVar()
e4=Entry(window,textvariable=category_text)
e4.grid(row=3,column=1)

duration_text=StringVar()
e5=Entry(window,textvariable=duration_text)
e5.grid(row=4,column=1)

viewbox=Listbox(window,height=10,width=50)
viewbox.grid(row=5,column=0,rowspan=6,columnspan=3)

scroll1=Scrollbar(window)
scroll1.grid(row=6,column=3,rowspan=4)

viewbox.config(yscrollcommand=scroll1.set)
scroll1.config(command=viewbox.yview)

viewbox.bind('<<ListboxSelect>>',get_row)

button1=Button(window,text="Display All",width=15,command=display_button)
button1.grid(row=5,column=4)

button2=Button(window,text="Search Movie",width=15,command=search_button)
button2.grid(row=6,column=4)

button3=Button(window,text="Add Movie",width=15,command=add_button)
button3.grid(row=7,column=4)

button4=Button(window,text="Update Selected",width=15,command=update_button)
button4.grid(row=8,column=4)

button5=Button(window,text="Delete Selected",width=15,command=delete_button)
button5.grid(row=9,column=4)

button6=Button(window,text="Exit",width=15,command=window.destroy)
button6.grid(row=10,column=4)

window.mainloop()
