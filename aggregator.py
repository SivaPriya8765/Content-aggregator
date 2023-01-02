import urllib, os, requests, datetime, subprocess
from tkinter import *
import praw, pprint
import webbrowser
import feedparser
import datetime
import time

from nsetools import Nse

reddit = praw.Reddit(client_id='XXXXXXX',
                     client_secret='XXXXXXXXXXX',
                     grant_type_access='client_credentials',
                     user_agent='script/1.0')


class News:
    def Indian_News(self):

        newsfeed = feedparser.parse(
            "http://feeds.feedburner.com/ndtvnews-india-news"

        )
        print("Today's News: ")
        for i in range(0,20):
            entry = newsfeed.entries[i]
            print(entry.title)
            print(entry.summary)
            print("------News Link--------")
            print(entry.link)
            print("###########################################")
        print('-------------------------------------------------------------------------------------------------------')



class StockExchange:
    def nse_stock(self):
        nse = Nse()
        print("TOP GAINERS OF YESTERDAY")
        pprint.pprint(nse.get_top_gainers())
        print("###########################################")
        print("TOP LOSERS OF YESTERDAY")
        pprint.pprint(nse.get_top_losers())
        print("###########################################")
        print('-------------------------------------------------------------------------------------------------------')


class Main:
    def NewsToday(self):
        try:
            from googlesearch import search
        except ImportError:
            print("No module named 'google' found")



        def callback(url):
            webbrowser.open_new_tab(url)
            link = Label(win, text=a[l], font=('Helveticabold', 15), fg="blue", cursor="hand2")
            link.pack()
            link.bind("<Button-1>", lambda e:
                      callback(a[l]))
            e = datetime.datetime.now()
            print ("%s" % e)
            print ("%s/%s/%s" % (e.day, e.month, e.year))
            print ("Time:%s:%s:%s" % (e.hour, e.minute, e.second))
            end = time.time()
            print("𝐄𝐥𝐚𝐩𝐬𝐞𝐝 𝐓𝐢𝐦𝐞:")
            print(end - start)
            win.mainloop()
            
        start = time.time()
        print("Enter the Topic that you want to search:")
        query = input(" ")
        a = []
        for i, j in enumerate(search(query, tld="co.in", num=20, stop=30, pause=2)):
            a.append(j)
        for m,k in enumerate(range(i)):
            print(m,a[k])
        size = len(a)
        print("Enter '-1' to Exit")
        while 1:
            l = int(input("enter index of the link that you wish to open"))
            if l == -1:
                break
            print(a[l])
            win = Tk()
            win.geometry("750x250")
            callback(a[l])
        


        
        
News_object = News()

StockExchange_object = StockExchange()
Ob=Main()

News_object.Indian_News()


StockExchange_object.nse_stock()

Ob.NewsToday()
