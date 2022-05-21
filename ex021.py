#Faça um programa que abra e reproduza um audio de um arquivo MP3

import pygame

pygame.init()
pygame.mixer.music.load("ex021.mp3")
pygame.mixer.music.play()
pygame.event.wait()

