import datetime

AUTHOR = "Sahil Nilesh Sagwekar"
SITENAME = "Sahil's Blog"
SITEURL = "http://localhost:8000"

PATH = "content"

TIMEZONE = "Asia/Kolkata"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Theme setting
# THEME = "/home/sahil/Sahil/blog/Pelican/pelican-themes/pelican-haerwu-theme"

# THEME_SIDEBAR_ABOUT = "<p>Developer and X Poster</p>"

# THEME_SIDEBAR_LINKS = {
#         "GitHub" : "https://github.com/sahil-sagwekar2652",
#         "linkedin" : "https://www.linkedin.com/in/sahil-sagwekar-0b955b223/",
#         "twitter" : "https://twitter.com/sagwekar_sahil",
#         }


# Theme


THEME = "/home/sahil/Sahil/blog/Pelican/pelican-themes/MinimalXY"

# Theme customizations
# MINIMALXY_CUSTOM_CSS = 'static/custom.css'
# MINIMALXY_FAVICON = 'favicon.ico'
MINIMALXY_START_YEAR = 2023
MINIMALXY_CURRENT_YEAR = datetime.date.today().year

# Author
AUTHOR_INTRO = "Hello world! I’m Sahil Sagwekar."
AUTHOR_DESCRIPTION = "Hello world! I’m John Doe. Developer and FOSS enthusiast."
AUTHOR_AVATAR = "https://www.gravatar.com/avatar/14d6aae5677b0a937900e452ab55d29effa852d31e3fbf971e20a89112441559?s=240"
AUTHOR_WEB = "https://sahil-sagwekar2652.github.io"

# Services
# GOOGLE_ANALYTICS = "UA-12345678-9"
# DISQUS_SITENAME = "johndoe"

# Social
SOCIAL = (
    ("twitter", "http://twitter.com/sagwekar_sahil"),
    ("github", "https://github.com/sahil-sagwekar2652"),
    ("linkedin", "http://www.linkedin.com/in/sahil-sagwekar-0b955b223/"),
)

CATEGORIES_SAVE_AS = "categories.html"
ARCHIVES_SAVE_AS = "archives.html"

# Menu
MENUITEMS = (
    ("Categories", "/" + CATEGORIES_SAVE_AS),
    ("Archive", "/" + ARCHIVES_SAVE_AS),
)
