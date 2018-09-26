from bs4 import BeautifulSoup
import requests
import re

def search(url):
	try:
		r = requests.get(url)
	except Exception as e:
		print("No connection")

for i in range(3):
	search("https://grupoglobo.admin.globoi.com")