import pyshorteners
long_url = input("Enter the URL to shorten: ")

type_tiny = pyshorteners.Shortener()
short_url = type_tiny.tinyurl.short(long_url)

# Use bitly but you have account first
#type_bitly = pyshorteners.Shortener(api_key='YOUR_BITLY_API_KEY')
#short_url = type_bitly.bitly.short(long_url)

print("The Shortened URL is: " + short_url)
