entrada = input().lower()
automato = {
    'A': {'b': 'B'},
    'B': {'a': 'B', 'b': 'D', 'c': 'C'},
    'C': {'a': 'B'},
    'D': {'b': 'A'}
}
estado = 'B'
fim = {'C'}
try:
    for letra in entrada:
        estado = automato[estado][letra]
    aceito  = True if(estado in fim) else False
except:
    aceito = False
if aceito:
    print("Aceito")
else:
    print("Rejeitado")