from tkinter import *

# TODO 1 create window
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)
window.minsize(width=300, height=150)

# TODO 2 create 6 components
# 6 components
# 1. Entry (1,0)
miles_input = Entry()
miles_input.config(width=15)
miles_input.grid(column=1, row=0)
# 2. Label (0,1)
equal_label = Label(text="is equal to", font=("Arial", 16, "normal"), padx=5, pady=5)
equal_label.grid(column=0, row=1)
# 3. Label (2,0)
miles_label = Label(text="Miles", font=("Arial", 16, "normal"), padx=5, pady=5)
miles_label.grid(column=2, row=0)
# 4. Label (1,1)
result_label = Label(font=("Arial", 16, "normal"), padx=5, pady=5)
result_label.grid(column=1, row=1)
# 5. Label (2,1)
km_label = Label(text="Km", font=("Arial", 16, "normal"), padx=5, pady=5)
km_label.grid(column=2, row=1)
# 6. Button (1,2)
def convert_mile_2_km():
    miles = float(miles_input.get())
    km = miles*1.60934
    result_label.config(text=f"{km}")

calculate_btn = Button(text="Calculate", font=("Arial", 16, "normal"), command= convert_mile_2_km, padx=5, pady=5)
calculate_btn.grid(column=1, row=2)




window.mainloop()
