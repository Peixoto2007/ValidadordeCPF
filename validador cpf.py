"""Calculo do primeiro dígito do CPF"""
Cpf= (input("digite seu cpf"))
Cpf= Cpf.replace('.','')
Cpf= Cpf.replace('-','')
Cpf= Cpf[0:9]
cpf= []
multiplicacao= []
soma=[]
contagem = 10
for i in Cpf:
    
    print(i)
    cpf.append(int(i))
    if contagem >= 2:
        soma.append(int(i)*contagem)
        
    contagem -= 1
        

print(soma)
multiplicacao= ((sum(soma))*10)%11
print(multiplicacao)
if multiplicacao > 9:
    print("o primeiro digito verificador do seu cpf e : 0")
else:print(f"o primeiro digito verificador do seu cpf e : {multiplicacao}")


"""Calculo do segundo dígito do CPF"""
CPF=input('digite seu cpf : ')
CPF= CPF[:10]
print(CPF)
cpf= []
contador=11
for i in CPF:
    cpf.append(int(i)*contador)
    contador -=1
print(cpf)
somaa= sum(cpf)
somaa= ((somaa*10)%11)
print(somaa)
if somaa > 9:
    print('o resultado e 0')
else: print(f'o resultado {somaa}')
