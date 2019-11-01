#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 15:28:13 2019

@author: rthiebaut
"""

"""
Useful Function
"""
import random #use randrange
import sys


def indice(liste,element): #trouve l'indice de l'élément dans la liste attention lelement doit etre present utiliser NameOfTheList.index
  for i,e in enumerate(liste):
      if e==element:
        return i


def question_ferme(proposition): #rajout dun quit
  """
  souhaitez vous "proposition" ? si oui -> vrai / si non -> false
  """
  while True :
       x=input("Souhaitez-vous %s ? oui/non " % proposition)
       if x=='quit':
           sys.exit()
       if x=='oui' or x=='non' :
           break
  if x=='oui':
      return True
  else :
      return False

def question_ouverte(question, liste_choix_possible) : #rajout dun quit
    """
    return une proposition qui reponds aux conditions requises
    """
    while True :
        proposition = input(question)
        if proposition=="quit":
            sys.exit()
        if proposition in liste_choix_possible :
            return proposition

def choix_aleatoire(liste_choix_possible) :
    """
    fais un choix aleatoire parmis ceux possibles
    """
    choix=random.randrange(len(liste_choix_possible))
    return liste_choix_possible[choix]

def decision(liste_choix_possible=[True,False], random=True, question="", ouverte=True):
    if random :
        return(choix_aleatoire(liste_choix_possible))
    else :
        if ouverte:
            return(question_ouverte(question, liste_choix_possible))
        else :
            return (question_ferme(question))




#GRAPHIC
import pygame


def draw_text(screen, text, position, color=(0,0,0),
                font_type='mono', font_size = 15):
    """
    write text in window
    """
    font = pygame.font.SysFont(font_type, font_size)
    surface = font.render(text, True, color)
    surface = pygame.transform.scale(surface,(position[2],position[3]))
    screen.blit(surface, position)
    pygame.display.flip()



def get_mouse(surface):
  """
  return true if the mouse in the surface
  """
  mouse=pygame.mouse.get_pos()
  if mouse[0]>surface[0] and mouse[0]<surface[2]+surface[0] and mouse[1]>surface[1] and mouse[1]<surface[1]+surface[3]:
    return True

def graphic_yesorno(screen,question,question_surface,yes_surface,no_surface):
  """
  do you like to "question" ? if click yes -> True if click no -> False
  """
  result=None
  draw_text(screen, text="YES", position=yes_surface)
  draw_text(screen, text="NO", position=no_surface)
  draw_text(screen, text=question, position=question_surface)


  while result!=True and result!=False :
     event = pygame.event.poll()

     if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: #escape
       break

     if get_mouse(yes_surface):
       if  event.type == pygame.MOUSEBUTTONDOWN :
         result=True

     if get_mouse(no_surface):
       if  event.type == pygame.MOUSEBUTTONDOWN :
         result=False


     pygame.display.flip()
  return result