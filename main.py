# import time
# from topnews import topStories
# from win10toast import ToastNotifier
#
# # fetch news items
# newsitems = topStories()
#
# # create ToastNotifier object
# toaster = ToastNotifier()
#
# for newsitem in newsitems:
#     # show notification on screen
#     toaster.show_toast(
#         newsitem['title'],
#         newsitem['description'],
#         duration=10
#     )
#
#     # short delay between notifications
#     time.sleep(15)
import time
from topnews import topStories
from win10toast import ToastNotifier

# Create toast notifier object
toaster = ToastNotifier()

# Fetch news items
newsitems = topStories()

for newsitem in newsitems:
    # Convert notification content to Unicode
    title = newsitem['title'].decode('utf-8')
    description = newsitem['description'].decode('utf-8')

    # Show notification
    toaster.show_toast(title, description, duration=10)

    # Short delay between notifications
    time.sleep(15)
