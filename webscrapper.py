import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import scrolledtext, messagebox

def scrape_website():
    url = url_entry.get() 

    try:
        response = requests.get(url)
        response.raise_for_status()  
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to retrieve data: {e}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')

    titles = soup.find_all('h2')

    if not titles:
        messagebox.showinfo("No Articles Found", "No <h2> tags found on this page.")
        return

    output_textbox.delete(1.0, tk.END) 
    for idx, title in enumerate(titles, start=1):
        output_textbox.insert(tk.END, f"{idx}. {title.get_text()}\n")

root = tk.Tk()
root.title("Web Scraper")
root.geometry("500x400")

tk.Label(root, text="Enter URL:").pack(pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.pack()

scrape_button = tk.Button(root, text="Scrape", command=scrape_website)
scrape_button.pack(pady=10)


output_textbox = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=15)
output_textbox.pack(pady=10)

root.mainloop()
