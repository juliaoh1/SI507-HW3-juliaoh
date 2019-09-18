#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 09:41:24 2019

@author: Julia Coxen (juliaoh) and Zimeng Ding (zimengd)
Homework 3 (Git and Github)
SI 501, Section 001, Tuesdays at 4pm
"""

import random

#asks a question of the user to start the magic eight ball game
def askQuestion():

    quest = str(input("What is your question? "))
    print("Confirming this is your question: ", quest)

    #print(quest)
    return quest

quest = askQuestion()
