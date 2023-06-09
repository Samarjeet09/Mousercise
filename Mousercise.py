import customtkinter as ct
import pyautogui
# global
running = False
timeBtwEachMovement = 5000
# functions


def move_mouse():
    if running:
        pyautogui.moveTo(590, 400, duration=1)
        pyautogui.moveTo(690, 420, duration=1)
    app.after(timeBtwEachMovement, move_mouse)


def on_start():
    global running
    running = True
    startBtn.configure(fg_color ='red')
    


def on_stop():
    global running
    running = False
    startBtn.configure(fg_color ='blue')


# sys settings
ct.set_appearance_mode("System")
ct.set_default_color_theme('green')

# our app frame
app = ct.CTk()
app.geometry('150x160')
app.title('Always Online')


startBtn = ct.CTkButton(app, text="Start", command=on_start,fg_color='blue')
startBtn.pack(padx=10, pady=20)
stopBtn = ct.CTkButton(app, text="Stop", command=on_stop)
stopBtn.pack(padx=10, pady=10)


# run a function after said time
app.after(timeBtwEachMovement, move_mouse)

# running the app inside the loop
app.mainloop()
