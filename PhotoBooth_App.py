import cv2
import tkinter as tk 
from tkinter import Label, Button
from PIL import Image, ImageTk
import time
import os


os.makedirs("photo", exist_ok=True)

class PhotoBooth_App:
    def __init__(self, window):
        self.window = window
        self.window.title("Python Photo Booth")
        
        self.video_capture = cv2.VideoCapture(0)
        
        self.label = Label(window)
        self.label.pack()
        
        self.capture_button = Button(window, text="Take photo", command=self.take_photo)
        self.capture_button.pack()
        
        self.update_frame()
        
    def update_frame(self):i
        ret, frame = self.video_capture.read()
        if ret:
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image = img)
            self.label.imgtk = imgtk
            self.label.configure(image = imgtk)
        self.window.after(10, self.update_frame)

    def take_photo(self):
        ret, frame = self.video_capture.read()
        if ret:
            filename = f"photos/photo_{int(time.time())}.jpg"
            cv2.imwrite(filename, frame)
            print(f"Photo saved to {filename}")
        
    def __del__(self):
        self.video_capture.release()
    
    
if __name__ == '__main__':
    root = tk.Tk()
    app = PhotoBooth_App(root)
    root.mainloop()               