import random
import tkinter as tk
from tkinter import messagebox
import random
import tkinter as tk
from tkinter import messagebox


def load_jokes(file_path):
    """
    Load jokes from a file. Each line should have the format: setup?punchline
    """
    jokes = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if '?' in line:
                    setup, punchline = line.strip().split('?', 1)
                    jokes.append((setup + '?', punchline.strip()))
        return jokes
    except FileNotFoundError:
        messagebox.showerror("Error", "Joke file not found!")
        return []
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        return []


class JokeApp:
    def __init__(self, root, jokes):
        self.jokes = jokes
        self.current_joke = None

        # Configure the root window
        root.title("Joke Teller App")
        root.geometry("600x450")
        root.configure(bg="#CB9DF0")  # Main background color

        # Title label
        title_label = tk.Label(
            root,
            text="Welcome to the Joke Teller!",
            font=("Helvetica", 18, "bold"),
            bg="#CB9DF0",
            fg="#333",
        )
        title_label.pack(pady=10)

        # Unified joke frame with border
        joke_frame = tk.Frame(root, bg="#F0C1E1", relief="solid", bd=3)
        joke_frame.pack(pady=10, fill="both", padx=20)

        # Joke setup label
        self.setup_label = tk.Label(
            joke_frame,
            text="",
            font=("Arial", 14),
            bg="#F0C1E1",
            fg="#333",
            wraplength=500,
            justify="center",
            padx=10,
            pady=10,
        )
        self.setup_label.pack()

        # Punchline label
        self.punchline_label = tk.Label(
            joke_frame,
            text="",
            font=("Arial", 14, "italic"),
            bg="#F0C1E1",  # Matches joke frame's background
            fg="#444",
            wraplength=500,
            justify="center",
            padx=10,
            pady=10,
        )
        self.punchline_label.pack(pady=(10, 0))  # Add spacing between setup and punchline

        # Buttons frame
        buttons_frame = tk.Frame(root, bg="#CB9DF0")
        buttons_frame.pack(pady=10)

        # Buttons for actions
        self.show_punchline_btn = tk.Button(
            buttons_frame,
            text="Show Punchline",
            font=("Arial", 12),
            bg="#007BFF",
            fg="white",
            padx=15,
            pady=5,
            command=self.show_punchline,
        )
        self.show_punchline_btn.grid(row=0, column=0, padx=10)
        self.show_punchline_btn.config(state="disabled")

        self.next_joke_btn = tk.Button(
            buttons_frame,
            text="Next Joke",
            font=("Arial", 12),
            bg="#28A745",
            fg="white",
            padx=15,
            pady=5,
            command=self.next_joke,
        )
        self.next_joke_btn.grid(row=0, column=1, padx=10)

        self.quit_btn = tk.Button(
            buttons_frame,
            text="Quit",
            font=("Arial", 12),
            bg="#DC3545",
            fg="white",
            padx=15,
            pady=5,
            command=root.quit,
        )
        self.quit_btn.grid(row=0, column=2, padx=10)

        # Load the first joke
        self.next_joke()

    def next_joke(self):
        """
        Display the setup of a new joke and reset punchline.
        """
        if not self.jokes:
            self.setup_label.config(text="No jokes available.")
            self.punchline_label.config(text="")
            self.show_punchline_btn.config(state="disabled")
            return
        self.current_joke = random.choice(self.jokes)
        self.setup_label.config(text=self.current_joke[0])
        self.punchline_label.config(text="")  # Clear previous punchline
        self.show_punchline_btn.config(state="normal")

    def show_punchline(self):
        """
        Show the punchline of the current joke in the frame.
        """
        if self.current_joke:
            self.punchline_label.config(text=self.current_joke[1])
            self.show_punchline_btn.config(state="disabled")


def main():
    """
    Main entry point for the application.
    """
    jokes = load_jokes("randomJokes.txt")  # Replace with the path to your joke file
    root = tk.Tk()
    app = JokeApp(root, jokes)
    root.mainloop()


if __name__ == "__main__":
    main()


def load_jokes(file_path):
    """
    Load jokes from a file. Each line should have the format: setup?punchline
    """
    jokes = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if '?' in line:
                    setup, punchline = line.strip().split('?', 1)
                    jokes.append((setup + '?', punchline.strip()))
        return jokes
    except FileNotFoundError:
        messagebox.showerror("Error", "Joke file not found!")
        return []
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        return []


class JokeApp:
    def __init__(self, root, jokes):
        self.jokes = jokes
        self.current_joke = None

        # Configure the root window
        root.title("Joke Teller App")
        root.geometry("600x450")
        root.configure(bg="#CB9DF0")  # Main background color

        # Title label
        title_label = tk.Label(
            root,
            text="Welcome to the Joke Teller!",
            font=("Helvetica", 18, "bold"),
            bg="#CB9DF0",
            fg="#333",
        )
        title_label.pack(pady=10)

        # Unified joke frame with border
        joke_frame = tk.Frame(root, bg="#F0C1E1", relief="solid", bd=3)
        joke_frame.pack(pady=10, fill="both", padx=20)

        # Joke setup label
        self.setup_label = tk.Label(
            joke_frame,
            text="",
            font=("Arial", 14),
            bg="#F0C1E1",
            fg="#333",
            wraplength=500,
            justify="center",
            padx=10,
            pady=10,
        )
        self.setup_label.pack()

        # Punchline label
        self.punchline_label = tk.Label(
            joke_frame,
            text="",
            font=("Arial", 14, "italic"),
            bg="#F0C1E1",  # Matches joke frame's background
            fg="#444",
            wraplength=500,
            justify="center",
            padx=10,
            pady=10,
        )
        self.punchline_label.pack(pady=(10, 0))  # Add spacing between setup and punchline

        # Buttons frame
        buttons_frame = tk.Frame(root, bg="#CB9DF0")
        buttons_frame.pack(pady=10)

        # Buttons for actions
        self.show_punchline_btn = tk.Button(
            buttons_frame,
            text="Show Punchline",
            font=("Arial", 12),
            bg="#007BFF",
            fg="white",
            padx=15,
            pady=5,
            command=self.show_punchline,
        )
        self.show_punchline_btn.grid(row=0, column=0, padx=10)
        self.show_punchline_btn.config(state="disabled")

        self.next_joke_btn = tk.Button(
            buttons_frame,
            text="Next Joke",
            font=("Arial", 12),
            bg="#28A745",
            fg="white",
            padx=15,
            pady=5,
            command=self.next_joke,
        )
        self.next_joke_btn.grid(row=0, column=1, padx=10)

        self.quit_btn = tk.Button(
            buttons_frame,
            text="Quit",
            font=("Arial", 12),
            bg="#DC3545",
            fg="white",
            padx=15,
            pady=5,
            command=root.quit,
        )
        self.quit_btn.grid(row=0, column=2, padx=10)

        # Load the first joke
        self.next_joke()

    def next_joke(self):
        """
        Display the setup of a new joke and reset punchline.
        """
        if not self.jokes:
            self.setup_label.config(text="No jokes available.")
            self.punchline_label.config(text="")
            self.show_punchline_btn.config(state="disabled")
            return
        self.current_joke = random.choice(self.jokes)
        self.setup_label.config(text=self.current_joke[0])
        self.punchline_label.config(text="")  # Clear previous punchline
        self.show_punchline_btn.config(state="normal")

    def show_punchline(self):
        """
        Show the punchline of the current joke in the frame.
        """
        if self.current_joke:
            self.punchline_label.config(text=self.current_joke[1])
            self.show_punchline_btn.config(state="disabled")


def main():
    """
    Main entry point for the application.
    """
    jokes = load_jokes("randomJokes.txt")  # Replace with the path to your joke file
    root = tk.Tk()
    app = JokeApp(root, jokes)
    root.mainloop()


if __name__ == "__main__":
    main()
