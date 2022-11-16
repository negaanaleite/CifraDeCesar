	# P R O J E T O - C I F R A DE C É S A R

# Em criptografia, a Cifra de César, também conhecida como cifra de troca, código de César ou troca de César, é uma das mais simples e conhecidas técnicas de criptografia. É um tipo de cifra de substituição na qual cada letra do texto é substituída por outra, que se apresenta no alfabeto abaixo dela um número fixo de vezes. Por exemplo, com uma troca de três posições, A seria substituído por D, B se tornaria E, e assim por diante. O nome do método é em homenagem a Júlio César, que o usou para se comunicar com os seus generais.[1]

# O processo de criptografia de uma cifra de César é frequentemente incorporado como parte de esquemas mais complexos, como a cifra de Vigenère, e continua tendo aplicações modernas, como no sistema ROT13. Como todas as cifras de substituição monoalfabéticas, a cifra de César é facilmente decifrada e na prática não oferece essencialmente nenhuma segurança na comunicação.[1]




alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(texto_inicial, quant_turno,direcao_cifra):
  texto_final = ""
  if direcao_cifra == "Código":
    quant_turno *= -1
  for char in texto_inicial:
			if char in alfabeto:
				lugar = alfabeto.index(char)
				novo_lugar = lugar + quant_turno
				texto_final += alfabeto[novo_lugar]
			else:
				texto_final += char
				print(f"Aqui esté o  {direcao_cifra} o resultado {texto_final}")

from art import logo
print(logo)

deveria_finalizar = False
while not deveria_finalizar:
	
	direcao = input("Digite 'encode' para criptografar, digite 'decode' para descriptografar:\n")
	texto = input("Digite sua mensagem:\n").lower()
	mudanca = int(input("Digite o número do turno:\n"))

	mudanca = mudanca % 26
	
	caesar(	texto_inicial = texto, quant_turno=mudanca, direcao_cifra = direcao)
	reiniciar = input("Digite 'sim' se quiser ir novamente. Caso contrário, digite 'não'.\n")
	if reiniciar == 'no':
		deveria_finalizar = True
		print("Adeus")