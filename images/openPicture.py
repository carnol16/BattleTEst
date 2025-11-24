import tkinter as tk
from PIL import Image, ImageTk

def openIMG(imagePath=None):
    # Ensure a root exists
    root = tk._default_root
    if root is None:
        root = tk.Tk()
        root.withdraw()  # hide the root window

    # Create new Toplevel window
    window = tk.Toplevel(root)
    window.title("Current Location")

    try:
        pilImage = Image.open(imagePath)
    except FileNotFoundError:
        print(f"Shit Broke {imagePath}")
        window.destroy()
        return None

    tkImage = ImageTk.PhotoImage(pilImage)
    label = tk.Label(window, image=tkImage)
    label.image = tkImage  # keep reference
    label.pack(padx=10, pady=10)

    # Allow user to manually close
    #window.protocol("WM_DELETE_WINDOW", window.destroy)

    return window  # return the window reference


        
    
    


