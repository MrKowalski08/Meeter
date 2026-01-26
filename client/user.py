import tkinter as tk

class User:
    def __init__(self,username,password_hash):
        self.username = username
        self.password_hash = password_hash
        self.pfp = None
        self.banner = None
        self.desc = ""
        self.ignore_list = set()
        self.block_list = set()