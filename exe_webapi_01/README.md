# <h1>Web Api</h1>

<h2 align="center">ReceitaWS</h2>
<strong>https://receitaws.com.br/api</strong>
<p>O ReceitaWS provê uma API para recuperação de dados de empresas brasileiras através de seu CNPJ.</p>

<h3>Paramentro necessário</h3> 

# cnpj: 
- obrigatório, numérico, o CNPJ a ser pesquisado

# Uso:

```
url = 'https://www.receitaws.com.br/v1/cnpj/27865757000102'
response = requests.get(url).json()
```

# Retorno:

```
{
  "atividade_principal": [
    {
      "text": "Provedores de acesso às redes de comunicações",
      "code": "61.90-6-01"
    }
  ],
  "data_situacao": "18/10/2010",
  "complemento": "B",
  "nome": "JORGE MORGADO",
  "uf": "PI",
  "telefone": "(86) 3223-1508",
  "atividades_secundarias": [
    {
      "text": "Comércio varejista especializado de equipamentos e suprimentos de informática",
      "code": "47.51-2-01"
    },
    {
      "text": "Suporte técnico, manutenção e outros serviços em tecnologia da informação",
      "code": "62.09-1-00"
    },
    {
      "text": "Portais, provedores de conteúdo e outros serviços de informação na internet",
      "code": "63.19-4-00"
    }
  ],
  "qsa": [],
  "situacao": "ATIVA",
  "bairro": "PICARRA",
  "logradouro": "AV HIGINO CUNHA",
  "numero": "265",
  "cep": "64.015-120",
  "municipio": "TERESINA",
  "abertura": "18/10/2010",
  "natureza_juridica": "213-5 - Empresário (Individual)",
  "fantasia": "PORTAL PIAUI",
  "cnpj": "12.726.555/0001-02",
  "ultima_atualizacao": "2018-10-20T13:15:06.836Z",
  "status": "OK",
  "tipo": "MATRIZ",
  "email": "",
  "efr": "",
  "motivo_situacao": "",
  "situacao_especial": "",
  "data_situacao_especial": "",
  "capital_social": "20000.00",
  "extra": {},
  "billing": {
    "free": true,
    "database": true
  }
}
```

<h2 align="center">Pesquisa na Web do Bing</h2>

<strong>https://docs.microsoft.com/pt-br/azure/cognitive-services/bing-web-search/quickstarts/python</strong>

<h3>Paramentro necessário</h3>

- subscription_key

# Uso:

```
import requests

def search(search_term):
	search_url = "https://api.cognitive.microsoft.com/bing/v7.0/search"
	headers = {"Ocp-Apim-Subscription-Key" : "23eb988979b325301fdd5389f9b1283a"}
	params  = {"q": search_term, "textDecorations":True, "textFormat":"HTML"}
	response = requests.get(search_url, headers=headers, params=params)
	response.raise_for_status()
	return response.json()

```


# Retorno

```
{'queryContext': {'originalQuery': 'web api'}, 'rankingResponse': {'sidebar': {'items': [{'resultIndex': 0, 'answerType': 'Entities', 'value': {'id': 'https://api.cognitive.microsoft.com/api/v7/#Entities.0'}}]}, 'mainline': {'items': [{'resultIndex': 0, 'answerType': 'WebPages', 'value': {'id': 'https://api.cognitive.microsoft.com/api/v7/#WebPages.0'}}, {'resultIndex': 1, 'answerType': 'WebPages', 'value': {'id': 'https://api.cognitive.microsoft.com/api/v7/#WebPages.1'}}, {'resultIndex': 2, 'answerType': 'WebPages', 'value': {'id': 'https://api.cognitive.microsoft.com/api/v7/#WebPages.2'}}, {'resultIndex': 3, 'answerType': 'WebPages', 'value': {'id': 'https://api.cognitive.microsoft.com/api/v7/#WebPages.3'}}, {'resultIndex': 4, 'answerType': 'WebPages', 'value': {'id': 'https://api.cognitive.microsoft.com/api/v7/#WebPages.4'}}, {'resultIndex': 5, 'answerType': 'WebPages', 'value': {'id': 'https://api.cognitive.microsoft.com/api/v7/#WebPages.5'}}, {'resultIndex': 6, 'answerType': 'WebPages', 'value': {'id': 'https://api.cognitive.microsoft.com/api/v7/#WebPages.6'}}, {'resultIndex': 7, 'answerType': 'WebPages', 'value': {'id': 'https://api.cognitive.microsoft.com/api/v7/#WebPages.7'}}, {'resultIndex': 8, 'answerType': 'WebPages', 'value': {'id': 'https://api.cognitive.microsoft.com/api/v7/#WebPages.8'}}, {'resultIndex': 9, 'answerType': 'WebPages', 'value': {'id': 'https://api.cognitive.microsoft.com/api/v7/#WebPages.9'}}, ....

OMITIDO

....
[{'_type': 'ContractualRules/LicenseAttribution', 'targetPropertyName': 'description', 'mustBeCloseToContent': True, 'license': {'name': 'CC-BY-SA', 'url': 'http://creativecommons.org/licenses/by-sa/3.0/'}, 'licenseNotice': 'Texto sob licença CC-BY-SA'}, {'_type': 'ContractualRules/LinkAttribution', 'targetPropertyName': 'description', 'mustBeCloseToContent': True, 'url': 'http://pt.wikipedia.org/wiki/Web_API', 'text': 'Wikipedia'}], 'id': 'https://api.cognitive.microsoft.com/api/v7/#Entities.0'}]}}


```

<h2 align="center">Api do Blogger</h2>

<strong>https://developers.google.com/blogger/</strong>

<p>A API do Blogger v3 permite que aplicativos clientes visualizem e atualizem o conteúdo do Blogger. Seu aplicativo cliente pode usar a Blogger API v3 para criar novas postagens de blog, editar ou excluir postagens existentes e consultar postagens que correspondam a critérios específicos.</p>

<h3>Paramentro necessário</h3>

- subscription_key
- userId
- blogId
- postId

# Uso:

```
response = requests.get("https://www.googleapis.com/blogger/v3/blogs/6399595320426306682?key=AIzaSyCrPvGQRpzalfnr0x9GmiX0upc1eApi")
	return response.json()
```

# Retorno

```
{'locale': {'variant': '', 'language': 'pt', 'country': 'BR'}, 'updated': '2018-12-19T17:22:04-08:00', 'posts': {'totalItems': 49, 'selfLink': 'https://www.googleapis.com/blogger/v3/blogs/6399595320426306682/posts'}, 'selfLink': 'https://www.googleapis.com/blogger/v3/blogs/6399595320426306682', 'name': ' CURSOS DE INFORMÁTICA INFSOLUTION', 'url': 'http://novoscursosdeinformaticagratis.blogspot.com/', 'description': 'Cursos de Informática, Windows 7 (seven), Windows 8,  Office, Outlook, Word, Linux, Download de Linux, Open Office, LibreOffice, Vídeos, tutoriais e Cursos Grátis ', 'pages': {'totalItems': 0, 'selfLink': 'https://www.googleapis.com/blogger/v3/blogs/6399595320426306682/pages'}, 'published': '2013-06-01T10:32:15-07:00', 'kind': 'blogger#blog', 'id': '6399595320426306682'}

```

- Delete
```
response = requests.delete("https://www.googleapis.com/blogger/v3/blogs/6399595320426306682/posts/5799608212156026150",
		headers={'Authorization':''})
	return response.json()
```