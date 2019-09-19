#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 09:41:24 2019

@author: Julia Coxen (juliaoh) and Zimeng Ding (zimengd)
Homework 3 (Git and Github)
SI 507, Section 001, Tuesdays at 4pm
"""

import random

#asks a question of the user to start the magic eight ball game
def askQuestion():

    quest = str(input("What is your question? "))
    print("Confirming this is your question: ", quest)

    #print(quest)
    return quest

quest = askQuestion()

def pickAnswer(answers_list):
    i = random.choice(answers_list)
    print(i)
    return(i)

answers_list = ["It is certain.", "It is decidedly so.", "Without a doubt.","Yes - definitely.","You may rely on it.","As I see it, yes."," Most likely.","Outlook good.","Yes.","Signs point to yes.","Reply hazy, try again.","Ask again later.","Better not tell you now.","Cannot predict now.","Concentrate and ask again.","Don't count on it.","My reply is no.","My sources say no.","Outlook not so good.","Very doubtful."]
pickAnswer(answers_list)
