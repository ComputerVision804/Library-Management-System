import tkinter as tk
from tkinter import ttk
import itertools
import random
import threading
import speech_recognition as sr

class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎭 Cyberpunk Library System")
        self.root.geometry("600x500")

        self.bg_colors = itertools.cycle(["#0D0D0D", "#1A1A1A", "#262626", "#333333"])
        self.books = ["📕 Cybernetics", "📗 AI Uprising", "📘 The Matrix Decoded"]
        self.glitch_active = True  

        self.create_glitchy_login()
        self.animate_background()
        self.start_voice_recognition()

    def create_glitchy_login(self):
        """Create a login screen with glitching UI elements."""
        self.clear_screen()

        login_frame = tk.Frame(self.root, bg="#1A1A1A", width=600, height=500)
        login_frame.pack(fill=tk.BOTH, expand=True)

        title_label = ttk.Label(login_frame, text="💾 Cyber Library Login", font=("Courier", 16, "bold"), foreground="lime")
        title_label.pack(pady=20)

        ttk.Label(login_frame, text="Username:", foreground="white", background="#1A1A1A").pack()
        self.username_entry = ttk.Entry(login_frame)
        self.username_entry.pack()

        ttk.Label(login_frame, text="Password:", foreground="white", background="#1A1A1A").pack()
        self.password_entry = ttk.Entry(login_frame, show="*")
        self.password_entry.pack()

        login_button = ttk.Button(login_frame, text="🔓 Enter", command=self.create_main_screen)
        login_button.pack(pady=10)

        ttk.Button(login_frame, text="🎤 Voice Login", command=self.start_voice_recognition).pack(pady=5)
        ttk.Button(login_frame, text="🚪 Exit", command=self.root.quit).pack(pady=5)

    def create_main_screen(self):
        """Create the main cyberpunk dashboard."""
        self.clear_screen()

        main_frame = tk.Frame(self.root, bg="#0D0D0D", width=600, height=500)
        main_frame.pack(fill=tk.BOTH, expand=True)

        title_label = ttk.Label(main_frame, text="🚀 Cyberpunk Library", font=("Courier", 18, "bold"), foreground="lime")
        title_label.pack(pady=20)

        self.create_cyberpunk_menu(main_frame)

    def create_cyberpunk_menu(self, parent):
        """Create a cyberpunk-style menu with glitching buttons."""
        menu_frame = tk.Frame(parent, bg="#1A1A1A", highlightbackground="lime", highlightthickness=2)
        menu_frame.pack(pady=10)

        # Display book list
        self.book_listbox = tk.Listbox(menu_frame, bg="black", fg="lime", font=("Courier", 12), width=40, height=6)
        self.book_listbox.pack(pady=5)
        self.update_book_list()

        # Add Book Button
        add_button = ttk.Button(menu_frame, text="➕ Add Book", command=self.add_book_popup)
        add_button.pack(pady=5)

        # Logout Button
        logout_button = ttk.Button(menu_frame, text="🚀 Logout", command=self.create_glitchy_login)
        logout_button.pack(pady=5)

    def update_book_list(self):
        """Update the book list display."""
        self.book_listbox.delete(0, tk.END)
        for book in self.books:
            self.book_listbox.insert(tk.END, book)

    def add_book_popup(self):
        """Show a pop-up to add a book."""
        popup = tk.Toplevel(self.root)
        popup.geometry("300x150")
        popup.title("📖 Add Book")
        popup.configure(bg="black")

        ttk.Label(popup, text="Enter Book Name:", font=("Courier", 12), foreground="lime", background="black").pack(pady=10)
        book_entry = ttk.Entry(popup)
        book_entry.pack()

        def add_book():
            book_name = book_entry.get()
            if book_name:
                self.books.append(f"📘 {book_name}")  # Add new book
                self.update_book_list()
                popup.destroy()

        ttk.Button(popup, text="✅ Add", command=add_book).pack(pady=10)

    def animate_background(self):
        """Change the background color dynamically for a cyber effect."""
        new_color = next(self.bg_colors)
        self.root.configure(bg=new_color)
        self.root.after(1000, self.animate_background)

    def start_voice_recognition(self):
        """Start voice recognition for commands."""
        threading.Thread(target=self.recognize_voice, daemon=True).start()

    def recognize_voice(self):
        """Use AI-powered speech recognition to control the system."""
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("🎤 Listening... Say a command!")

            try:
                audio = recognizer.listen(source)
                command = recognizer.recognize_google(audio).lower()
                print(f"🎙️ You said: {command}")

                if "login" in command:
                    self.create_main_screen()
                elif "logout" in command:
                    self.create_glitchy_login()
                elif "add book" in command:
                    self.add_book_popup()
                elif "exit" in command:
                    self.root.quit()
                else:
                    print(f"❌ Unknown Command: {command}")

            except sr.UnknownValueError:
                print("❌ I didn't understand that!")
            except sr.RequestError:
                print("🔌 Error with voice recognition service!")

    def clear_screen(self):
        """Clear all widgets from the screen."""
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()
