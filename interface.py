import tkinter
from PIL import Image, ImageTk

default_padx = 10
default_pady = 5

# Create a user interface using tkinter.
def create_user_interface():
    # Create a window.
    root = tkinter.Tk()
    root.title("Png to Asm Converter")
    root.geometry("480x260")
    root.iconbitmap("assets/chef.ico")

    frame = tkinter.Frame(root, borderwidth=14, bg="#EFEFEA")
    frame.pack(fill="both", expand=True)

    # Adding content to the frame
    logo = ImageTk.PhotoImage(Image.open("assets/chef.ico"))
    label = tkinter.Label(frame, image=logo)
    label.pack()

    settingsFrame = tkinter.LabelFrame(frame, text="Settings Panel", bg="#EFEFEA")
    settingsFrame.pack()

    # Add a button to frame
    convertButton = tkinter.Button(frame, text="Convert", command=())
    convertButton.pack(padx=5, pady=5)

    # Adding content to the settings Frame
    outputSettingsFrame = tkinter.LabelFrame(settingsFrame, text="Output", bg="#EFEFEA")
    outputSettingsFrame.grid(row=0, column=0, padx=default_padx, pady=default_pady)

    otherSettingsFrame = tkinter.LabelFrame(settingsFrame, text="Other", bg="#EFEFEA")
    otherSettingsFrame.grid(row=0, column=1, padx=default_padx, pady=default_pady)

    # Add content to the output frame
    outputLabel = tkinter.Label(outputSettingsFrame, text="Var name:")
    outputLabel.grid(row=0, column=0, padx=default_padx, pady=default_pady)

    outputEntry = tkinter.Text(outputSettingsFrame, width=10, height=1)
    outputEntry.grid(row=0, column=1, padx=default_padx, pady=default_pady)

    outputLabel = tkinter.Label(outputSettingsFrame, text="Var name:")
    outputLabel.grid(row=1, column=0, padx=default_padx, pady=default_pady)

    outputEntry = tkinter.Text(outputSettingsFrame, width=10, height=1)
    outputEntry.grid(row=1, column=1, padx=default_padx, pady=default_pady)

    # Add content to the other frame
    otherLabel = tkinter.Label(otherSettingsFrame, text="Var name:")
    otherLabel.grid(row=0, column=0, padx=default_padx, pady=default_pady)

    otherEntry = tkinter.Text(otherSettingsFrame, width=10, height=1)
    otherEntry.grid(row=0, column=1, padx=default_padx, pady=default_pady)

    otherLabel = tkinter.Label(otherSettingsFrame, text="Var name:")
    otherLabel.grid(row=1, column=0, padx=default_padx, pady=default_pady)

    otherEntry = tkinter.Text(otherSettingsFrame, width=10, height=1)
    otherEntry.grid(row=1, column=1, padx=default_padx, pady=default_pady)

    # Main Loop
    root.mainloop()


# Function to start the program.
def main():
    create_user_interface()

if __name__ == "__main__":
    main()