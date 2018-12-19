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