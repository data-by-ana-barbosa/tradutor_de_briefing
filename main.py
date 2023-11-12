# Este script realiza a tradução de um arquivo de briefing de projeto de inglês para português.
# Ele verifica a conexão com a internet, lê o arquivo de entrada, traduz o conteúdo e escreve o resultado em um novo arquivo.


# --- IMPORTs
from googletrans import Translator
import urllib.request

# --- FUNCIONs
def check_internet_connection():
    try:
        urllib.request.urlopen('http://www.google.com', timeout=1)
        return True
    except Exception as e:
        print(f'Lamentamos, mas ocorreu um erro com a internet.Por favor contate o suporte com a seguinte chave: -{e}-')
        return False

# --- TESTE DE CONEXÃO
if check_internet_connection():
    text_EN = 'project_briefing_EN.txt'
    text_PT = 'project_briefing_PT.txt'
    tradutor = Translator()

# --- ETAPA 01: Leitura de arquivo
    try:
        with open(text_EN, 'r') as arq_EN:
            text_in_EN = arq_EN.read()
    except FileNotFoundError as fnfe:
        print(f'\nO arquivo {text_EN} não foi encontrado. Por favor, verifique o arquivo encontrado e tente novamente.\nCaso o erro persista, por favor contate o suporte com a seguinte chave: -{fnfe}-')
    except Exception as e:
        print(f'\nOcorreu um erro na leitura do arquivo {text_EN}\n Por favor contate o suporte com a seguinte chave: -{e}-')

# --- ETAPA 02: Tradução
    try:
        text_translate = tradutor.translate(text_in_EN, src='en', dest='pt').text
    except Exception as e:
        print(f'\nLamentamos, mas correu um erro na tradução.\nPor favor contate o suporte com a seguinte chave: -{e}-')

# --- ETAPA 03: Arquivo de saída
    with open(text_PT, 'w', encoding='utf8') as arq_PT:
        try:
            arq_PT.write(text_translate)
            print('\nTradução concluída com sucesso!')
        except Exception as e:
            print(f'\nOcorreu um erro ao escrever o arquivo de tradução.\nPor favor contate o suporte com a seguinte chave: -{e}-')
else:
    print('Verifique sua rede Wi-Fi ou dados móveis e tente novamente.')