# EXEMPLO IMPORTANDO ARQUIVO CSV
# Importamos a biblioteca statistics para calcular média, mediana, moda, etc.
import statistics

# Importamos o pandas para trabalhar com tabelas e arquivos (CSV, Excel).
import pandas as pd


# Esta função recebe uma lista de números e calcula
# as medidas de tendência central e variabilidade.
def calcular_medidas(lista_numeros):
    # Calcula a média (somatório dos valores dividido pela quantidade)
    media = statistics.mean(lista_numeros)
    
    # Calcula a mediana (valor que fica no meio quando a lista está ordenada)
    mediana = statistics.median(lista_numeros)
    
    # Tenta calcular a moda (valor que mais aparece)
    # Em alguns casos pode não existir moda única (por isso usamos try/except)
    try:
        moda = statistics.mode(lista_numeros)
    except statistics.StatisticsError:
        # Se não tiver uma moda clara, colocamos esse texto
        moda = "sem moda única"
    
    # Calcula o desvio-padrão populacional (o quão espalhados os dados estão da média)
    desvio_padrao = statistics.pstdev(lista_numeros)
    
    # Calcula a variância populacional (quadrado do desvio-padrão)
    variancia = statistics.pvariance(lista_numeros)
    
    # Calcula a amplitude (maior valor menos o menor valor)
    amplitude = max(lista_numeros) - min(lista_numeros)
    
    # Calcula o coeficiente de variação (CV = desvio padrão / média * 100)
    # Serve para medir a variabilidade relativa em porcentagem.
    if media != 0:
        coeficiente_variacao = (desvio_padrao / media) * 100
    else:
        coeficiente_variacao = float("nan")  # se a média for 0, evitamos dividir por zero
    
    # Retornamos todas as medidas em um dicionário (como se fosse uma “tabelinha”)
    return {
        "média": media,
        "mediana": mediana,
        "moda": moda,
        "desvio_padrão": desvio_padrao,
        "variância": variancia,
        "amplitude": amplitude,
        "coeficiente_variação_%": coeficiente_variacao
    }


# Esta função apenas imprime as medidas de forma bonita na tela.
def mostrar_resultados(nome_variavel, medidas):
    print(f"\n==== Medidas para {nome_variavel} ====")
    
    # O dicionário "medidas" tem chave -> valor (por exemplo "média": 35.2)
    # Percorremos cada item para imprimir.
    for nome, valor in medidas.items():
        # Se o valor for numérico (int ou float), formatamos com 2 casas decimais.
        if isinstance(valor, (int, float)):
            print(f"{nome.capitalize()}: {valor:.2f}")
        else:
            # Se não for número (por exemplo, o texto da moda), mostramos direto.
            print(f"{nome.capitalize()}: {valor}")




# EXEMPLO ENTRADA MANUAL PELO USUÁRIO
# Esta função lê os dados digitados pelo usuário.
def ler_lista_numeros(nome_variavel):
    print(f"\nDigite os valores de {nome_variavel} separados por espaço.")
    print("Exemplo: 30 35 40 32.5 28")
    
    # input() lê uma linha que o usuário digitar.
    texto = input("> ")
    
    # Quebramos o texto em partes, usando o espaço como separador.
    # Por exemplo, "30 35 40" vira ["30", "35", "40"].
    partes = texto.split()
    
    # Agora vamos transformar cada pedacinho em número (float).
    # Também trocamos vírgula por ponto, caso o usuário digite 32,5.
    lista_numeros = []
    for p in partes:
        p = p.replace(",", ".")   # troca vírgula por ponto
        numero = float(p)         # converte para número decimal (float)
        lista_numeros.append(numero)  # adiciona o número na lista
    
    # Devolvemos a lista pronta
    return lista_numeros


# Esta função executa toda a análise usando entrada manual.
def analise_manual():
    print("=== Análise com dados digitados manualmente ===")
    
    # Lê tempos de entrega digitados pelo usuário
    tempos = ler_lista_numeros("tempo de entrega (min)")
    
    # Lê temperaturas digitadas pelo usuário
    temperaturas = ler_lista_numeros("temperatura do produto (°C)")
    
    # Calcula as medidas para os tempos
    medidas_tempo = calcular_medidas(tempos)
    
    # Calcula as medidas para as temperaturas
    medidas_temp = calcular_medidas(temperaturas)
    
    # Mostra o resultado na tela
    mostrar_resultados("Tempo de entrega (min)", medidas_tempo)
    mostrar_resultados("Temperatura do produto (°C)", medidas_temp)


# Para rodar essa versão no Colab, execute depois:
# analise_manual()

#Chamando a função em outro chunck do colab
analise_manual()


# EXEMPLO DE UPLOAD DE CSV NO COLAB
# Essa importação é específica do Google Colab. Ela permite fazer upload de arquivos.
from google.colab import files

def ler_dados_de_arquivo():
    print("Faça o upload do arquivo com os dados (CSV ou Excel).")
    
    # Abre uma janela para selecionar o arquivo no seu computador.
    arquivos_enviados = files.upload()
    
    # Pega o nome do primeiro arquivo enviado.
    nome_arquivo = list(arquivos_enviados.keys())[0]
    print(f"\nArquivo recebido: {nome_arquivo}")
    
    # Verifica a extensão do arquivo para saber como ler.
    if nome_arquivo.lower().endswith(".csv"):
        # Lê arquivo CSV
        df = pd.read_csv(nome_arquivo)
    elif nome_arquivo.lower().endswith(".xlsx") or nome_arquivo.lower().endswith(".xls"):
        # Lê arquivo Excel
        df = pd.read_excel(nome_arquivo)
    else:
        print("Formato de arquivo não suportado. Use .csv, .xlsx ou .xls")
        return None, None  # devolve vazio se der problema
    
    # Mostra as primeiras linhas da tabela para o usuário conferir.
    print("\nPrévia dos dados (primeiras linhas):")
    display(df.head())
    
    # Mostra os nomes das colunas disponíveis.
    print("\nColunas encontradas no arquivo:")
    print(list(df.columns))
    
    # Agora pedimos para o usuário informar qual coluna é o tempo de entrega.
    print("\nDigite exatamente o nome da coluna de TEMPO de entrega (min):")
    nome_col_tempo = input("> ").strip()
    
    # E qual coluna é a temperatura do produto.
    print("Digite exatamente o nome da coluna de TEMPERATURA do produto (°C):")
    nome_col_temp = input("> ").strip()
    
    # Pegamos a coluna de tempo e tentamos converter para número.
    # errors='coerce' coloca NaN onde não conseguir converter.
    tempos = pd.to_numeric(df[nome_col_tempo], errors="coerce")
    temperaturas = pd.to_numeric(df[nome_col_temp], errors="coerce")
    
    # Removemos valores NaN (dados inválidos ou vazios)
    tempos = tempos.dropna()
    temperaturas = temperaturas.dropna()
    
    # Convertendo as séries do pandas para listas de Python.
    lista_tempos = tempos.tolist()
    lista_temperaturas = temperaturas.tolist()
    
    # Devolvemos as duas listas
    return lista_tempos, lista_temperaturas


def analise_por_arquivo():
    print("=== Análise com dados de arquivo (CSV/Excel) ===")
    
    # Lê os dados do arquivo
    tempos, temperaturas = ler_dados_de_arquivo()
    
    # Se deu problema e retornou None, encerramos.
    if tempos is None or temperaturas is None:
        print("Não foi possível ler os dados.")
        return
    
    # Calcula as medidas para tempos e temperaturas
    medidas_tempo = calcular_medidas(tempos)
    medidas_temp = calcular_medidas(temperaturas)
    
    # Mostra os resultados na tela
    mostrar_resultados("Tempo de entrega (min)", medidas_tempo)
    mostrar_resultados("Temperatura do produto (°C)", medidas_temp)


# Para rodar essa versão no Colab, execute depois:
# analise_por_arquivo()
# chamando a função no colab
analise_por_arquivo()

#===================================================== EXEMPLO 02 ==========================================================

# Lista com as idades dos amigos
idades = [25, 28, 30, 32, 35, 40]

# Mostrando a lista na tela, só para conferência
print("Idades dos amigos:", idades)

# MÉDIA: A média é a soma de todas as idades dividida pela quantidade de amigos.
# A função sum() soma todos os valores da lista
soma_idades = sum(idades)
# A função len() diz quantos elementos existem na lista
quantidade_amigos = len(idades)
# Média = A mediana é o valor que fica no meio quando os dados estão ordenados.
media = soma_idades / quantidade_amigos

print("Soma das idades:", soma_idades)
print("Quantidade de amigos:", quantidade_amigos)
print("Média das idades:", media)

# MEDIANA: A mediana é o valor que fica no meio quando os dados estão ordenados.

# Primeiro, garantimos que as idades estão em ordem crescente
idades_ordenadas = sorted(idades)
print("Idades ordenadas:", idades_ordenadas)

# Número de elementos na lista
n = len(idades_ordenadas)

# Como n é par (6), a mediana é a média dos dois valores centrais
# Em Python, o índice começa em 0
# Para n = 6:
# índices: 0  1  2  3  4  5
# valores: 25 28 30 32 35 40
# valores centrais são índices 2 e 3

indice_central_direita = n // 2       # 6 // 2 = 3
indice_central_esquerda = indice_central_direita - 1  # 3 - 1 = 2

valor_esquerda = idades_ordenadas[indice_central_esquerda]  # 30
valor_direita = idades_ordenadas[indice_central_direita]    # 32

mediana = (valor_esquerda + valor_direita) / 2

print("Valor central esquerdo:", valor_esquerda)
print("Valor central direito:", valor_direita)
print("Mediana das idades:", mediana)

# MODA: A moda é o valor que mais se repete.

# Vamos contar quantas vezes cada idade aparece
maior_frequencia = 0      # maior número de repetições encontrado até agora
moda = None               # valor que mais se repete (a moda)

for idade in idades:
    # count() conta quantas vezes 'idade' aparece na lista
    frequencia = idades.count(idade)
    
    # Se essa frequência for maior do que qualquer outra que vimos até agora,
    # atualizamos a moda.
    if frequencia > maior_frequencia:
        maior_frequencia = frequencia
        moda = idade

# Se a maior frequência for 1, significa que ninguém se repetiu
if maior_frequencia == 1:
    print("Não há moda: nenhuma idade se repete.")
else:
    print("Moda das idades:", moda, "- aparece", maior_frequencia, "vezes.")

#AMPLITUDE: A amplitude é a diferença entre o maior e o menor valor.

# AMPLITUDE

# max() devolve o maior valor da lista
maior_idade = max(idades)

# min() devolve o menor valor da lista
menor_idade = min(idades)

amplitude = maior_idade - menor_idade

print("Maior idade:", maior_idade)
print("Menor idade:", menor_idade)
print("Amplitude das idades:", amplitude)
