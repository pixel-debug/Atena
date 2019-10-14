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


tela = pygame.display.set_mode((var.tamTela_X_Interface, var.tamTela_Y_Interface))
pygame.display.set_caption("Atena - Meta 2019")

inciar = True

img_background = pygame.image.load("/home/pi/Projetos/Atena/Imagens/mapa.png")

clock = pygame.time.Clock()

while inciar:
	tela.blit(img_background,(0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			inciar = False
		#print(event)
	
	
	mouse = pygame.mouse.get_pos()
	print(mouse)

	# Teatro
	if var.pos_x_butao_teatro + var.tamBotao > mouse[0] > var.pos_x_butao_teatro and var.pos_y_butao_teatro + var.tamBotao > mouse[1] > var.pos_y_butao_teatro:
		pygame.draw.rect(tela, var.cor_azul_fraco, (var.pos_x_butao_teatro, var.pos_y_butao_teatro, var.tamBotao, var.tamBotao))
	else:
		pygame.draw.rect(tela, var.cor_azul, (var.pos_x_butao_teatro, var.pos_y_butao_teatro, var.tamBotao, var.tamBotao))



	# igreja
	if var.pos_x_butao_igreja + var.tamBotao > mouse[0] > var.pos_x_butao_igreja and var.pos_y_butao_igreja + var.tamBotao > mouse[1] > var.pos_y_butao_igreja:
		pygame.draw.rect(tela, var.cor_vermelho_fraco, (var.pos_x_butao_igreja, var.pos_y_butao_igreja, var.tamBotao, var.tamBotao))
	else:
		pygame.draw.rect(tela, var.cor_vermelho, (var.pos_x_butao_igreja, var.pos_y_butao_igreja, var.tamBotao, var.tamBotao))
		


	# museu
	if var.pos_x_butao_museu + var.tamBotao > mouse[0] > var.pos_x_butao_museu and var.pos_y_butao_museu + var.tamBotao > mouse[1] > var.pos_y_butao_museu:
		pygame.draw.rect(tela, var.cor_verde_fraco, (var.pos_x_butao_museu, var.pos_y_butao_museu, var.tamBotao, var.tamBotao))
	else:
		pygame.draw.rect(tela, var.cor_verde, (var.pos_x_butao_museu, var.pos_y_butao_museu, var.tamBotao, var.tamBotao))



	



	
	
	pygame.display.update()
	clock.tick(15)

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

