# -*- coding: utf8 -*-
from tkinter import *
from math import sin,pi
#classe permettant de visualiser les courbes qa l'osciloscope
class Oscilo(Canvas):
	"c'est une class derivee de la class Canvas de tkinter"
	debord=30						#cette variables globale permet de definir les bordures
	def __init__(self,boss=None,larg=800,haut=800):
		Canvas.__init__(self) 				#appel du constructeur de la class mere Canvas
		self.configure(width=larg,height=haut)	#assignation des dimension du canevas
		self.haut,self.larg=haut,larg
		self.create_line(self.debord,haut/2,larg,haut/2,width=2,arrow=LAST)   #l'axe des abscisses
		self.create_line(self.debord,haut-5,self.debord,5,width=2,arrow=LAST) #l'axe des ordonnees
#tracage de grille(ligne horizontales)
		pas=(larg-25)/16
		for t in range(1,17):
			xt=self.debord+t*pas
			self.create_line(xt,0,xt,haut,fill='grey')   
			self.create_text(xt,haut/2+20,text=t,fill='grey')# abscisses
		pas1=(haut)/16
#tracage de grille(ligne verticales)
		for t1 in range(1,17):
			yt=t1*pas1
			self.create_line(self.debord,yt,self.larg,yt, fill='grey')
#ordonnees
		pas2=(haut)/16
		for t2 in range(1,8):
			yt2=t2*pas2
			self.create_text(self.debord-20,yt2,text=8-t2,fill='grey')
		pas3=(haut)/16
		for t3 in range(8,17):
			yt3=t3*pas3
			self.create_text(self.debord-20,yt3,text=8-t3,fill='grey')
		self.create_text(larg-15,haut/2-14,text='time')
		self.create_text(50,self.debord,text='amplitude')
		
#methodes traceCourbes permet de tracer des sinusoides
	def traceCourbe(self,freq=1,ampl=10,phase=1,coul='red'):
		coord=[]
		echan=(self.larg-25)/10000
		for i in range(0,10000,5):
			e=ampl*sin(2*pi*freq*i/10000-phase)
			x=self.debord+i*echan
			y=self.haut/2-e*self.haut/25
			coord.append((x,y))
		n=self.create_line(coord,fill=coul,smooth=1,width=1)
		return n
	

# programmes principales
if __name__=='__main__':
	root=Tk()
	graphe=Oscilo(root,800,800) #instances d'un objet Oscilo
	graphe.pack()
	graphe.configure(bg='ivory',bd=2,relief='sunken') #appel de la methode
	graphe.traceCourbe(4,10,3,'blue')
	graphe.traceCourbe(4,5,0,'red')
	root.mainloop()
		
