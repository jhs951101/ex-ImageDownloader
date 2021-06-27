import urllib.request
import time
import ssl

targetUrl = "url"
ssl._create_default_https_context = ssl._create_unverified_context
urllib.request.urlretrieve(targetUrl, "test.jpg")
