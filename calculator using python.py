import tkinter

button_values = [
    ["AC", "+/-", "%", "+"],
    ["7", "8", "9", "-"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "/"],
    ["0", ".", "^", "="],
]

right_symbols = ["+", "-", "*", "/", "="]
top_symbols = ["AC", "+/-", "%"]

row_count = len(button_values)
column_count = len(button_values[0]) if button_values else 0

color_light_gray = "#D4D4D2"
color_black = "#1C1C1C"
color_dark_gray = "#505050"
color_orange = "#FF9500"
color_white = "#FFFFFF"

# window setup
window = tkinter.Tk()
window.title("Calculator")
window.resizable(False, False)

frame = tkinter.Frame(window, bg=color_light_gray)
label = tkinter.Label(frame, text="0", anchor=tkinter.E, bg=color_light_gray,
                      fg=color_black, padx=24, font=("Arial", 30),width=column_count)

label.grid(row=0, column=0, columnspan=column_count, sticky="we", pady=8)

for row in range(row_count):
    for column in range(column_count):
       value = button_values[row][column]
       button = tkinter.Button(frame, text=value, width=5, 
                               height=2, font=("Arial", 20),command=lambda value=value: button_click(value))
       if value in top_symbols:
           button.configure(bg=color_dark_gray, fg=color_white)
       elif value in right_symbols:
           button.configure(bg=color_orange, fg=color_white)
       else:
           button.configure(bg=color_dark_gray, fg=color_white)
       button.grid(row=row + 1, column=column, padx=2, pady=2)
frame.pack()

# A+B, and other operations will be handled in this function
A = "0"
operator = "none"
B = None

def clear_all():
    global A, B, operator
    A = "0"
    B = None
    operator = "none"
    
def remove_zero_decmimal(num):
        if num%1 == 0:
            num = int(num)
        return str(num)

def button_click(value):
    global right_symbols, top_symbols, label, A, B , operator
    if value in right_symbols:
        if value == "=":
            if A is not None and operator is not None:
                B = label["text"]
                numA = float(A)
                numB = float(B)
                
                if operator == "+":
                    label["text"] = remove_zero_decmimal(numA + numB)
                elif operator == "-":
                    label["text"] = remove_zero_decmimal(numA - numB)
                elif operator == "*":
                    label["text"] = remove_zero_decmimal(numA * numB)
                elif operator == "/":
                    if numB == 0:
                        label["text"] = "Error"
                    else:
                        label["text"] = remove_zero_decmimal(numA / numB)
                        
                        clear_all()

        elif value in "+-*/^":
            if operator == "none":
                A = label["text"]
                label["text"] = "0"
                B = "0"
                
                operator = value
            
    elif value in top_symbols:
        if value == "AC":
            clear_all()
            label["text"] = "0"
            
        elif value == "+/-":
            result = float(label["text"]) * -1
            label["text"] = remove_zero_decmimal(result)
            
        elif value == "%":
            result = float(label["text"]) / 100
            label["text"] = remove_zero_decmimal(result)
            
    else: # digits or .
        if value == "." :
            if value not in label["text"]:
                label["text"] += value
        elif value in "0123456789":
                if label["text"] == "0":
                    label["text"] = value
                else:
                    label["text"] += value

# centre in the screen
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width / 2) - (window_width / 2)
y = (screen_height / 2) - (window_height / 2)
window.geometry(f"{window_width}x{window_height}+{int(x)}+{int(y)}")

window.mainloop()