linha = 1
coluna = 1

while linha <= 10:
    while coluna <= 10:
        print("|", linha * coluna, end="\t") # \t é o responsável pelo "tabspace"; ao lê-lo, o interpretador insere um tab
        coluna += 1
    linha += 1
    print("|")
    coluna = 1

