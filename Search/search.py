from bs4 import BeautifulSoup
import requests
import re

class Engine:

	def __init__(self, wordSearch):
		self.wordSearch = wordSearch
		self.blackLink = []
		
	def searchPage(self, url):
		if url not in self.blackLink:
			links = []
			try:
				r = requests.get(url) # requests.get pega a response da url
			except Exception as e:
				print("Conection Error in "+url)
				r = None
			if r != None:		
				html_page = BeautifulSoup(r.text,'html.parser')# Analiza o html para a extração de dados
				pattern = re.compile(r'href="(.*?)"')#cria um pattern que pega todos os links da page
				for i in r.text.split(): #faz um for em todas as "linhas" do documento html
					if 'http' in i or 'https' in i:	#verifica se a linha contem http ou https
						links += pattern.findall(i) #adiciona o link à lista
				numLink = len(links)		
				print("Foram encontrados "+str(len(links))+" Links em "+url+":")
				#print(links)
				self.blackLink.append(url)
				word = html_page.text.find(self.wordSearch)
				wordS = html_page.text[word-10:word+len(self.wordSearch)+10]
				if len(wordS)>0 :
					print("A busca encontrou a palavra: "+wordS)
				else:
					print("Nada foi encontrado!")
				return links
			return []
					

	def engineSearch(self, urls,depth):
				lk = []
				if depth > 0:
					for i in urls:
						lk = self.searchPage(i)
					self.engineSearch(lk, depth-1)	
				else:
					print("END")







word = input("Digite o que você procura!\n")
link = input("Informe um link\n")
depth = int(input("Qual a profundidade?\n"))
engine = Engine( word)
engine.engineSearch([link],depth)
