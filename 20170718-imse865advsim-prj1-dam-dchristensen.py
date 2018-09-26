# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 16:27:36 2017

@author: derekc
"""

import random

def getrand(lv, uv):
    randnum = random.randint(lv, uv)
    #print randnum
    return (randnum)

#Probably looking for 2nd highest point, so
#    □ Keep track of MAX HEIGHT and 2nd MAX HEIGHT

def rain(lv, chancerainuv):
    #uv = 100/chancerain
    #print uv
    randnum = getrand(lv, chancerainuv)
    if randnum == 5:
        rain = 'rains'
    elif randnum < 5:
        rain = 'no rain'
#    print rain
    return (rain)

def type(lv, chancetypeuv):
    randnum = getrand(lv, chancetypeuv)
    #print randnum
    if randnum == 1:
        type = 'downpour'
    elif randnum > 1 and randnum <=5:
        type = 'rain'
    elif randnum > 5:
        type = 'shower'
    #print type
    return (type)

def amount(typerain):
    if typerain == 'downpour':
        amount = getrand(100, 500) / 100.0
    elif typerain == 'rain':
        amount = getrand(40,120) / 100.0
    elif typerain == 'shower':
        amount = getrand(5, 60) / 100.0
    #print 'amount of precipitation =', amount
    return (amount)
    
def lose(normalh, oldh):
    diffh = oldh - normalh
    if diffh >= 5:
        lose = 0.50
    else:
        lose = 0.25
    #print 'daily amount lost =', lose
    return (lose)

def gain(amountrain):
    if amountrain < 0.40:
        gain = amountrain
    elif amountrain >= 0.40 and amountrain <= 1.00:
        gain = amountrain * 2
    elif amountrain > 1.00:
        gain = amountrain * 5
    #print 'amount that the lake gains =', gain
    return (gain)

#main
maxmax = []
max2nd = []

print 'max =', maxmax
print 'max2nd =', max2nd

lv = 1
chancerainuv = 5
chancetypeuv = 20

for rep in range (0,30):
#    print
#    print 'rep =', rep
    
    normalh = 1108
    maxh = 1108
    max2ndh = 1108
    oldh = 1108
    
    for day in range (0,365):
        gainh = 0
#        print
#        print 'day =', day
        
#        print 'max height =', maxh
#        print '2nd heighest =', max2ndh
#        print 'old height =', oldh
        
        loseh = lose(normalh, oldh)
        #print'loseh =', loseh
        
        weather = rain(lv, chancerainuv)
        #print 'weather =', weather
    
        if weather == 'rains':
            typerain = type(lv, chancetypeuv)
            #print 'type of rain =', typerain
            
            amountrain = amount(typerain)
            #print 'amount of rain =' , amountrain
            
            gainh = gain(amountrain)
            #print 'gainh =', gainh
        
        newh = oldh - loseh + gainh
#        print 'the new height = oldh', oldh, '- loseh', loseh, \
#        '+ gainh', gainh, '= ', newh
        
#        print 'oldh =',oldh
#        print 'newh =', newh
    
        if newh > maxh:
            max2ndh = maxh
            maxh = newh
        elif newh > max2ndh and newh <= maxh:
            max2ndh = newh
        
#        print 'updated maxh =', maxh
#        print 'updated max2ndh =', max2ndh
        
        oldh = newh
        
#    print 'updated maxh =', maxh
#    print 'updated max2ndh =', max2ndh
    
    
    maxmax.append(maxh)
    max2nd.append(max2ndh)
    
print 'maxmax =', maxmax
print 'max2nd =', max2nd

# SUM AND AVG OF max2nd ARRAY
summax2nd = 0

for i in range (0,len(max2nd)):
    summax2nd = summax2nd + max2nd[i]
    #print summax2nd
#print 'summax2nd = ', summax2nd

avgmax2nd = summax2nd / len(max2nd)
print 'avgmax2nd = ', avgmax2nd

# VARIANCE OF max2nd ARRAY
totalvarmax2nd = 0
n = 0
for i in range (0,len(max2nd)):
    n = (max2nd[i] - avgmax2nd)**2
#    print 'n =', n
    totalvarmax2nd = totalvarmax2nd + n
#    print 'totalvarmax2nd =', totalvarmax2nd

varmax2nd = totalvarmax2nd / (len(max2nd)-1)
print 'varmax2nd =', varmax2nd

#print 'Sum of var diff = ', totalvarmax2nd
#print 'Var = ', varmax2nd

# STD DEV OF max2nd ARRAY

stdmax2nd = varmax2nd**0.5
print 'stdmax2nd =', stdmax2nd

#Variance ==> Sum{i = 1,n} (xi - xbar)^2 / (n-1)

#Example:
# ave = 136
# n1 = 18 --> (18 - 136)^2
# n2 = 91 --> (91 - 136)^2
# . . .

#    totalvar = 0
#    for i in range(0, len(histgames)):
#        totalvar = totalvar + (histgames[i]-ave)**2
#        #print total
#    var = totalvar / (len(histgames)-1)
#    print 'Sum of var diff = ', totalvar
#    print 'Var = ', var

# Standrad Deviation = SQRT(var)
#    std = var**0.5
#    print 'Standard Deviation =', std

 


#    if money == 0:
#        history.append('L')
#    if money == 250:
#        history.append('W')
#    histgames.append(gamesplayed)

#    print history
#    count = 0
#    maximum = 0
#    for i in range(0, len(history)):
#        #history[i]
#        if history[i] == 'L':
#            count = 0
#        if history[i] == 'W':
#            count += 1
#        if count > maximum:
#            maximum = count
#    print 'Longest winning streak = ', maximum
#    print 'histgames = ', histgames
#    totalgames = 0
#    for i in range(0, len(histgames)):
#        totalgames = totalgames + histgames[i]
#        #print total
#    ave = totalgames / len(histgames)
#    print 'Total games = ', totalgames
#    print 'Average number of games = ', ave
    
#print 'program over'


