#cabecera


print(""" 
..######.....###....##........######..##.....##.##..........###....########...#######..########.....###......
.##....##...##.##...##.......##....##.##.....##.##.........##.##...##.....##.##.....##.##.....##...##.##.....
.##........##...##..##.......##.......##.....##.##........##...##..##.....##.##.....##.##.....##..##...##....
.##.......##.....##.##.......##.......##.....##.##.......##.....##.##.....##.##.....##.########..##.....##...
.##.......#########.##.......##.......##.....##.##.......#########.##.....##.##.....##.##...##...#########...
.##....##.##.....##.##.......##....##.##.....##.##.......##.....##.##.....##.##.....##.##....##..##.....##...
..######..##.....##.########..######...#######..########.##.....##.########...#######..##.....##.##.....##...
 """) 
print("Author: @antonioalme_20")
import sys
from clint.textui import colored
import math
def main():
	from clint.textui import colored

	print("\n1)Ecuaciones\n2)Terna Pitagorica\n3)Conversor de Unidades\n4)Teorema de Pitagoras\n5)Sistema de Evaluacion\n6)Vectores")
	eleccion1=input()

	if eleccion1== '1':
		print(colored.yellow("\nCalculadora de la forma Ax^2+Bx+C"))
		#Meter datos
		print("\nPon A:")
		num_a=float(input())

		print("Pon B:")
		num_b=float(input())

		print("Pon C:")
		num_c=float(input())
		#Si la ecuacion no tiene solucion 
		if num_b**2-4*num_a*num_c<0 :
			print(colored.red("\nNo tiene solucion")) 
		#Si la ecuacion tiene solucion hace las operaciones
		else:
			print(colored.green("\nSOLUCIONES"))
			import math
			print((-num_b+math.sqrt(num_b**2-4*num_a*num_c))/(2*num_a))
			print((-num_b-math.sqrt(num_b**2-4*num_a*num_c))/(2*num_a))
	#Eleccion de Terna
	if eleccion1== '2':
		print(colored.yellow("\nDe la forma a^2=b^2+c^2"))
		#meter valores de la terna y pasarlos a int
		print("\nPon A:") 
		numt_a=float(input())

		print("Pon B:")
		numt_b=float(input())

		print("Pon C:")
		numt_c=float(input())
		#Resultado
		
		if numt_a**2<(numt_b**2)+(numt_c**2) :
			print(colored.red("\nNo es una terna pitagorica"))
		elif numt_a**2>(numt_b**2)+(numt_c**2) :
			print(colored.red("\nNo es una terna pitagorica"))
		else :
			print(colored.green("\n Si es una terna pitagorica"))
	#Conversor
	if eleccion1== '3':
		print("\n1)Longitudes\n2)Capacidad\n3)Peso\n4)Comunes S.I\n5)Energia")
		eleccion_f=input()
		#LONGITUDES
		#LONGITUDES
		#LONGITUDES
		if eleccion_f == '1':
			print("\n1)mm->...\n2)cm->...\n3)dm->...\n4)m->...\n5)dam->...\n6)hm->...\n7)km->...")
			eleccion_fl=input()
			#mm
			if eleccion_fl == '1':
				print("\nMilimetros")
				print("\n1)mm->cm\n2)mm->dm\n3)mm->m\n4)mm->dam\n5)mm->hm\n6)mm->km")
				eleccion_flmm=input()
				#mm cm
				if eleccion_flmm== '1':
					print("\nPon mm")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/10)
				#mm dm
				if eleccion_flmm== '2':
					print("\nPon mm")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/100)
				#mm m
				if eleccion_flmm== '3':
					print("\nPon mm")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/1000)
				#mm dam
				if eleccion_flmm== '4':
					print("\nPon mm")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/10000)
				#mm hm
				if eleccion_flmm== '5':
					print("\nPon mm")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/100000)
				#mm km
				if eleccion_flmm== '6':
					print("\nPon mm")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/1000000)
					#cm 
			if eleccion_fl == '2':
				print("\nCentimetros")
				print("\n1)cm->mm\n2)cm->dm\n3)cm->m\n4)cm->dam\n5)cm->hm\n6)cm->km")
				eleccion_flmm=input()
				#cm mm
				if eleccion_flmm== '1':
					print("\nPon cm")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*10)
					#cm dm
				if eleccion_flmm== '2':
					print("\nPon cm")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/10)
					#cm m
				if eleccion_flmm== '3':
					print("\nPon cm")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/100)
					#cm dam
				if eleccion_flmm== '4':
					print("\nPon cm")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/1000)
					#cm hm
				if eleccion_flmm== '5':
					print("\nPon cm")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/10000)
					#cm km
				if eleccion_flmm== '6':
					print("\nPon cm")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/100000)
			if eleccion_fl == '3':
				print("\nDecimetros")
				print("\n1)dm->mm\n2)dm->cm\n3)dm->m\n4)dm->dam\n5)dm->hm\n6)dm->km")
				eleccion_flmm=input()
				#dm mm
				if eleccion_flmm== '1':
					print("\nPon dm")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*100)
					#dm cm
				if eleccion_flmm== '2':
					print("\nPon dm")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*10)
					#dm m
				if eleccion_flmm== '3':
					print("\nPon dm")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/10)
					#dm dam
				if eleccion_flmm== '4':
					print("\nPon dm")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/100)
					#dm hm
				if eleccion_flmm== '5':
					print("\nPon dm")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/1000)
					#dm km
				if eleccion_flmm== '6':
					print("\nPon dm")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/10000)
			if eleccion_fl == '4':
				print("\nMetros")
				print("\n1)m->mm\n2)m->cm\n3)m->dm\n4)m->dam\n5)m->hm\n6)m->km")
				eleccion_flmm=input()
				#m mm
				if eleccion_flmm== '1':
					print("\nPon m")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*1000)
					#m cm
				if eleccion_flmm== '2':
					print("\nPon m")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*100)
					#m dm
				if eleccion_flmm== '3':
					print("\nPon m")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*10)
					#m dam
				if eleccion_flmm== '4':
					print("\nPon m")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/10)
					#m hm
				if eleccion_flmm== '5':
					print("\nPon m")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/100)
					#m km
				if eleccion_flmm== '6':
					print("\nPon m")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/1000)
			if eleccion_fl == '5':
				print("\nDecametros")
				print("\n1)dam->mm\n2)dam->cm\n3)dam->dm\n4)dam->m\n5)dam->hm\n6)dam->km")
				eleccion_flmm=input()
				#dam mm
				if eleccion_flmm== '1':
					print("\nPon dam")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*10000)
					#dam cm
				if eleccion_flmm== '2':
					print("\nPon dam")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*1000)
					#dam dm
				if eleccion_flmm== '3':
					print("\nPon dam")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*100)
					#dam m
				if eleccion_flmm== '4':
					print("\nPon dam")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*10)
					#dam hm
				if eleccion_flmm== '5':
					print("\nPon dam")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/10)
					#dam km
				if eleccion_flmm== '6':
					print("\nPon m")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/100)
			if eleccion_fl == '6':
				print("\nHectometros")
				print("\n1)hm->mm\n2)hm->cm\n3)hm->dm\n4)hm->m\n5)hm->dam\n6)hm->km")
				eleccion_flmm=input()
				#hm mm
				if eleccion_flmm== '1':
					print("\nPon hm")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*100000)
					#hm cm
				if eleccion_flmm== '2':
					print("\nPon hm")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*10000)
					#hm dm
				if eleccion_flmm== '3':
					print("\nPon hm")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*1000)
					#hm m
				if eleccion_flmm== '4':
					print("\nPon hm")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*100)
					#hm dam
				if eleccion_flmm== '5':
					print("\nPon hm")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*10)
					#hm km
				if eleccion_flmm== '6':
					print("\nPon hm")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/10)
			if eleccion_fl == '6':
				print("\nKilometros")
				print("\n1)km->mm\n2)km->cm\n3)km->dm\n4)km->m\n5)km->dam\n6)km->hm")
				eleccion_flmm=input()
				#km mm
				if eleccion_flmm== '1':
					print("\nPon km")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*1000000)
					#km cm
				if eleccion_flmm== '2':
					print("\nPon km")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*100000)
					#km dm
				if eleccion_flmm== '3':
					print("\nPon km")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*10000)
					#km m
				if eleccion_flmm== '4':
					print("\nPon km")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*1000)
					#km dam
				if eleccion_flmm== '5':
					print("\nPon km")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*100)
					#km hm
				if eleccion_flmm== '6':
					print("\nPon km")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*10)
		if eleccion_f == '2':
			print("\n1)ml->...\n2)cl->...\n3)dl->...\n4)l->...\n5)dal->...\n6)hl->...\n7)kl->...")
			eleccion_fl=input()
			#ml
			if eleccion_fl == '1':
				print("\nMililitros")
				print("\n1)ml->cl\n2)ml->dl\n3)ml->l\n4)ml->dal\n5)ml->hl\n6)ml->kl")
				eleccion_flmm=input()
				#ml cl
				if eleccion_flmm== '1':
					print("\nPon ml")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/10)
				#ml dl
				if eleccion_flmm== '2':
					print("\nPon ml")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/100)
				#ml l
				if eleccion_flmm== '3':
					print("\nPon ml")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/1000)
				#ml dal
				if eleccion_flmm== '4':
					print("\nPon ml")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/10000)
				#ml hl
				if eleccion_flmm== '5':
					print("\nPon ml")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/100000)
				#ml kl
				if eleccion_flmm== '6':
					print("\nPon ml")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/1000000)
					#cm 
			if eleccion_fl == '2':
				print("\nCentilitros")
				print("\n1)cl->ml\n2)cl->dl\n3)cl->l\n4)cl->dal\n5)cl->hl\n6)cl->kl")
				eleccion_flmm=input()
				#cm mm
				if eleccion_flmm== '1':
					print("\nPon cl")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*10)
					#cm dm
				if eleccion_flmm== '2':
					print("\nPon cl")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/10)
					#cm m
				if eleccion_flmm== '3':
					print("\nPon cl")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/100)
					#cm dam
				if eleccion_flmm== '4':
					print("\nPon cl")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/1000)
					#cm hm
				if eleccion_flmm== '5':
					print("\nPon cl")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/10000)
					#cm km
				if eleccion_flmm== '6':
					print("\nPon cl")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/100000)
			if eleccion_fl == '3':
				print("\nDecilitros")
				print("\n1)dl->ml\n2)dl->cl\n3)dl->l\n4)dl->dal\n5)dl->hl\n6)dl->kl")
				eleccion_flmm=input()
				#dm mm
				if eleccion_flmm== '1':
					print("\nPon dl")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*100)
					#dm cm
				if eleccion_flmm== '2':
					print("\nPon dl")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*10)
					#dm m
				if eleccion_flmm== '3':
					print("\nPon dl")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/10)
					#dm dam
				if eleccion_flmm== '4':
					print("\nPon dl")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/100)
					#dm hm
				if eleccion_flmm== '5':
					print("\nPon dl")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/1000)
					#dm km
				if eleccion_flmm== '6':
					print("\nPon dl")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/10000)
			if eleccion_fl == '4':
				print("\nLitros")
				print("\n1)l->ml\n2)l->cl\n3)l->dl\n4)l->dal\n5)l->hl\n6)l->kl")
				eleccion_flmm=input()
				#m mm
				if eleccion_flmm== '1':
					print("\nPon l")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*1000)
					#m cm
				if eleccion_flmm== '2':
					print("\nPon l")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*100)
					#m dm
				if eleccion_flmm== '3':
					print("\nPon l")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*10)
					#m dam
				if eleccion_flmm== '4':
					print("\nPon l")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/10)
					#m hm
				if eleccion_flmm== '5':
					print("\nPon l")
					num_f_mm=float(input())
					print("\nResultado:")
					print(num_f_mm/100)
					#m km
				if eleccion_flmm== '6':
					print("\nPon l")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/1000)
			if eleccion_fl == '5':
				print("\nDecalitros")
				print("\n1)dal->ml\n2)dal->cl\n3)dal->dl\n4)dal->l\n5)dal->hl\n6)dal->kl")
				eleccion_flmm=input()
				#dam mm
				if eleccion_flmm== '1':
					print("\nPon dal")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*10000)
					#dam cm
				if eleccion_flmm== '2':
					print("\nPon dal")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*1000)
					#dam dm
				if eleccion_flmm== '3':
					print("\nPon dal")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*100)
					#dam m
				if eleccion_flmm== '4':
					print("\nPon dal")
					num_f_mm=float(input())
					print("\nResultado:")
					print(num_f_mm*10)
					#dam hm
				if eleccion_flmm== '5':
					print("\nPon dal")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/10)
					#dam km
				if eleccion_flmm== '6':
					print("\nPon dal")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/100)
			if eleccion_fl == '6':
				print("\nHectolitros")
				print("\n1)hl->ml\n2)hl->cl\n3)hl->dl\n4)hl->l\n5)hl->dal\n6)hl->kl")
				eleccion_flmm=input()
				#hm mm
				if eleccion_flmm== '1':
					print("\nPon hl")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*100000)
					#hm cm
				if eleccion_flmm== '2':
					print("\nPon hl")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*10000)
					#hm dm
				if eleccion_flmm== '3':
					print("\nPon hl")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*1000)
					#hm m
				if eleccion_flmm== '4':
					print("\nPon hl")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*100)
					#hm dam
				if eleccion_flmm== '5':
					print("\nPon hl")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*10)
					#hm km
				if eleccion_flmm== '6':
					print("\nPon hl")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/10)
			if eleccion_fl == '6':
				print("\nKilolitros")
				print("\n1)kl->ml\n2)kl->cl\n3)kl->dl\n4)kl->l\n5)kl->dal\n6)kl->hl")
				eleccion_flmm=input()
				#km mm
				if eleccion_flmm== '1':
					print("\nPon kl")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*1000000)
					#km cm
				if eleccion_flmm== '2':
					print("\nPon kl")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*100000)
					#km dm
				if eleccion_flmm== '3':
					print("\nPon kl")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*10000)
					#km m
				if eleccion_flmm== '4':
					print("\nPon kl")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*1000)
					#km dam
				if eleccion_flmm== '5':
					print("\nPon kl")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*100)
					#km hm
				if eleccion_flmm== '6':
					print("\nPon kl")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*10)
		if eleccion_f == '3':
			print("\n1)mg->...\n2)cg->...\n3)dg->...\n4)g->...\n5)dag->...\n6)hg->...\n7)kg->...")
			eleccion_fl=input()
			#ml
			if eleccion_fl == '1':
				print("\nMiligramos")
				print("\n1)mg->cg\n2)mg->dg\n3)mg->g\n4)mg->dag\n5)mg->hg\n6)mg->kg")
				eleccion_flmm=input()
				#ml cl
				if eleccion_flmm== '1':
					print("\nPon mg")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/10)
				#ml dl
				if eleccion_flmm== '2':
					print("\nPon mg")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/100)
				#ml l
				if eleccion_flmm== '3':
					print("\nPon mg")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/1000)
				#ml dal
				if eleccion_flmm== '4':
					print("\nPon mg")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/10000)
				#ml hl
				if eleccion_flmm== '5':
					print("\nPon mg")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/100000)
				#ml kl
				if eleccion_flmm== '6':
					print("\nPon mg")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/1000000)
					#cm 
			if eleccion_fl == '2':
				print("\nCentigramos")
				print("\n1)cg->mg\n2)cg->dg\n3)cg->g\n4)cg->dag\n5)cg->hg\n6)cg->kg")
				eleccion_flmm=input()
				#cm mm
				if eleccion_flmm== '1':
					print("\nPon cg")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*10)
					#cm dm
				if eleccion_flmm== '2':
					print("\nPon cg")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/10)
					#cm m
				if eleccion_flmm== '3':
					print("\nPon cg")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/100)
					#cm dam
				if eleccion_flmm== '4':
					print("\nPon cg")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/1000)
					#cm hm
				if eleccion_flmm== '5':
					print("\nPon cg")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/10000)
					#cm km
				if eleccion_flmm== '6':
					print("\nPon cg")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/100000)
			if eleccion_fl == '3':
				print("\nDecigramos")
				print("\n1)dg->mg\n2)dg->cg\n3)dg->g\n4)dg->dag\n5)dg->hg\n6)dg->kg")
				eleccion_flmm=input()
				#dm mm
				if eleccion_flmm== '1':
					print("\nPon dg")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*100)
					#dm cm
				if eleccion_flmm== '2':
					print("\nPon dg")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*10)
					#dm m
				if eleccion_flmm== '3':
					print("\nPon dg")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/10)
					#dm dam
				if eleccion_flmm== '4':
					print("\nPon dg")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/100)
					#dm hm
				if eleccion_flmm== '5':
					print("\nPon dg")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/1000)
					#dm km
				if eleccion_flmm== '6':
					print("\nPon dg")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/10000)
			if eleccion_fl == '4':
				print("\nGramos")
				print("\n1)g->mg\n2)g->cg\n3)g->dg\n4)g->dag\n5)g->hg\n6)g->kg")
				eleccion_flmm=input()
				#m mm
				if eleccion_flmm== '1':
					print("\nPon g")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*1000)
					#m cm
				if eleccion_flmm== '2':
					print("\nPon g")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*100)
					#m dm
				if eleccion_flmm== '3':
					print("\nPon g")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*10)
					#m dam
				if eleccion_flmm== '4':
					print("\nPon g")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/10)
					#m hm
				if eleccion_flmm== '5':
					print("\nPon g")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/100)
					#m km
				if eleccion_flmm== '6':
					print("\nPon g")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/1000)
			if eleccion_fl == '5':
				print("\nDecagramos")
				print("\n1)dag->mg\n2)dag->cg\n3)dag->dg\n4)dag->g\n5)dag->hg\n6)dag->kg")
				eleccion_flmm=input()
				#dam mm
				if eleccion_flmm== '1':
					print("\nPon dag")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*10000)
					#dam cm
				if eleccion_flmm== '2':
					print("\nPon dag")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*1000)
					#dam dm
				if eleccion_flmm== '3':
					print("\nPon dag")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*100)
					#dam m
				if eleccion_flmm== '4':
					print("\nPon dag")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*10)
					#dam hm
				if eleccion_flmm== '5':
					print("\nPon dag")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/10)
					#dam km
				if eleccion_flmm== '6':
					print("\nPon dag")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/100)
			if eleccion_fl == '6':
				print("\nHectogramos")
				print("\n1)hg->mg\n2)hg->cg\n3)hg->dg\n4)hg->g\n5)hg->dag\n6)hg->kg")
				eleccion_flmm=input()
				#hm mm
				if eleccion_flmm== '1':
					print("\nPon hg")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*100000)
					#hm cm
				if eleccion_flmm== '2':
					print("\nPon hg")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*10000)
					#hm dm
				if eleccion_flmm== '3':
					print("\nPon hg")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*1000)
					#hm m
				if eleccion_flmm== '4':
					print("\nPon hg")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*100)
					#hm dam
				if eleccion_flmm== '5':
					print("\nPon hg")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*10)
					#hm km
				if eleccion_flmm== '6':
					print("\nPon hg")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm/10)
			if eleccion_fl == '6':
				print("\nKilogramos")
				print("\n1)kg->mg\n2)kg->cg\n3)kg->dg\n4)kg->g\n5)kg->dag\n6)kg->hg")
				eleccion_flmm=input()
				#km mm
				if eleccion_flmm== '1':
					print("\nPon kg")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*1000000)
					#km cm
				if eleccion_flmm== '2':
					print("\nPon kg")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*100000)
					#km dm
				if eleccion_flmm== '3':
					print("\nPon kg")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*10000)
					#km m
				if eleccion_flmm== '4':
					print("\nPon kg")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*1000)
					#km dam
				if eleccion_flmm== '5':
					print("\nPon kg")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*100)
					#km hm
				if eleccion_flmm== '6':
					print("\nPon kg")
					num_f_mm=float(input())
					print(colored.green("\nResultado:"))
					print(num_f_mm*10)
		if eleccion_f == '4':
			print("\n1)Velocidad\n2)Tiempo\n3)Temperatura")
			eleccion_fsi=input()
			if eleccion_fsi == '1':
				print("\n1)km/h->m/s\n2)m/s->km/h")
				eleccion_fsiv=input()
				if eleccion_fsiv== '1':
					print("\nPon km/h")
					num_kmh=float(input())
					def kmhtoms():
						print((num_kmh*1000)/3600)
					print(colored.green("\nResultado:"))
					kmhtoms()
				elif eleccion_fsiv== '2':
					print("\nPon m/s")
					num_kmh=float(input())
					def mstokmh():
						print((num_kmh*3600)/1000)
					print(colored.green("\nResultado:"))
					mstokmh()
			if eleccion_fsi == '2':
				print("\n1)h->s\n2)min->s\n3)s->h\n4)s->min")
				eleccion_fsit=input()
				if eleccion_fsit == '1':
					print("\nPon h")
					num_h=float(input())
					def htos():
						print(num_h*3600)
					print(colored.green("\nResultado:"))
					htos()
				elif eleccion_fsit == '':
					print("\nPon min")
					num_h=float(input())
					def mintos():
						print(num_h*60)
					print(colored.green("\nResultado:"))
					mintos()
				elif eleccion_fsit == '3':
					print("\nPon s")
					num_h=float(input())
					def stoh():
						print(num_h//3600)
					print(colored.green("\nResultado:"))
					stoh()
				elif eleccion_fsit == '4':
					print("\nPon s")
					num_h=float(input())
					def stomin():
						print(num_h/60)
					print(colored.green("\nResultado:"))
					stomin()
			if eleccion_fsi == '3':
				print("\n1)Centigrados->Kelvin\n2)Kelvin->Centigrados")
				eleccion_fsic=input()
				if eleccion_fsic== '1':
					print("Pon Centigrados")
					num_cent=float(input())
					def ctok():
						print(num_cent+273.15)
					print(colored.green("\nResultado:"))
					ctok()
				else:
					print("Pon K")
					num_k=float(input())
					def ktoc():
						print(num_k-273.15)
					print(colored.green("\nResultado:"))
					ktoc()
		if eleccion_f == '5':
			print("\n1)BTU\n2)Calorias\n3)Electron Voltios\n4)Gigajulios\n5)Julios\n6)Kilocalorias\n7)Kilojulios\n8)Kilovatios Hora\n9)Megajulios\n10)Newton Metros\n11)Thermie\n12)Segundos de Watt\n13)Quads\n14)Therms\n15)Pies Libras")
			eleccion_fsie=input()
			if eleccion_fsie== '1':
				print(colored.yellow("BTU"))
				print("\n1)BTU -> Calorias\n2)BTU -> Electron Voltios\n3)BTU -> Gigajulios\n4)BTU -> Julios\n5)BTU -> Kilocalorias\n6)BTU -> Kilojulios\n7)BTU -> Kilovatios hora\n8)BTU -> Megajulios\n9)BTU -> Newton Metros\n10)BTU -> Thermie\n11)BTU -> Segundos de Watt\n12)BTU -> Quads\n13)BTU -> Therms\n14)BTU -> Pies Libras")
				eleccion_fsibtu=input()
				if eleccion_fsibtu == '1':
						print(colored.yellow("Pon BTU"))
						num_btu=float(input())
						def btutocal():
							print(num_btu*251.996)
						btutocal()


	#Teorema de pitagoras
	if eleccion1== '4':
		print("\n1)Hallar la hipotenusa\n2)Hallar un cateto")
		eleccion_tp=input()
		if eleccion_tp == '1':
			print(colored.yellow("\nPon Cateto 1"))
			num_cat1=float(input())
			print(colored.yellow("Pon Cateto 2"))
			num_cat2=float(input())
			def hipotenusa():
				import math
				print(math.sqrt((num_cat1**2)+(num_cat2**2)))
			print(colored.green("\nHipotenusa:"))
			hipotenusa()
		else:
			print(colored.yellow("\nPon Hipotenusa"))
			num_hipo=float(input())
			print(colored.yellow("Pon Cateto"))
			num_cat1=float(input())
			def cateto():
				import math
				print(math.sqrt((num_hipo**2)-(num_cat1**2)))
			print(colored.green("\nResultado:"))
			cateto()
	#Evaluacion
	if eleccion1 == '5':
		print("\n1)Con 1 nota\n2)Con 2 notas\n3)Con 3 notas\n4)Con 4 notas")
		eleccion_n=input()
		if eleccion_n == '1':
			print(colored.yellow("Pon la nota:"))
			nota1=input()
			print(colored.green("\nResultado:"))
			print(nota1)
		elif eleccion_n == '2': 
			print(colored.yellow("Pon la primera nota"))
			nota1=float(input())
			print(colored.yellow("Pon la segunda nota"))
			nota2=float(input())
			def notas2():
				notass2=(nota1+nota2)/2
				print(colored.green("\nResultado:"))
				print(notass2)
			notas2()
		elif eleccion_n == '3':
			print(colored.yellow("Pon la primera nota"))
			nota1=float(input())
			print(colored.yellow("Pon la segunda nota"))
			nota2=float(input())
			print(colored.yellow("Pon la tercera nota"))
			nota3=float(input())
			def notas3():
				notass3=(nota1+nota2+nota3)/3
				print(colored.green("\nResultado:"))
				print(notass3)
			notas3()
		elif eleccion_n == '4':
			print(colored.yellow("Pon la primera nota"))
			nota1=float(input())
			print(colored.yellow("Pon la segunda nota"))
			nota2=float(input())
			print(colored.yellow("Pon la tercera nota"))
			nota3=float(input())
			print(colored.yellow("Pon la cuarta nota"))
			nota4=float(input())
			def notas4():
				notass4=(nota1+nota2+nota3+nota4)/4
				print(colored.green("\nResultado"))
				print(notass4)
			notas4()
	if eleccion1 == '6':
		print("\n1)Ecuaciones de la recta\n2)Modulo\n3)Hallar vector con dos puntos")
		eleccionv=input()
		if eleccionv == '1':
			print("\n1)Vectorial\n2)Parametrica\n3)Continua\n4)General\n5)Explicita\n6)Todas")
			eleccionvv=input()
			if eleccionvv == '1':
				print(colored.yellow("\nPon x"))
				x=str(input())
				print(colored.yellow("\nPon y"))
				y=str(input())
				print(colored.yellow("\nPon Primera coordenada de el vector"))
				v1=str(input())
				print(colored.yellow("\nPon Segunda coordenada de el vector"))
				v2=str(input())
				def vectorial():
					print("(x,y)=("+x+(",")+y+")+t("+v1+(",")+v2+")")
				vectorial()
			if eleccionvv=='2':
				print(colored.yellow("\nPon x"))
				x=str(input())
				print(colored.yellow("\nPon y"))
				y=str(input())
				print(colored.yellow("\nPon Primera coordenada de el vector"))
				v1=str(input())
				print(colored.yellow("\nPon Segunda coordenada de el vector"))
				v2=str(input())
				def parametrica():
					print("\n  ---")
					print("  |x="+x+("+t(")+v1+(")"))
					print(" -|")
					print("  |y="+y+("+t(")+v2+(")"))
					print("  ---")
				parametrica()
			if eleccionvv=='3':
				print(colored.yellow("\nPon x"))
				x=str(input())
				print(colored.yellow("\nPon y"))
				y=str(input())
				print(colored.yellow("\nPon Primera coordenada de el vector"))
				v1=str(input())
				print(colored.yellow("\nPon Segunda coordenada de el vector"))
				v2=str(input())
				def continua():
					print("\n x-("+x+")    y=("+y+")")
					print("------ = ------")
					print("  "+v1+"         "+v2)
				continua()
			if eleccionvv=='4':
				print(colored.yellow("\nPon x"))
				x=str(input())
				print(colored.yellow("\nPon y"))
				y=str(input())
				print(colored.yellow("\nPon Primera coordenada de el vector"))
				v1=str(input())
				print(colored.yellow("\nPon Segunda coordenada de el vector"))
				v2=str(input())
				def general():
					print("\n("+v2+"x)"+"-("+v1+"y)+("+v1+"*"+y+"-"+v2+"*"+x+")")
				general()
			if eleccionvv == '5':
				print(colored.yellow("\nPon x"))
				x=float(input())
				print(colored.yellow("\nPon y"))
				y=float(input())
				print(colored.yellow("\nPon Primera coordenada de el vector"))
				v1=float(input())
				print(colored.yellow("\nPon Segunda coordenada de el vector"))
				v2=float(input())
				def explicita():
					m=str(-(v2/-v1))
					n=str(-((v1*y-v2*x)/(-v1)))
					print("y="+m+"x+"+n)
				explicita()
				def explicita1():
					x=float(x)
					y=float(y)
					v1=float(v1)
					v2=float(v2)
					m=str(-(v2/-v1))
					n=str(-((v1*y-v2*x)/(-v1)))
					print("y="+m+"x+"+n)

			if eleccionvv=='6':
				print(colored.yellow("\nPon x"))
				x=str(input())
				print(colored.yellow("\nPon y"))
				y=str(input())
				print(colored.yellow("\nPon Primera coordenada de el vector"))
				v1=str(input())
				print(colored.yellow("\nPon Segunda coordenada de el vector"))
				v2=str(input())
				print(colored.yellow("\nVECTORIAL"))
				def vectorial():
					print("\n(x,y)=("+x+(",")+y+")+t("+v1+(",")+v2+")")
				vectorial()
				print(colored.yellow("\nPARAMETRICA"))
				def parametrica():
					print("\n  ---")
					print("  |x="+x+("+t(")+v1+(")"))
					print(" -|")
					print("  |y="+y+("+t(")+v2+(")"))
					print("  ---")
				parametrica()
				print(colored.yellow("\nCONTINUA"))
				def continua():
					print("\n x-("+x+")    y=("+y+")")
					print("------ = ------")
					print("  "+v1+"         "+v2)
				continua()
				print(colored.yellow("\nGENERAL"))
				def general():
					print("\n("+v2+"x)"+"-("+v1+"y)+("+v1+"*"+y+"-"+v2+"*"+x+")=0")
				general()
				print(colored.yellow("\nEXPLICITA"))
				def explicita1():
					x1=float(x)
					y2=float(y)
					v3=float(v1)
					v4=float(v2)
					m=str(-(v4/-v3))
					n=str(-((v3*y2-v4*x1)/(-v3)))
					print("\ny="+m+"x+"+n)
				explicita1()
		if eleccionv == '2':
			print(colored.yellow("\nPon primera coordenada"))
			mod1=float(input())
			print(colored.yellow("Pon segunda coordenada"))
			mod2=float(input())
			def modulo():
				import math
				print(colored.green("\nResultado"))
				print(math.sqrt((mod1**2)+(mod2**2)))
			modulo()
		if eleccionv=='3':
			print(colored.yellow("\nCoordenada 1 del origen"))
			x1=float(input())
			print(colored.yellow("Coordenada 2 del origen"))
			y1=float(input())
			print(colored.yellow("\nCoordenada 1 del extremo"))
			x2=float(input())
			print(colored.yellow("Coordenada 2 del extremo"))
			y2=float(input())
			def vector():
				v1=str(x2-x1)
				v2=str(y2-x1)
				print(colored.green("\nVector")+"("+v1+","+v2+")")
			vector()	
main()
def looop():
	print(colored.red("\n¿Volver? Si/No"))
	eleccionvolverr=input()
	eleccionvolver=eleccionvolverr.lower()
	if eleccionvolver == 'si':
		main()
	if eleccionvolver == 'no':
		sys.exit()

i=1
while i<10:
	looop()
