import customtkinter
from tkinter.colorchooser import askcolor

# Create the application window

app = customtkinter.CTk()
app.geometry('962x627')
app.configure(fg_color='#6300bd')

# Split window into frames
# Split it in the center of screen with heright 627 so it fills the entire half screen

Frame_1 = customtkinter.CTkLabel(app, text="", width=481, height=627)
Frame_1.place(x=0, y=0)
Frame_2 = customtkinter.CTkLabel(app, text="", width=481, height=627)
Frame_2.place(x=481, y=0)

# Change color line 1

def change_color_Line1():
    #global colors
    colors = askcolor(title="Tkinter Color Chooser")
    Frame_1.configure(fg_color=colors[1])
  
# Change color line 2

def change_color_Line2():
    #global color2
    color2 = askcolor(title="Tkinter Color Chooser")
    Frame_2.configure(fg_color=color2[1])
    
# Recolor the graph:

def Recolor():
    global colors, color2
    colors = askcolor(title="Tkinter Color Chooser")
    color2 = askcolor(title="Tkinter Color Chooser")
    import Recolor_graph
    Recolor_graph.new_graph()


# Create the Label

Heading = customtkinter.CTkLabel(app, text="Stock Prediction", fg_color='#e1a8ff', width=719, height=48, font=('Roboto', 36))
Heading.configure(text_color='#6d6dff')
Heading.place(x=115, y=25)

# Line 1 Button

Line_1 = customtkinter.CTkButton(app, text="Line 1", command=change_color_Line1, width=156, height=69, fg_color='#7d00f9', font=('Roboto', 23))
Line_1.configure(text_color='#e8d2ff')
Line_1.place(x=387, y=185)

# Line 2

Line_2 = customtkinter.CTkButton(app, text="Line 2", command=change_color_Line2, width=156, height=69, fg_color='#9200d6', font=('Roboto', 23))
Line_2.configure(text_color='#e8d2ff')
Line_2.place(x=387, y=410)

# recolor button

Recolor_button = customtkinter.CTkButton(app, text="Recolor graph", command=Recolor, width=156, height=69, font=('Roboto', 23))
Recolor_button.place(x=387, y=300)

# Run the mainloop

app.mainloop()
