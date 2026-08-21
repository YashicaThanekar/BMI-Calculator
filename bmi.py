from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("BMI Calculator")
root.geometry("700x600+440+100")
root.resizable(False,False)
root.configure(bg="gray13")
f1 = ("Georgia", 32, "bold","underline")
f2 = ("Georgia", 20, "normal")
f3 = ("Cambria", 15, "normal")
f4 = ("Cambria", 25, "normal")

label1 = Label(root,text="BMI Calculator",font=f1, bg="gray13", fg="cyan2")
label1.pack(pady=10)

label2 = Label(root,text="Enter your weight in ",font=f2, bg="gray13", fg="white")
label2.pack(pady=10)

off_img = PhotoImage(file="off_img.png")
on_img = PhotoImage(file="on_img.png")

c = IntVar()
c.set(1)

w1 = Radiobutton(root,text="Kilograms",font=f3, bg="gray13", fg="cyan2",variable=c, value=1,image=off_img,selectimage=on_img, indicatoron=False,borderwidth=0, compound="left",selectcolor="gray13")
w1.place(x=220,y=120)

w2 = Radiobutton(root,text="Pounds",font=f3, bg="gray13", fg="cyan2",variable=c, value=2,image=off_img,selectimage=on_img, indicatoron=False,borderwidth=0, compound="left",selectcolor="gray13")
w2.place(x=360,y=120)

weight = Entry(root,font=f3,highlightcolor="cyan2",highlightthickness=2)
weight.pack(pady=30)
    
label3 = Label(root,text="Enter your height in ",font=f2,bg="gray13", fg="white")
label3.pack(pady=10)

d = IntVar()
d.set(1)

h1 = Radiobutton(root,text="Meters",font=f3, bg="gray13", fg="cyan2",variable=d, value=1,image=off_img,selectimage=on_img, indicatoron=False,borderwidth=0, compound="left",selectcolor="gray13")
h1.place(x=220,y=270)

h2 = Radiobutton(root,text="Centimeters",font=f3, bg="gray13", fg="cyan2",variable=d, value=2,image=off_img,selectimage=on_img, indicatoron=False,borderwidth=0, compound="left",selectcolor="gray13")
h2.place(x=360,y=270)

height = Entry(root,font=f3,highlightcolor="cyan2",highlightthickness=2)
height.pack(pady=35)

def get_bmi():
    try:
        if weight.get() == "":
            ans.config(text="Weight cannot be empty",fg="red")
            weight.focus()
        elif height.get() == "":
            ans.config(text="Height cannot be empty",fg="red")
            height.focus()
        elif weight.get().isalpha():
            ans.config(text="Weight should be in numbers only",fg="red")
            weight.focus()
        elif height.get().isalpha():
            ans.config(text="Height should be in numbers only",fg="red")
            height.focus()
        elif float(weight.get()) <= 0:
            ans.config(text="Weight should be greater than 0",fg="red")
            weight.focus()
        elif float(height.get()) <= 0:
            ans.config(text="Height should be greater than 0",fg="red")
            height.focus()
        else:    
            w = float(weight.get())
            h = float(height.get())
            if c.get() == 2:
                w = w * 0.453592

            if d.get() == 2:
                h = h / 100
                
            bmi = w/(h*h)
            ans.config(text=f"Your BMI is : {bmi:.2f}",fg="cyan2")

    except Exception as e:
        messagebox.showerror("Invalid Input: ",e)

button = Button(root,text="Calculate BMI",font=f2,command=get_bmi,bg="cyan2", fg="gray13")
button.pack(pady=10)

ans = Label(root,text="",font=f4, bg="gray13", fg="cyan2")
ans.pack(pady=10)


root.mainloop()
