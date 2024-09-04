                ### FATORIAL ###

# numero = int(input("Digite um numeiro inteiro: "))

# if numero > 0:
#     fatorial = 1
#     for i in range(1, numero +1):
#         fatorial = fatorial * i
#     print(fatorial)


            ### ALEATORIO ###

# import random

# numero_aleatorio = random.randint(1,10)
# acertou = False
# while acertou == False:
#     chute = int(input("Digite um numero aleatório de 1 a 10: "))
#     if chute > numero_aleatorio:
#         print("Chute foi maior que o valor gerado.")
#     elif chute < numero_aleatorio:
#         print("Chute foi menor que o valor gerado.")
#     elif chute == numero_aleatorio:
#         acertou == True
#         print("Você acerto!!!")



            ### VELOCIDADE ####


# velocidade = int(input("Digita a velocidade atual: "))

# velocidade_maxima = 80

# if velocidade <= velocidade_maxima:
#     print("Você está no limite da via.")
# elif velocidade > velocidade_maxima and velocidade <= velocidade_maxima + 10:
#     print("Você levou multa leve.")
# elif velocidade > velocidade_maxima + 11 and velocidade <= velocidade_maxima + 20:
#     print("Você levou multa grave.")
# elif velocidade > velocidade_maxima + 20:
#     print("Você levou multa gravíssima.")

            ###FUNÇOES###

# def multas_caso_precise(velocidade, velocidade_maxima):

#     if velocidade <= velocidade_maxima:
#         print('Nao levou multa')

#     elif velocidade > velocidade_maxima and velocidade <= velocidade_maxima + 10:
#         print('Levou multa leve')

#     elif velocidade >= velocidade_maxima + 11 and velocidade <= velocidade_maxima + 20:
#         print('Levou multa grave')

#     elif velocidade > velocidade_maxima + 20:
#         print('Levou multa gravissima')

# multas_caso_precise(100,100)

#Para usar uma classe é necessário "Instanciar" ela.


# class Radar:
#     def __init__(self, velocidade_maxima, multa_leve,multa_grave, multa_gravissima):
#         self.velocidade_maxima = velocidade_maxima
#         self.multa_leve = multa_leve
#         self.multa_grave = multa_grave
#         self.multa_gravissima = multa_gravissima
# # A função deve exibir o valor da multa que será aplicadcda de acordo com o nivel.
#     def obter_valor_multa(self, nivel_multa):
#         if nivel_multa == 'multa leve':
#             print(f'O valor da multa leve é R${self.multa_leve}')
#         elif nivel_multa == 'multa grave':
#             print(f'O valor da multa grave é R${self.multa_grave}')
#         else:
#             print(f'O valor da multa gravissima é R${self.multa_gravissima}')

#     def calcular_multa(self, velodade):
#         if velodade <= self.velocidade_maxima:
#             print('Não levou multa')
#         elif velodade > self.velocidade_maxima and velodade <= self.velocidade_maxima + 10:
#             print('Levou multa leve')
#         elif velodade >= self.velocidade_maxima + 11 and velodade<= self.velocidade_maxima + 20:
#             print('Levou multa grave')
#         elif velodade > self.velocidade_maxima + 21:
#             print('Levou multa gravissima')

#     def aplicar_multa(self, nivel_multa):
#         if nivel_multa == 'multa leva':
#             print('Perdeu 3 pontos na carteira')
#         elif nivel_multa == 'multa grave':
#             print('Perdeu 5 pontos na carteira')
#         else:
#             print('Perdeu 7 pontos na carteira')

# radar1 = Radar(velocidade_maxima=100,multa_leve=180,multa_grave=550,multa_gravissima=1500)
# # radar1.obter_valor_multa('multa grave')
# # radar1.calcular_multa(200)
# radar1.aplicar_multa('multa grave')



class Artista():
  def __init__(self,nome_do_artista,genero_de_musica,albuns):
    self.nome_do_artista = nome_do_artista
    self.genero_de_musica = genero_de_musica
    self.albuns = albuns
    
  def adicionar_albuns(self,nome_album):
    self.albuns.append(nome_album)
    print(f'Foi adicionado um album chamado de {nome_album}')

  # Função de listar albuns
  def listar_albuns(self):
    for album in self.albuns:
      print(album)

artista1 = Artista('Artista 1','rock',['Album 1','Album 2','Album 3'])
artista1.adicionar_albuns('O melhor do rock!')
artista1.listar_albuns()