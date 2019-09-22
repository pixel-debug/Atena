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

pygame.init()

pygame.display.set_mode((var.tam_original_tela_x, var.tam_original_tela_y))
pygame.display.set_caption("Atena - Meta 2019")

inciar = True

while inciar:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			inciar = False
		print(event)
	pygame.display.update()

pygame.quit()
