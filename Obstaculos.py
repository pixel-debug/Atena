#-*- coding utf-8 -*-

# ------------------ Projeto Atena -----------------------

# 	Autores: Estanislau Filho e José Antônio
# 	Ano: 2019
# 	Orientadora: Natália Batista
#	Instituição: CEFET-MG	
# 	Link github: https://github.com/EstanislauFilho/Atena

#	Script: Obstaculos

# --------------------------------------------------------

def perspectiva_pista(img):
	cv2.line(img, var.pt_osbtaculo_1, var.pt_osbtaculo_2, (var.cor_azul), 4)
	cv2.line(img, var.pt_osbtaculo_1, var.pt_osbtaculo_3, (var.cor_azul), 4)
	cv2.line(img, var.pt_osbtaculo_2, var.pt_osbtaculo_4, (var.cor_azul), 4)
	cv2.line(img, var.pt_osbtaculo_3, var.pt_osbtaculo_4, (var.cor_azul), 4)

	cv2.line(img, var.pt_destino_1, var.pt_destino_2, (var.cor_verde), 4)
	cv2.line(img, var.pt_destino_1, var.pt_destino_3, (var.cor_verde), 4)
	cv2.line(img, var.pt_destino_2, var.pt_destino_4, (var.cor_verde), 4)
	cv2.line(img, var.pt_destino_3, var.pt_destino_4, (var.cor_verde), 4)

	matriz = cv2.getPerspectiveTransform(var.pontos_pista, var.pontos_destino)
	img = cv2.warpPerspective(img, matriz, (var.tam_original_tela_x, var.tam_original_tela_y)) 
	return img
