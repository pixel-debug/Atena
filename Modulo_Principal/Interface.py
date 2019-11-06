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
'''
pygame.init()



pygame.display.set_caption("Atena - Meta 2019")



clock = pygame.time.Clock()

def text_objects(text, font):
    textSurface = font.render(text, True, var.cor_branco)
    return textSurface, textSurface.get_rect()



def botoesInicial(tela_inicial, x, y, w, h, c1, c2, msg, txt_x, txt_y):
	mouse = pygame.mouse.get_pos()

	click = pygame.mouse.get_pressed()
	
	if x + w > mouse[0] > x and y + h > mouse[1] > y:
		pygame.draw.rect(tela_inicial, c1, (x, y, w, h))

		if(click[0] == 1 and msg != None):
			if(msg == "Entrar"):
				gps()

			elif(msg == "Sair"): 
				pygame.quit()
				quit()
	else:

		pygame.draw.rect(tela_inicial, c2, (x, y, w, h))

	texto = pygame.font.Font("freesansbold.ttf", 20)
	textoIn, textoIniciar = text_objects(msg, texto) 
	textoIniciar.center = (txt_x, txt_y)
	tela_inicial.blit(textoIn, textoIniciar)




def botoesConfirma(tela_inicial, x, y, w, h, c1, c2, msg, txt_x, txt_y):
	mouse = pygame.mouse.get_pos()

	click = pygame.mouse.get_pressed()
	
	if x + w > mouse[0] > x and y + h > mouse[1] > y:
		pygame.draw.rect(tela_inicial, c1, (x, y, w, h))

		if(click[0] == 1 and msg != None):
			if(msg == "Sim"):
				pygame.quit()
				quit()

			elif(msg == "Não"): 
				gps()
				
	else:
		pygame.draw.rect(tela_inicial, c2, (x, y, w, h))

	texto = pygame.font.Font("freesansbold.ttf", 20)
	textoIn, textoIniciar = text_objects(msg, texto) 
	textoIniciar.center = (txt_x, txt_y)
	tela_inicial.blit(textoIn, textoIniciar)





def botoesLocalidades(tela_gps, x, y, w, h, c1, c2):
	mouse = pygame.mouse.get_pos()

	click = pygame.mouse.get_pressed()

	if x + w > mouse[0] > x and y + h > mouse[1] > y:
		pygame.draw.rect(tela_gps, c1, (x, y, w, h))
		if(click[0] == 1 and (var.pos_x_butao_museu == x and var.pos_y_butao_museu == y)):
			museu()
		elif(click[0] == 1 and (var.pos_x_butao_igreja == x and var.pos_y_butao_igreja == y)):
			igreja()
		elif(click[0] == 1 and (var.pos_x_butao_teatro == x and var.pos_y_butao_teatro == y)):
			teatro()
	else:
		pygame.draw.rect(tela_gps, c2, (x, y, w, h))




def menu():
	img_telaInicial = pygame.image.load("/home/pi/Projetos/Atena/Imagens/telainicial.png")
	tela_inicial = pygame.display.set_mode((499, 325))
	tela_inicial.blit(img_telaInicial,(0,0))
	
	inciar = True

	while(inciar):
		# Botao Entrar
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		botoesInicial(tela_inicial, var.pos_x_butao_iniciar, var.pos_y_butao_iniciar, var.tamBotaoIniciar_x, var.tamBotaoIniciar_y, var.cor_verde_fraco, var.cor_verde, "Entrar", 245, 107)

		# Botao Sair
		botoesInicial(tela_inicial, var.pos_x_butao_sair, var.pos_y_butao_sair, var.tamBotaoIniciar_x, var.tamBotaoIniciar_y, var.cor_vermelho_fraco, var.cor_vermelho, "Sair", 245, 157)


		pygame.display.update()
		clock.tick(15)




def gps():
	img_background = pygame.image.load("/home/pi/Projetos/Atena/Imagens/mapa.png")
	tela_gps = pygame.display.set_mode((var.tamTela_X_Interface, var.tamTela_Y_Interface))

	tela_gps.blit(img_background,(0,var.deslocamento))
 
	inciar = True

	while(inciar):
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			
	quit()


		# Botao Museu
		botoesLocalidades(tela_gps, var.pos_x_butao_museu, var.pos_y_butao_museu, var.tamBotao, var.tamBotao, var.cor_vermelho_fraco, var.cor_vermelho)

		# Botao Igreja
		botoesLocalidades(tela_gps,var.pos_x_butao_igreja, var.pos_y_butao_igreja, var.tamBotao, var.tamBotao, var.cor_verde_fraco, var.cor_verde)

		# Botao Teatro
		botoesLocalidades(tela_gps, var.pos_x_butao_teatro, var.pos_y_butao_teatro, var.tamBotao, var.tamBotao, var.cor_azul_fraco, var.cor_azul)

		texto = pygame.font.Font("freesansbold.ttf", 25)
		textoSurf, textoTitulo = text_objects("Por favor, selecione um destino abaixo...", texto) 
		textoTitulo.center = (252, 25)
		tela_gps.blit(textoSurf, textoTitulo)


		pygame.display.update()
		clock.tick(15)


def museu():
	img_museu = pygame.image.load("/home/pi/Projetos/Atena/Imagens/museu1.jpg")
	tela_museu = pygame.display.set_mode((var.tamTela_X_ImgBack, var.tamTela_y_ImgBack))

	tela_museu.blit(img_museu,(0,0))
 
	inciar = True

	while(inciar):
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		botoesConfirma(tela_museu, var.pos_x_butao_confirma, var.pos_y_butao_confirma, var.tamBotaoIniciar_x, var.tamBotaoIniciar_y, var.cor_verde_fraco, var.cor_verde, "Sim", 245, 411)

		# Botao Sair
		botoesConfirma(tela_museu, var.pos_x_nega, var.pos_y_nega, var.tamBotaoIniciar_x, var.tamBotaoIniciar_y, var.cor_vermelho_fraco, var.cor_vermelho, "Não", 245, 474)

		texto = pygame.font.Font("freesansbold.ttf", 25)
		textoMu, textoMuseu = text_objects("Museu! Deseja confirmar o destino? ", texto) 
		textoMuseu.center = (225, 300)
		tela_museu.blit(textoMu, textoMuseu)

		pygame.display.update()
		clock.tick(15)
	


def igreja():
	img_igreja = pygame.image.load("/home/pi/Projetos/Atena/Imagens/igreja1.jpg")
	tela_igreja = pygame.display.set_mode((var.tamTela_X_ImgBack, var.tamTela_y_ImgBack))

	tela_igreja.blit(img_igreja,(0,0))
 
	inciar = True

	while(inciar):
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				inciar = False
				#break

		botoesConfirma(tela_igreja, var.pos_x_butao_confirma, var.pos_y_butao_confirma, var.tamBotaoIniciar_x, var.tamBotaoIniciar_y, var.cor_verde_fraco, var.cor_verde, "Sim", 245, 411)

		# Botao Sair
		botoesConfirma(tela_igreja, var.pos_x_nega, var.pos_y_nega, var.tamBotaoIniciar_x, var.tamBotaoIniciar_y, var.cor_vermelho_fraco, var.cor_vermelho, "Não", 245, 474)

		texto = pygame.font.Font("freesansbold.ttf", 25)
		textoMu, textoMuseu = text_objects("Igreja! Deseja confirmar o destino? ", texto) 
		textoMuseu.center = (225, 330)
		tela_igreja.blit(textoMu, textoMuseu)

		pygame.display.update()
		clock.tick(15)



def teatro():
	img_teatro = pygame.image.load("/home/pi/Projetos/Atena/Imagens/teatro1.jpg")
	tela_teatro = pygame.display.set_mode((var.tamTela_X_ImgBack, var.tamTela_y_ImgBack))

	tela_teatro.blit(img_teatro,(0,0))
 
	inciar = True

	while(inciar):
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				inciar = False
				break

		botoesConfirma(tela_teatro, var.pos_x_butao_confirma, var.pos_y_butao_confirma, var.tamBotaoIniciar_x, var.tamBotaoIniciar_y, var.cor_verde_fraco, var.cor_verde, "Sim", 245, 411)

		# Botao Sair
		botoesConfirma(tela_teatro, var.pos_x_nega, var.pos_y_nega, var.tamBotaoIniciar_x, var.tamBotaoIniciar_y, var.cor_vermelho_fraco, var.cor_vermelho, "Não", 245, 474)

		texto = pygame.font.Font("freesansbold.ttf", 25)
		textoMu, textoMuseu = text_objects("Teatro! Deseja confirmar o destino? ", texto) 
		textoMuseu.center = (225, 360)
		tela_teatro.blit(textoMu, textoMuseu)

		pygame.display.update()
		clock.tick(15)


m, i, t = False, False, False
menu()
gps()
m = museu()
i = igreja()
t = teatro()
print(m, i, t)
pygame.quit()
quit()

'''




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

'''
def apresenta_tela(nome, imagem, pos_x, pos_y):
	cv2.namedWindow(nome, cv2.WINDOW_KEEPRATIO);
	cv2.moveWindow(nome, pos_x, pos_y);
	cv2.resizeWindow(nome, var.tam_mini_tela_x, var.tam_mini_tela_y)
	cv2.imshow(nome, imagem)













