# notification_desktop
This is desktop notifier , for every 15 seconds we get a notification regarding trending news.
The project aims to display desktop notifications for top news stories using Python. It utilizes various libraries such as `requests`, `xml.etree.ElementTree`, and `win10toast` to fetch news headlines from an RSS feed and show them as toast notifications on the Windows desktop.

The main components of the project are as follows:

1. `topnews.py`: This module handles fetching the top news stories from an RSS feed and parsing the XML data to extract the relevant information. It provides a function called `topStories()` that returns a list of news items.

2. `main.py`: This is the main script where the desktop notifications are displayed. It imports the `topStories()` function from `topnews.py` and uses the `win10toast` library to show toast notifications on the Windows desktop. It fetches the news items, iterates through them, and displays a notification for each news item with a certain duration.

By running the `main.py` script, you should be able to see desktop notifications appearing at regular intervals, displaying the top news stories fetched from the RSS feed.

Please note that to make the project work, you might need to provide a valid RSS feed URL and a path to an icon image that will be used for the notification icons.
