import tkinter as tk
import requests
import datetime
import webbrowser

USERNAME = "***********"
TOKEN = "***********"
GRAPH_ID = "***********"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"

class PixelaApp:
    def __init__(self, master):
        self.master = master
        master.title("Pixela App")

        # Create a label for the pages read entry field
        self.label1 = tk.Label(master, text="Pages read:")
        self.label1.pack()

        # Create an entry field for the user to enter the number of pages read
        self.entry1 = tk.Entry(master)
        self.entry1.pack()

        # Create a label for the date entry field
        self.label2 = tk.Label(master, text="Date (yyyymmdd):")
        self.label2.pack()

        # Create an entry field for the user to enter the date
        self.entry2 = tk.Entry(master)
        self.entry2.pack()

        # Create a button to use the current date
        self.button1 = tk.Button(master, text="Use current date", command=self.use_current_date)
        self.button1.pack()

        # Create a button to submit the entry
        self.button2 = tk.Button(master, text="Submit", command=self.submit)
        self.button2.pack()

        # Create a button to open the graph URL
        self.button3 = tk.Button(master, text="Open graph URL", command=self.open_graph_url)
        self.button3.pack()

    def use_current_date(self):
        # Set the date entry field to today's date
        today = datetime.datetime.now().strftime("%Y%m%d")
        self.entry2.delete(0, tk.END)
        self.entry2.insert(0, today)

    def submit(self):
        # Get the date entered in the date entry field
        date = self.entry2.get()

        # Get today's date in the correct format
        today = datetime.datetime.now().strftime("%Y%m%d")

        # Use today's date if the date entry field is empty
        if not date:
            date = today

        # Get the value entered in the pages read entry field
        pages_read = self.entry1.get()

        # Update the pixel for the given date
        pixel_data = {
            "quantity": pages_read,
        }

        pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{date}"
        headers = {
            "X-USER-TOKEN": TOKEN,
        }
        response = requests.put(url=pixel_endpoint, json=pixel_data, headers=headers)
        print(response.text)

        # Clear the entry fields after submitting
        self.entry1.delete(0, tk.END)
        self.entry2.delete(0, tk.END)

    def open_graph_url(self):
        # Open the graph URL in a web browser
        url = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}.html"
        webbrowser.open(url)


if __name__ == '__main__':
    root = tk.Tk()
    app = PixelaApp(root)
    root.mainloop()
