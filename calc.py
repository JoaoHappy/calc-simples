def somar(number1, number2):
	return print("Resultado é: ", number1 + number2)

def subtrair(number1, number2):
	return print("Resultado é: ", number1 - number2)

def multiplica(number1, number2):
	return print("Resultado é: ", number1 * number2)

def dividir(number1, number2):
	return print("Resultado é: ", number1 / number2)

print('''
	Digite uma opção:
	+ somar
	- subtrair
	/ dividir
	* multiplica\n
	''')

option = str(input())

while True:
		
		if option == '+':
			try:
				number1 = int(input('Digite um numero '))
				number2 = int(input('Digite um numero '))
			except Exception:
				print("Digite um numero valido")
			else:
				somar(number1,number2)
		
		if option == '-':
			try:
				number1 = int(input('Digite um numero '))
				number2 = int(input('Digite um numero '))
			except Exception:
				print("Digite um numero valido")
			else:
				subtrair(number1,number2)
		
		if option == '*':
			try:
				number1 = int(input('Digite um numero '))
				number2 = int(input('Digite um numero '))
			except Exception:
				print("Digite um numero valido")
			else:
				multiplica(number1,number2)
		
		if option == '/':
			try:
				number1 = int(input('Digite um numero '))
				number2 = int(input('Digite um numero '))
			except Exception:
				print("Digite um numero valido")
			else:
				dividir(number1,number2)


