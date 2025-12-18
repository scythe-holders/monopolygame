import tkinter as tk

class guiImage:
    def __init__(self):
        self.root = tk.Tk()

        self.root.title("My first Gui")
        self.root.geometry("400x300")

        tk.Label(self.root, text="Email:").grid(row=1, column=0, padx=20, pady=5)

        self.ENT1 = tk.Entry(self.root)
        self.ENT1.grid(row=1, column=1, padx=20, pady=5)

        tk.Label(self.root, text="your phone number:").grid(row=2, column=0, padx=20, pady=5)

        self.ENT2 = tk.Entry(self.root)
        self.ENT2.grid(row=2, column=1, padx=20, pady=5)

        self.button = tk.Button(
            self.root,
            text="Get Data",
            command=self.get_value
        )
        self.button.grid(row=3, column=1, padx=20, pady=5)

        self.root.mainloop()

    def get_value(self):
        self.user_name = self.ENT1.get()
        self.user_Number = self.ENT2.get()

        print("Email:", self.user_name)
        print("Phone:", self.user_Number)


if __name__ == "__main__":
    s = guiImage()
