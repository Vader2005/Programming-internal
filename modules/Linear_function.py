import customtkinter
import matplotlib.pyplot as plt
import Machine_learning
import pandas as pd
import matplotlib.dates as mdates

def draw():
    
    # Get the y values from entries
    
    y_1_new = y_1.get()
    y_2_new = y_2.get()
    
    # Validate the user input for y-values (closing prices)
    if not y_1_new.replace(".", "").isdigit() or not y_2_new.replace(".", "").isdigit():
        print("Invalid input for y-values. Please enter valid numbers.")
        return
    
    # Printing the values
    
    print("y_1_new:", y_1_new)
    print("y_2_new:", y_2_new)
    
    # Convert y values to float after valdation
    
    y_1_value = float(y_1_new)
    y_2_value = float(y_2_new)
    
    # Get corresponding values from Machine Learning
    
    x_1_value = Machine_learning.get_x_value(y_1_value)
    x_2_value = Machine_learning.get_x_value(y_2_value)
    
    print("The first x-value is:", x_1_value)
    print("The second x-value is", x_2_value)

    
    # Handles the error in case doesn't exist
    
    if x_1_value is None or x_2_value is None:
        print("Invalid closing price or closing price not found in the dataset.")

        
    # Put in the right form
    
    y_values = [y_1_value, y_2_value]
    x_values = [x_1_value, x_2_value]
    
    # Convert x values to datetime objects
    
    x_values_datetime = pd.to_datetime(x_values, format='%Y-%m-%d')
    
    print("The list of y values is: ", y_values)
    print("The list of x values is: ", x_values)
    
    plt.figure(figsize=(5, 4))
    plt.title("Machine learning")
    plt.xlabel('Date', fontsize=8)
    plt.ylabel('Closing price', fontsize=8)
    plt.plot(Machine_learning.train['Close']) # The training data
    plt.plot(Machine_learning.valid['Close'])
    plt.plot(Machine_learning.valid['Predictions'])
    plt.plot(x_values_datetime, y_values, marker='o', color='blue')
    plt.legend(['Train', 'Validations', 'Predictions'], loc='lower right')
    plt.xticks(rotation=45)
    plt.show()

app = customtkinter.CTk()
app.geometry('940x589')
app.configure(fg_color='#663399')

# Create the main label
Heading = customtkinter.CTkLabel(app, text="Linear Trendline", fg_color="#e1a8ff", width=719, height=48, font=('Roboto', 36))
Heading.configure(text_color="#6d6dff")
Heading.place(x=90, y=40)

# Create the starting x value label

y_1_label = customtkinter.CTkLabel(app, text="Enter your first y value here:", fg_color='#be9edf', width=300, height=48, font=('Roboto', 16))
y_1_label.configure(text_color='#660cc0')
y_1_label.place(x=30, y=225)

# Creating the Starting entry

y_1 = customtkinter.CTkEntry(app, placeholder_text="Enter your first y value here")
y_1.configure(width=100, height=100)
y_1.place(x=350, y=200)

# Create the ending x value label

y_2_label = customtkinter.CTkLabel(app, text="Enter your second y value here:", fg_color='#be9edf', width=300, height=48, font=('Roboto', 16))
y_2_label.configure(text_color='#660cc0')
y_2_label.place(x=30, y=350)

# Create the end x value entry

y_2 = customtkinter.CTkEntry(app, placeholder_text="Enter your second y value here")
y_2.configure(width=100, height=100)
y_2.place(x=350, y=325)

# Draw button

Equation_button = customtkinter.CTkButton(app, command=draw, text="Draw", width=142, height=75, fg_color='#bec3fa', font=('Roboto', 16))
Equation_button.configure(text_color='#22277a')
Equation_button.place(x=500, y=275)

app.mainloop()
