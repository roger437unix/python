# Euler

from os import system

system('cls')

ref = True

while True:
	try:
		if ref == True:
			print()
			while True:
				n = float(input('Digite um número > 0: '))
				if n > 0:
					ref = not ref
					break

		qtd = int(input('\nQuantidade de repetições? '))

		print()
		for i in range(0, qtd, 1):
			e = (1 + 1/n) ** n
			print('%d\t%s' %(i+1, e))
			n += 1

		print()
		op = input('\nContinuar? [s/n]: ')
		if op != 's' and op != 'S' and op != 'sim' and op != 'Sim' and op != 'SIM' and \
		   op != 'y' and op != 'Y' and op != 'yes' and op != 'Yes' and op != 'YES':
		   break

		ref = not ref

	except ValueError:
		print('\nApenas números são aceitos.\n')
	except:
		print('\nErro Inesperado.\n')