import dotenv
import os

dotenv.load_dotenv()


USERNAME = os.getenv("USER")  # facebook email
PWD = os.getenv("PWD")  # facebook pwd
PAGE_URL = os.getenv(
    "PAGE_URL"
)  # facebook page url e.g https://www.facebook.com/etc/ (dont forget the / at end)
SCROLL_N = 20
# example: range(10) scrolls down 650+ images
