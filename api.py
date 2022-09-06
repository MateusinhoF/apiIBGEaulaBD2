import requests 

paises = requests.get("https://servicodados.ibge.gov.br/api/v1/paises/BR|RU|IN|CN|ZA/indicadores/77850").json() 
paises = paises[0]['series']

listPaises = []

for pais in paises: 
    listPaises.append(pais)

bibliotecaTaxas = {}

for numPais in range(len(listPaises)):
    for numAnoValor in range(len(listPaises[numPais]['serie'])): 
        if None not in listPaises[numPais]['serie'][numAnoValor].values():
            for chave, valor in listPaises[numPais]['serie'][numAnoValor].items():
                bibliotecaTaxas.update({
                    listPaises[numPais]['pais']['nome']+' '+chave:valor
                })
        
bibliotecaTaxasOrdenado = {}

for paisAno in sorted(bibliotecaTaxas, key = bibliotecaTaxas.get, reverse=True):
    bibliotecaTaxasOrdenado.update({ paisAno: bibliotecaTaxas[paisAno] })

contador = 0
listPaisesOrdenados = list(bibliotecaTaxasOrdenado)
while contador < 10:
    print("Posição "+str(contador+1)+ " = "+listPaisesOrdenados[contador]+" com valor = "+bibliotecaTaxasOrdenado[listPaisesOrdenados[contador]])
    contador = contador + 1