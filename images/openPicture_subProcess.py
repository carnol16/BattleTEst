# openPicture_subprocess.py
import tkinter as tk
from PIL import Image, ImageTk
import sys

"""print("SUBPROCESS STARTED")
print("Received path:", sys.argv[1])"""

def openIMG(path):
    root = tk.Tk()
    root.title("Current Location")

    pil = Image.open(path)
    tkimg = ImageTk.PhotoImage(pil)
    pil.close()  # Close PIL image to free memory

    label = tk.Label(root, image=tkimg)
    label.image = tkimg
    label.pack()

    root.mainloop()

if __name__ == "__main__":
    openIMG(sys.argv[1])

    
    


