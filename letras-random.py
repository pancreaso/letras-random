import tkinter as tk
import random

class LetterPickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Letter Picker")

        self.letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.create_widgets()

    def create_widgets(self):
        # Label to display the letter
        self.letter_label = tk.Label(self.root, text="", font=("Helvetica", 48))
        self.letter_label.pack(pady=20)

        # Button to pick a random letter
        self.pick_button = tk.Button(self.root, text="Pick a Letter", command=self.pick_letter)
        self.pick_button.pack(pady=10)

        # Button to reset the letter list
        self.reset_button = tk.Button(self.root, text="Reset List", command=self.reset_list)
        self.reset_button.pack(pady=10)

    def pick_letter(self):
        if self.letters:
            letter = random.choice(self.letters)
            self.letter_label.config(text=letter)
            self.letters.remove(letter)
        else:
            self.letter_label.config(text="No more letters!")

    def reset_list(self):
        self.letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.letter_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = LetterPickerApp(root)
    root.mainloop()
