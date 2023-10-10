import string
import random
import tkinter as tk

# Define the base URL for the shortened links
BASE_URL = "https://shrtlnk.com/"

# Define the length of the shortened link
LINK_LENGTH = 6

def generate_short_link():
    # Generate a random string of characters for the shortened link
    characters = string.ascii_lowercase + string.digits
    short_link = ''.join(random.choice(characters) for i in range(LINK_LENGTH))
    
    # Return the full shortened link with the base URL
    return BASE_URL + short_link

# Create a tkinter window
window = tk.Tk()
window.title("URL Shortener")

# Create a label for the URL input
url_label = tk.Label(window, text="Enter URL:")
url_label.pack()

# Create an entry field for the URL input
url_entry = tk.Entry(window)
url_entry.pack()

# Create a label for the shortened link output
short_label = tk.Label(window, text="Shortened Link:")
short_label.pack()

# Create a text field for the shortened link output
short_text = tk.Text(window, height=1)
short_text.pack()

def shorten_url():
    # Get the URL from the entry field
    url = url_entry.get()
    
    # Generate a shortened link and display it in the text field
    short_link = generate_short_link()
    short_text.delete(1.0, tk.END)
    short_text.insert(tk.END, short_link)

# Create a button to trigger the URL shortening process
shorten_button = tk.Button(window, text="Shorten URL", command=shorten_url)
shorten_button.pack()

# Start the tkinter event loop
window.mainloop()

