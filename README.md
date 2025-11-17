<h1 align="center"> Medidas Tendencia Central e Variabilidade </h1>

<p align="center">
  <a HREF="#-integrantes">Contribuintes</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-tecnologias">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-projeto">Projeto</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</p>

### Contribuintes:
- Jhayne Henemam - [perfil](https://github.com/JhayneK)

## 🚀 Tecnologias

Esse projeto foi desenvolvido com as seguintes tecnologias:

- Git e Github
- Python
- Google Colabatory
- VSCode
  
## 💻 Projeto

#### 📊 Requisitos Iniciais: 

Este repositório apresenta cálculos estatísticos básicos aplicados em dois cenários:

1 - Uma confeitaria que mede o tempo de entrega (min) e a temperatura (°C) na chegada do produto.

2 - Um exercício simples usando as idades de seis amigos para demonstrar média, mediana, moda e amplitude.

Todos os cálculos são feitos em Python de forma simples e clara, incluindo a possibilidade de entrada manual via input().

## 🧁 Cenário 1 — Confeitaria

A confeitaria coleta:

- Tempo de entrega (min)
- Temperatura do produto (°C)

O objetivo é calcular:
- Média
- Mediana
- Moda
- Variância
- Desvio-padrão
- Amplitude
- Coeficiente de variação

✔ Código Python (entrada manual)
import statistics as stats

def coletar_dados():
    dados = input("Digite os valores separados por vírgula: ")
    return [float(x.strip()) for x in dados.split(",")]

def calcular_estatisticas(valores):
    media = stats.mean(valores)
    mediana = stats.median(valores)

    try:
        moda = stats.mode(valores)
    except:
        moda = "Sem moda (valores não se repetem)"

    variancia = stats.variance(valores)
    desvio_padrao = stats.stdev(valores)
    amplitude = max(valores) - min(valores)
    
    coef_var = (desvio_padrao / media) * 100

    return {
        "Média": media,
        "Mediana": mediana,
        "Moda": moda,
        "Variância": variancia,
        "Desvio-padrão": desvio_padrao,
        "Amplitude": amplitude,
        "Coeficiente de Variação (%)": coef_var
    }

print("\n🔢 Cálculo estatístico:")
valores = coletar_dados()
resultado = calcular_estatisticas(valores)

for chave, valor in resultado.items():
    print(f"{chave}: {valor}")


## 👥 Cenário 2 — Idades dos amigos

Dados:
25, 28, 30, 32, 35, 40

## 📌 Resultados esperados

Média: (25 + 28 + 30 + 32 + 35 + 40) / 6 = 31,67 

(25+28+30+32+35+40)/6=31,67

Mediana: Valores ordenados: 25, 28, 30, 32, 35, 40
Como são 6 valores, a mediana é a média entre o 3º e 4º: (30 + 32 ) / 2 = 31

(30+32)/2=31

Moda: Não existe moda, pois nenhum valor se repete.

Amplitude: 40 − 25 = 15

40−25=15

✔ Código Python do exercício das idades
idades = [25, 28, 30, 32, 35, 40]
print("Média:", stats.mean(idades))
print("Mediana:", stats.median(idades))

try:
    print("Moda:", stats.mode(idades))
except:
    print("Moda: Não existe (valores não se repetem)")

print("Amplitude:", max(idades) - min(idades))

## 📌 Conclusão

Este repositório demonstra como aplicar estatística básica usando Python de maneira simples, clara e adequada para estudantes, iniciantes e projetos acadêmicos.
Você pode reutilizar os scripts para qualquer conjunto de dados — basta inserir os valores desejados.

