import customtkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import Machine_learning
from matplotlib.figure import Figure
from matplotlib.backend_tools import ToolBase, ToolToggleBase

# Change the color

def color_changer():
    import Color_changer
    
# Create the drawn equations

def Draw_equations():
    Equation_chosen = combo.get()
    
    if Equation_chosen == 'Linear':
        import Linear_function

# Create the color Variables

Train_color = 'y'
Valid_color = 'r'
Prediction_color = 'b'

# Create the application window

app = customtkinter.CTk()
app.geometry('940x589')
app.configure(fg_color='#663399')

# Create a label

Heading = customtkinter.CTkLabel(app, text="Stock Prediction", fg_color='#be9edf', width=719, height=48, font=('Roboto', 36))
Heading.configure(text_color='#660cc0')
Heading.place(x=105, y=25)

# Embed the graph

fig = Figure(figsize= (5, 5), dpi=100)
plot1 = fig.add_subplot(111)
plot1.plot(Machine_learning.train['Close'], Train_color)
plot1.plot(Machine_learning.valid['Close'], Valid_color)
plot1.plot(Machine_learning.valid['Predictions'], Prediction_color)
plot1.legend(['Train', 'Validations', 'Predictions'], loc='lower right')

canvas = FigureCanvasTkAgg(fig, master=app)
canvas.draw()
canvas.get_tk_widget().place(x=50, y=150)

# Add a tool bar

toolbar = NavigationToolbar2Tk(canvas, app)
toolbar.update()
toolbar.place(x=50, y=653)

# Line customization button

Line_customization = customtkinter.CTkButton(app, command=color_changer, text="Line Customization", width=142, height=75, fg_color='#bec3fa', font=('Roboto', 16))
Line_customization.configure(text_color='#22277a')
Line_customization.place(x=460, y=500)

# Combobox

combo = customtkinter.StringVar()
Equations = ['Linear']
Equations_combo = customtkinter.CTkComboBox(app, variable=combo, state='readonly', values=Equations)
Equations_combo.place(x=600, y=435)

# Button for combobox

Equation_button = customtkinter.CTkButton(app, command=Draw_equations, text="Draw Trendline", width=142, height=75, fg_color='#bec3fa', font=('Roboto', 16))
Equation_button.configure(text_color='#22277a')
Equation_button.place(x=460, y=300)

# Draw trendline option

Trendline_label = customtkinter.CTkLabel(app, text="Draw a trendline: ", fg_color='#be9edf', width=50, height=50, font=('Roboto', 16))
Trendline_label.configure(text_color='#660cc0')
Trendline_label.place(x=460, y=425)

# Run the window

app.mainloop()
