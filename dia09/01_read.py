#%%
nome_arquivo = "historia.txt"

with open(nome_arquivo) as open_file:
    conteudo = open_file.read()
#ao sair do with, o arquivo fecha automaticamente

#abre o arquivo
open_file = open(nome_arquivo)

#processa os dados do arquivo
conteudo = open_file.read()
print(conteudo)

#fecha o arquivo
open_file.close()

