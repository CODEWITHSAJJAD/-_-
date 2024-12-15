import tkinter as tk
from tkinter import ttk,scrolledtext
def FIBONACCI_GENERATOR(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return FIBONACCI_GENERATOR(num-1)+FIBONACCI_GENERATOR(num-2)
def generator():
    try:
        num= int(entry.get())
        if num>35:
            output_area.delete(1.0,tk.END)
            output_area.insert(tk.END,"Enter a valid number less than 35 to avoid delay")
            return
        result="Febonacci Sequence:\n"
        for i in range(num):
            result+=str(FIBONACCI_GENERATOR(i))+"\n"
        output_area.delete(1.0, tk.END)
        output_area.insert(tk.END,result)
    except ValueError:
        output_area.delete(1.0, tk.END)
        output_area.insert(tk.END, "Enter a valid number")
root=tk.Tk()
root.title("Febonacci Generator")
root.geometry("400x500")
frame=ttk.Frame(root,padding=10)
frame.pack(fill=tk.BOTH,expand=True)
tk.Label(frame,text="Enter a Number to Generate its Sequence:").pack(pady=5)
entry=tk.Entry(frame,width=20)
entry.pack(pady=5)
ttk.Button(frame,text="Generate",command=generator).pack(pady=10)
output_area=scrolledtext.ScrolledText(frame,width=40,height=20)
output_area.pack(pady=5,fill=tk.BOTH,expand=True)
root.mainloop()
