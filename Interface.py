#-*- coding utf-8 -*-

# ------------------ Projeto Atena -----------------------

# 	Autores: Estanislau Filho e José Antônio
# 	Ano: 2019
# 	Orientadora: Natália Batista
#	Instituição: CEFET-MG	
# 	Link github: https://github.com/EstanislauFilho/Atena

#	Script: Interface

# --------------------------------------------------------
import cv2
import pygame
import Variaveis as var

pygame.init()



pos_x = 740/2 
pos_y = 507/2
tamBotao = 10

pos_x_butao_igreja = 525
pos_y_butao_igreja = 311

pos_x_butao_teatro = 215
pos_y_butao_teatro = 40

pos_x_butao_museu = 293
pos_y_butao_museu = 469


tela = pygame.display.set_mode((740,507))
pygame.display.set_caption("Atena - Meta 2019")

inciar = True

img_background = pygame.image.load("/home/pi/Projetos/Atena/Imagens/mapa.png")


while inciar:
	tela.blit(img_background,(0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			inciar = False
		print(event)
	#fundo.fill(var.cor_branco)
	#pygame.draw.rect(tela, var.cor_preto, [pos_x, pos_y, tamBotao, tamBotao])

	pygame.draw.rect(tela, var.cor_azul, [pos_x_butao_igreja, pos_y_butao_igreja, tamBotao, tamBotao])

	pygame.draw.rect(tela, var.cor_vermelho, [pos_x_butao_teatro, pos_y_butao_teatro, tamBotao, tamBotao])

	pygame.draw.rect(tela, var.cor_verde, [pos_x_butao_museu, pos_y_butao_museu, tamBotao, tamBotao])
	
	pygame.display.update()

pygame.quit()


'''
def menu_texto():
	print(" ############################################### ")
	print(" #         *** Atena - META 2019 ***           # ")
	print(" #_____________________________________________# ")
	print(" #                                             # ")
	print(" #  Selecione um dos destinos:                 # ")
	print(" #  1 - Igreja                                 # ")      
	print(" #  2 - Teatro                                 # ")
	print(" #  3 - Museu                                  # ")
	print(" #_____________________________________________# ")
	print(" #                                             # ")
	print(" #  Digite:                                    # ")
	print(" #  4 - Sair                                   # ")
	print(" #                                             # ")
	print(" ###############################################\n ")
	opcao = int(input())
	return opcao



def confirma_opcao(op, nome):
	print(" ############################################### ")
	print(" #                                             # ")
	print(" #  Voce selecionou o destino: {0} - {1}       # ".format(op,nome))
	print(" #_____________________________________________# ")
	print(" #                                             # ")
	print(" #  Digite:                                    # ")
	print(" #        1 - Confirmar      2 - Voltar        # ")
	print(" #                                             # ")
	print(" ###############################################\n ")
	confirmacao_opcao = int(input())
	return confirmacao_opcao


def apresenta_tela(nome, imagem, pos_x, pos_y):
	cv2.namedWindow(nome, cv2.WINDOW_KEEPRATIO);
	cv2.moveWindow(nome, pos_x, pos_y);
	cv2.resizeWindow(nome, var.tam_mini_tela_x, var.tam_mini_tela_y)
	cv2.imshow(nome, imagem)

'''

