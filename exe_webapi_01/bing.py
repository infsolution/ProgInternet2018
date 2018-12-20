import requests
def receita():
	url = 'https://www.receitaws.com.br/v1/cnpj/27865757000102'
	response = requests.get(url).json()
	return response

#print(receita())

def search(search_term):
	search_url = "https://api.cognitive.microsoft.com/bing/v7.0/search"
	headers = {"Ocp-Apim-Subscription-Key" : "AIzaSyDF9QlWI3cSrLI34guh1_rZBQHy_OZyHFo"}
	params  = {"q": search_term, "textDecorations":True, "textFormat":"HTML"}
	response = requests.get(search_url, headers=headers, params=params)
	response.raise_for_status()
	return response.json()

#print(search("web api"))


def blogger():
	response = requests.get("https://www.googleapis.com/blogger/v3/blogs/6399595320426306682?key=AIzaSyCrPvGQR_Rpza-lfnr0xDGmiX0u7c1eApY")
	return response.json()

def delete_post():
	cliet_id = '540926209188-9ui0o9it4ic2dr22apv4v3u1q4hd9dpp.apps.googleusercontent.com'
	client_secret = 'asp-N8XnXR_3275OfhHrfh8'
	response = requests.delete("https://www.googleapis.com/blogger/v3/blogs/6399595320426306682/posts/5799608212156026150",
		headers={'Authorization':''})
	return response.json()

print(blogger())
#print(delete_post())