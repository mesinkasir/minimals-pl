# A Themes by Creativitas.dev
# https://creativitas.dev/
# Hire developer for your website project
# https://fiverr.com/creativitas/
# Buy Me A Coffee - https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=JVZVXBC4N9DAN
# Be A Sponsor for this project https://github.com/sponsors/mesinkasir
# Download our source code project https://www.hockeycomputindo.com/themes/


# SEO by creativitas https://fiverr.com/creativitas
AUTHOR = 'creativitas'
SITENAME = 'Minimalis Pelican Themes'
SITEURL = ""
FAVICON = '/static/images/pelican.png'
SITESUBTITLE = 'A minimalis themes for python pelican static site generator project'

# Change Header Area in here - themes by creativitas https://fiverr.com/creativitas
SITESLOGAN = 'Minimals'
SITE_INTRO = 'Clean Minimalist and SEO themes for Pelician Project'

# For change Navbar area - themes by creativitas https://fiverr.com/creativitas
MENUITEMS = (
    ("Home", "/"), # Your homepage
    ("Page", "/pages/static-page.html"), # Link on your static page
    ("Posts", "/archives.html"), # Link go to your archives paage
    ("Contact", "/pages/contact-us.html"), # create static page on pages folder and create contact for your contact page
)

# For change Footer area - themes by creativitas https://fiverr.com/creativitas
FOOTER_AREA = (
    ("Clean Minimalist Pelican Themes Project - Develope by Creativitas - https://creativitas.dev"),
    ("Hire developer on fiverr - https://fiverr.com/creativitas"),
)

# For change Pagination List Posts - themes by creativitas https://fiverr.com/creativitas
DEFAULT_PAGINATION = 4
# Configuration your site - themes by creativitas https://fiverr.com/creativitas
THEME = 'minimals' # a themes develope by https://creativitas.dev - Hire developer https://fiverr.com/creativitas
TIMEZONE = 'Asia/Jakarta'
DEFAULT_LANG = 'en'
PATH = "content"
PAGE_PATHS = ['pages']

# For your static assets folder
STATIC_PATHS = [
    'static',
    'static/images',
    'static/robots.txt',
    ]
EXTRA_PATH_METADATA = {
    "static/robots.txt": {"path": "robots.txt"},
}
# Setup bro
USE_FOLDER_AS_CATEGORY = True
DELETE_OUTPUT_DIRECTORY = False
OUTPUT_RETENTION = [".articles"]
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.5,
        "indexes": 0.5,
        "pages": 0.5
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly"
    }
}

# Thank you by using minimals pelician develope by creativitas - https://creativitas.dev/
# Hire Developer on Fiverr - https://fiverr.com/creativitas
# Download all source code project https://www.hockeycomputindo.com/themes/
# Buy Me A Coffee - https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=JVZVXBC4N9DAN
# Be A Sponsor for this project https://github.com/sponsors/mesinkasir