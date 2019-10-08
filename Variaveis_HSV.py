
# ---------------- Check points -------------------------
area_min, area_max = 4000, 50000


nome_check_1 = "Museu."
min_H_ck1 = 126 
max_H_ck1 = 151
min_S_ck1 = 70
max_S_ck1 = 180
min_V_ck1 = 77 
max_V_ck1 = 255

placa_check_1 = [min_H_ck1, max_H_ck1, min_S_ck1, max_S_ck1, min_V_ck1, max_V_ck1]

nome_check_2 = "Igreja."
min_H_ck2 = 9 
max_H_ck2 = 84
min_S_ck2 = 101
max_S_ck2 = 255 
min_V_ck2 = 131 
max_V_ck2 = 255

placa_check_2 = [min_H_ck2, max_H_ck2, min_S_ck2, max_S_ck2, min_V_ck2, max_V_ck2]

nome_check_3 = "Teatro."
min_H_ck3 = 82 
max_H_ck3 = 111
min_S_ck3 = 49 
max_S_ck3 = 255 
min_V_ck3 = 85 
max_V_ck3 = 255

placa_check_3 = [min_H_ck3, max_H_ck3, min_S_ck3, max_S_ck3, min_V_ck3, max_V_ck3]


dados_checkpoints = [
				(nome_check_1, placa_check_1),
				(nome_check_2, placa_check_2),
				(nome_check_3, placa_check_3)	
			]
# --------------------------------------------------------







# ------------------------ Semáforo --------------------- 

CONST_DETECCAO_SEMAFORO = 3200


'''
# Tarde/dia
nome_semaforo_verde_hsv = "Sinal Verde"
min_H_sem_verde = 0
max_H_sem_verde = 93
min_S_sem_verde = 172 
max_S_sem_verde = 255 
min_V_sem_verde = 99 
max_V_sem_verde = 255
'''

# Noite
nome_semaforo_verde_hsv = "Sinal Verde"
min_H_sem_verde = 0
max_H_sem_verde = 179
min_S_sem_verde = 186
max_S_sem_verde = 255 
min_V_sem_verde = 10 
max_V_sem_verde = 255


semaforo_verde = [min_H_sem_verde, max_H_sem_verde, min_S_sem_verde, max_S_sem_verde, min_V_sem_verde, max_V_sem_verde]


'''
# Tarde/dia
nome_semaforo_vermelho_hsv = "Sinal Vermelho"
min_H_sem_vermelho = 0 
max_H_sem_vermelho = 179
min_S_sem_vermelho = 132
max_S_sem_vermelho = 255
min_V_sem_vermelho = 130 
max_V_sem_vermelho = 255
'''

# Noite
nome_semaforo_vermelho_hsv = "Sinal Vermelho"
min_H_sem_vermelho = 0 
max_H_sem_vermelho = 179
min_S_sem_vermelho = 174
max_S_sem_vermelho = 255
min_V_sem_vermelho = 59 
max_V_sem_vermelho = 255


semaforo_vermelho = [min_H_sem_vermelho, max_H_sem_vermelho, min_S_sem_vermelho, max_S_sem_vermelho, min_V_sem_vermelho, max_V_sem_vermelho]


dados_semaforo = [
					(nome_semaforo_verde_hsv, semaforo_verde),
					(nome_semaforo_vermelho_hsv, semaforo_vermelho)
				 ]
	
# --------------------------------------------------------
