# 1) Definir a variável da tabuada
# 2) Definir uma variável de contador - variar de 1 a 10
# 3) Criar um loop
# 4) multiplicar as variáveis e guardar o resultado
# 5) Mostrar o resultado
# 6) somar 1 ao valor do contador 

tabuada   = 2
contador  = 1
resultado = 0

while tabuada <= 10:
    resultado = tabuada * contador
    print(tabuada," x ",contador," = ",resultado)
    contador += 1
    if contador == 11:
       tabuada+=1
       contador=1