import tkinter as tk
from tkinter import messagebox
import sqlite3

# Create a database connection
def create_db():
    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Function to sign up a new user
def sign_up():
    username = entry_username.get()
    password = entry_password.get()
    
    if username and password:
        conn = sqlite3.connect('user_data.db')
        c = conn.cursor()
        
        # Check if the username already exists
        c.execute("SELECT * FROM users WHERE username=?", (username,))
        if c.fetchone():
            messagebox.showerror("Error", "Username already exists!")
        else:
            c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            messagebox.showinfo("Success", "User registered successfully!")
        
        conn.close()
    else:
        messagebox.showwarning("Input Error", "Both fields are required!")

def sign_in():
    username=entry_username.get()
    password=entry_password.get()
    if username and password:
        conn = sqlite3.connect('user_data.db')
        c= conn.cursor()

        c.execute("SELECT * FROM users WHERE username=? AND password=?" ,(username,password))
        if c.fetchone():
           messagebox.showinfo("Successfully, Signin")
        else:
           messagebox.showerror("Error, Username Or Password invalid")
        conn.close()
    else:
        messagebox.showwarning("Thukka", "Mula Password ra Usename ma euta milena tero")


# Tkinter GUI setup
root = tk.Tk()
root.title("Sign Up/Sign In")
root.geometry("600x600")


# Create sign up frame
frame_signup = tk.Frame(root)
frame_signin =tk.Frame(root)
# Entry fields for username and password
entry_username = tk.Entry(frame_signup, width=50)
entry_password = tk.Entry(frame_signup, width=50, show="*")

# Sign-up buttons and labels
label_username = tk.Label(frame_signup, text="Username:")
label_password = tk.Label(frame_signup, text="Password:")
button_signup = tk.Button(frame_signup, text="Sign Up", command=sign_up)

#Entry fiels for username and password in signin
entry_username_signin= tk.Entry(frame_signin, width=50)
entry_password_signin=tk.Entry(frame_signin, width=50, show="#")

#Sign-in buttons and labels
label_username_signin =tk.Label(frame_signin, text="Username:")
label_password_sigin =tk.Label(frame_signin, text="Password:")
button_signin = tk.Button(frame_signin,text="Sign In", command=sign_in)

def show_signup():
    frame_signin.pack_forget()
    frame_signup.pack(pady=30)

def show_signin():
    frame_signup.pack_forget()
    frame_signin.pack(pady=30)

show_signin()

# Layout for the SignUp page
label_username.grid(row=0, column=0, pady=10)
label_password.grid(row=1, column=0, pady=10)
entry_username.grid(row=0, column=1)
entry_password.grid(row=1, column=1)
button_signup.grid(row=2, columnspan=2, pady=10)

#Layout for SignIn page
label_username_signin.grid(row=0, column=0, pady=10)
label_password_sigin.grid(row=1, column=0, pady=10)
entry_username_signin.grid(row=0, column=1)
entry_password_signin.grid(row=1, column=1)
button_signin.grid(row=2, columnspan=2, pady=10)

# Pack the frame
button_to_signup = tk.Button(root,text="Don't have an account?, Signup", command=show_signup)
button_to_signin = tk.Button(root, text="You have an account?, Signin", command=show_signin)

button_to_signin.pack(side="bottom", padx=5, pady=5)
button_to_signup.pack(side="bottom", padx=5, pady=5)

# Initialize the database
create_db()

# Run the main application loop
root.mainloop()
