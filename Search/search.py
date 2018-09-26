from bs4 import BeautifulSoup
import requests
import re

class Engine:

	def __init__(self, url, wordSearch, depth):
		self.url = url
		self.wordSearch = wordSearch
		self.depth = depth
		self.blackLink = []
		
	def searchPage(self):
		if self.url not in self.blackLink:
			links = []
			r = requests.get(self.url) # requests.get pega a response da url
			html_page = BeautifulSoup(r.text,'html.parser')# Analiza o html para a extração de dados
			pattern = re.compile(r'href="(.*?)"')#cria um pattern que pega todos os links da page
			for i in r.text.split(): #faz um for em todas as "linhas" do documento html
				if 'http' in i or 'https' in i:	#verifica se a linha contem http ou https
					links += pattern.findall(i) #adiciona o link à lista
			numLink = len(links)		
			print("Foram encontrados "+str(len(links))+" Links em "+self.url+":")
			#print(links)
			self.blackLink.append(self.url)
			word = html_page.text.find(self.wordSearch)
			wordS = html_page.text[word:word+len(self.wordSearch)]
			if len(wordS)>0 :
				print("A busca encontrou a palavra: "+wordS)
			else:
				print("Nada foi encontrado!")
			return links









engine = Engine("http://www.globo.com", "entretenimento", 1)
engine.searchPage()
