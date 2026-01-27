import tkinter as tk

class Main:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Meeter")
        self.root.columnconfigure(0,weight=1)
        self.root.rowconfigure(0,weight=1)

        self.frame = tk.Frame(self.root)
        self.frame.columnconfigure(0,weight=1)
        self.frame.rowconfigure(0,weight=1)
        self.frame.columnconfigure(0, weight=0) # rooms
        self.frame.columnconfigure(1, weight=1) # chat
        self.frame.columnconfigure(2, weight=0) # send
        self.frame.rowconfigure(0, weight=1)    # chat row
        self.frame.rowconfigure(1, weight=0)    # input
    
        self.chat = tk.Text(self.frame)
        self.chat.see("end")
        self.chat.config(state="disabled")
        self.chat.configure(bg="#CCCCCC")

        self.user_config_btn = tk.Button(self.frame, text="user")
        self.user_config_btn.configure(width=10, bg="#5774a0",fg="#ffffff")

        self.input_msg = tk.Entry(self.frame)
        self.input_msg.bind("<Return>", lambda e: self.send_message())

        self.rooms = tk.Listbox(self.frame)
        self.rooms.configure(bg="#DDDDDD")

        self.chat_scrollbar = tk.Scrollbar(self.frame)
        self.rooms_scrollbar = tk.Scrollbar(self.frame)
        self.chat.config(yscrollcommand=self.chat_scrollbar.set)
        self.rooms.config(yscrollcommand=self.rooms_scrollbar.set)

    def run(self):
        self.frame.grid(sticky="nsew")
        self.chat_scrollbar.grid(row=0, column=2, sticky="nes")
        self.rooms_scrollbar.grid(row=0, column=0, sticky="nes")
        self.rooms.grid(row=0,column=0,sticky="nsw")
        self.chat.grid(row=0,column=1,sticky="nsew")
        self.input_msg.grid(row=1,column=1,sticky="nsew")
        self.user_config_btn.grid(row=1,column=0,sticky="new")

        self.root.mainloop()

Main().run()