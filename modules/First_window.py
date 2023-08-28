from tkinter import *
import customtkinter
import sys
from playsound import playsound
from PIL import ImageTk, Image
import os
from pathlib import Path

def Window():
    # Quit button function

    def Quit():
        sys.exit()
        
    # Create the shawn function
    
    def Shawn():
        Path_audio = str(Path(os.getcwd()) / 'modules' / 'audio.mp3')
        playsound(Path_audio)
        
        win = Toplevel()
        
        win.geometry("900x800")
        
        frame = Frame(win, width=900, height=800)
        frame.pack()
        frame.place(anchor='center', relx=0.5, rely=0.5)
        
        image_file = str(Path(os.getcwd()) / 'modules' / 'Shawn.jpg')
        image1 = Image.open(image_file)
        resize_image = image1.resize((900, 800), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(resize_image)
        
        
        label = Label(frame, image=img)
        label.pack()
        
        win.mainloop()
    
    # The continue button function, it would redirect to another tkinter drawing

    def Continue():
        app.destroy()
        from After_first_window_design import draw
        import Second_window
        Second_window.app.mainloop()

    # Create the application window
    app = customtkinter.CTk()
    app.geometry("1008x592")
    app.configure(fg_color="#610094")

    # Create the main label
    Heading = customtkinter.CTkLabel(app, text="Stock Predicton", fg_color="#e1a8ff", width=719, height=48, font=('Roboto', 36))
    Heading.configure(text_color="#6d6dff")
    Heading.place(x=135, y=40)

    # Creating the instructions window area

    information = ("""
                This is a basic stock prediction program that would display the forecast of a stock.
                Once you proceed, the graph would appear as well as a legend for the lines.
                You also have the ability to reveal the additional lines if needed by clicking on the radio button.
                If you aren't happy with the color of the lines, you can customize them by clicking the button on the top right.
                """)

    InformationLabel = customtkinter.CTkLabel(app, text=information, width=776, height=240, font=('Roboto', 15))
    InformationLabel.configure(text_color="#f5e2ff")
    InformationLabel.place(x=75, y=120)

    # Creating the quit button

    Quit = customtkinter.CTkButton(app, text="Quit", command=Quit, width=142, height=75, fg_color="#aa7dce", font=('Roboto', 27))
    Quit.configure(text_color="#eee5f5")
    Quit.place(x=160, y=400)

    # Creating the proceed button

    Continue = customtkinter.CTkButton(app, text="Continue", command=Continue, width=142, height=75, fg_color="#a98bff", font=('Roboto', 27))
    Continue.configure(text_color="#000000")
    Continue.place(x=700, y=400)
    
    # Create the Shawn Button
    
    Shawn =  Continue = customtkinter.CTkButton(app, text="Shawn", command=Shawn, width=142, height=75, fg_color="#610094", font=('Roboto', 27))
    Shawn.configure(text_color='#610094')
    Shawn.place(x=400, y=400)

    # Run the application window
    app.mainloop()
Window()
