import customtkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import Machine_learning
from matplotlib.figure import Figure
from matplotlib.backend_tools import ToolBase, ToolToggleBase

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
plot1.plot(Machine_learning.train['Close'])
plot1.plot(Machine_learning.valid[['Close', 'Predictions']])
plot1.legend(['Train', 'Validations', 'Predictions'], loc='lower right')

canvas = FigureCanvasTkAgg(fig, master=app)
canvas.draw()
canvas.get_tk_widget().place(x=50, y=150)

# Add a tool bar

toolbar = NavigationToolbar2Tk(canvas, app)
toolbar.update()
toolbar.place(x=50, y=653)

# Line customization button

Line_customization = customtkinter.CTkButton(app, text="Line Customization", width=142, height=75, fg_color='#bec3fa', font=('Roboto', 16))
Line_customization.configure(text_color='#22277a')
Line_customization.place(x=460, y=500)

# Run the window

app.mainloop()
