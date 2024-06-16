import tkinter as tk

root = tk.Tk()
root.geometry("1200x800")
root.config(bg="black")


futurense = tk.Label(root, text="Futurense", fg="white", bg="black")
moto = tk.Label(root, text = "The Godfather of Talent", fg="white", bg="black")
name = tk.Label(root, text = "Welcome visitor", fg="white", bg="black")
grades = tk.Button(root, text = "Show Grades", fg="white", bg="black")
profile = tk.Button(root, text = "Show profile", fg="white", bg="black")
assignment = tk.Button(root, text = "Show Assignment", fg="white", bg="black")
attendance = tk.Button(root, text = "Show Attendance", fg="white", bg="black")
test = tk.Button(root, text = "Show Test", fg="white", bg="black")

futurense.config(font=("Arial", 40))
futurense.place(x = 150, y = 80)
moto.place(x = 150, y = 140)
name.place(x = 10, y = 170)
grades.place(x = 350, y = 250)
profile.place(x= 350, y = 650)
assignment.place(x = 800, y = 250)
attendance.place(x = 562, y = 424)
test.place(x = 800, y = 650)


root.mainloop()