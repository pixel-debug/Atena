#-*- coding utf-8 -*-

# ------------------ Projeto Atena -----------------------

# 	Autores: Estanislau Filho e José Antônio
# 	Ano: 2019
# 	Orientadora: Natália Batista
#	Instituição: CEFET-MG	
# 	Link github: https://github.com/EstanislauFilho/Atena

#	Script: Interface

# --------------------------------------------------------

import pygame
import Variaveis as var

#pygame.init()


pos_x = var.tam_original_tela_x/2 
pos_y = var.tam_original_tela_y/2
tamanho = 10
'''
fundo = pygame.display.set_mode((var.tam_original_tela_x, var.tam_original_tela_y))
pygame.display.set_caption("Atena - Meta 2019")

inciar = True

while inciar:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			inciar = False
		print(event)
	fundo.fill(var.cor_branco)
	pygame.draw.rect(fundo, var.cor_preto, [pos_x, pos_y, tamanho, tamanho])
	
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










