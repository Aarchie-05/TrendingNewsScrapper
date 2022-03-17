# import modules
from tkinter import *
from gnewsclient import gnewsclient

# defined functions
def news():
    # news client object declaration
	client = gnewsclient.NewsClient(
		language=lang.get(), location=loc.get(), topic=top.get(), max_results=3)
    # Getting the news data
	news_list = client.get_news()
	result_title.set(news_list[0]["title"] + "\n" +
					news_list[1]["title"] + "\n" + news_list[2]["title"])


# tkinter object
master = Tk()
master.title("TRENDING NEWS")

# background set to grey
master.configure(bg='#E6E6FA')

# Variable Classes in tkinter
result_title = StringVar()
result_link = StringVar()

# Creating label for each information
# name using widget Label
Label(master, text="Choose language :", bg="#E6E6FA").grid(row=0, sticky=W)
Label(master, text="Choose Location :", bg="#E6E6FA").grid(row=1, sticky=W)
Label(master, text="Choose Topic :", bg="#E6E6FA").grid(row=2, sticky=W)


lang = Entry(master)
lang.grid(row=0, column=1)

loc = Entry(master)
loc.grid(row=1, column=1)

top = Entry(master)
top.grid(row=2, column=1)


# Creating label for class variable
# name using widget Entry
Label(master, text="", textvariable=result_title,
	bg="#E6E6FA").grid(row=3, column=1, sticky=W)

# creating a button using the widget
# Button to call the submit function
Button(master, text="SHOW", command=news, bg="white").grid(row=1, column=3)


mainloop()
