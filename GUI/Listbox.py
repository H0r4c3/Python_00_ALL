import tkinter as tk

root = tk.Tk()
root.geometry("500x500")  # Size of the window 

def selected_element():
    print(my_listbox.get(tk.ACTIVE))     # The selected element  
        
my_listbox = tk.Listbox(root, height=4)
my_listbox.grid(row=1,column=1) 
my_list=['PHP','Python','MySQL']
for element in my_list:
    my_listbox.insert(tk.END, element)

    
button1 = tk.Button(root, text='Show', width=10,bg='yellow',command=lambda: selected_element())
button1.grid(row=1,column=2) 

root.mainloop()  # Keep the window open
