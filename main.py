import tkinter as tk
from tkinter import ttk

class Main:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Meeter")
        self.root.columnconfigure(0,weight=1)
        self.root.rowconfigure(0,weight=1)

        self.style = ttk.Style()

        self.frame = tk.Frame(self.root)
        self.frame.columnconfigure(0,weight=1)
        self.frame.rowconfigure(0,weight=1)
        self.frame.columnconfigure(0, weight=0) # rooms
        self.frame.columnconfigure(1, weight=1) # chat
        self.frame.columnconfigure(2, weight=0) # send
        self.frame.rowconfigure(0, weight=1)    # chat row
        self.frame.rowconfigure(1, weight=0)    # input
        self.frame.configure(bg="#444444")
    
        self.chat = tk.Text(self.frame)
        self.chat.see("end")
        self.chat.config(state="disabled")
        self.chat.configure(bg="#333333",fg="#ffffff")

        self.user_config_btn = tk.Button(self.frame, text="user", command=lambda: Main.show_user(self))
        self.user_config_btn.configure(width=10, bg="#1C3A4E",fg="#ffffff")

        self.input_msg = tk.Entry(self.frame)
        self.input_msg.bind("<Return>", lambda e: self.send_message())
        self.input_msg.configure(bg="#333333",fg="#ffffff")

        self.rooms = tk.Listbox(self.frame)
        self.rooms.configure(bg="#333333", fg="#ffffff")

        self.chat_scrollbar = ttk.Scrollbar(self.frame)
        self.rooms_scrollbar = ttk.Scrollbar(self.frame)
        self.style.theme_use("clam")  # "clam" supports colors
        self.style.configure(
            "Custom.Vertical.TScrollbar",
            troughcolor="#333333",  # background track color
            background="#333333",        # the slider color
            arrowcolor="#ffffff",       # arrows
            width=10                  # scrollbar width
        )
        self.chat.config(yscrollcommand=self.chat_scrollbar.set)
        self.rooms.config(yscrollcommand=self.rooms_scrollbar.set)

    def show_user(self):
        #if not logged in
        self.window_login = tk.Toplevel()
        self.login = tk.Entry(self.window_login)
        self.login.grid(row=1,column=0)

        self.password = tk.Entry(self.window_login)
        self.password.grid(row=2,column=0)

        self.btn_login = tk.Button(self.window_login, text="login")
        self.btn_login.grid(row=3,column=0)
        


        #if not logged in
        #register
    

    def run(self):
        self.frame.grid(sticky="nsew")
        self.chat_scrollbar.grid(row=0, column=2, sticky="nes", padx=2, pady=2)
        self.rooms_scrollbar.grid(row=0, column=0, sticky="nes", padx=2, pady=2)
        self.rooms.grid(row=0,column=0,sticky="nsw", padx=2, pady=2)
        self.chat.grid(row=0,column=1,sticky="nsew", padx=2, pady=2)
        self.input_msg.grid(row=1,column=1,sticky="nsew", padx=2, pady=2)
        self.user_config_btn.grid(row=1,column=0,sticky="new", padx=2, pady=2)

        self.root.mainloop()

Main().run()