# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 16:27:36 2017

@author: derekc
"""
from __future__ import print_function
from __future__ import division
import random

def getrand():
    randnum = random.randint(1, (factor*10))
    #num = intval
#    print(randnum)
    return (randnum)

def aboutcome(batter):
    randnum = getrand()
    
    if batter == 4 or batter == 8:
#        print('batter is mac')
        sng = 0.1264
        dbl = 0.0407
        trp = 0.0010
        hr = 0.0942

    else:
#        print('batter is gwyn')
        sng = 0.2024
        dbl = 0.0585
        trp = 0.0145
        hr = 0.0628
    
    A = int(sng * factor*10)
    B = int(A + (dbl * factor*10))
    C = int(B + (trp * factor*10))
    D = int(C + (hr * factor*10))
    E = int(factor*10)
        
    if randnum <= A:
        AB = 'single'
    elif randnum > A and randnum <= B:
        AB = 'double'
    elif randnum > B and randnum <= C:
        AB = 'triple'
    elif randnum > C and randnum <= D:
        AB = 'homerun'
    elif randnum > D:
        AB = 'out'
#    print('AB =', AB)
    return(AB)

#main
reps = []

for rep in range (0,30):   #30
    
    runsgame = []
    totab = []
    tot1b = []
    tot2b = []
    tot3b = []
    tothr = []
    totout = []
    
    for numgames in range (0,100):   #100
        factor = 1000
        runs = inning = outs = 0
        abcnt = sngcnt = dblcnt = trpcnt = hrcnt = outcnt = 0
        
        batter = 1
        
        while inning != 9:   #10
            inning += 1
            outs = 0
            
            first = 'empty'
            second = 'empty'
            third = 'empty'
        
    #        print()
    #        print('inning =', inning)
        
    #        print(first, second, third)
            
            while outs != 3:
    #            print('outs =', outs)
#                print('batter =', batter)
                AB = aboutcome(batter)
                abcnt += 1
    #            print('AB =', AB)
        
                if AB == 'single':
                    sngcnt += 1
                    if third == 'runner':
                        runs += 1
                        third = 'empty'
                    if second == 'runner':
                        third = 'runner'
                        second = 'empty'
                    if first == 'runner':
                        second = 'runner'
                        first = 'empty'
                    first = 'runner'
                    
    #                print(first, second, third)
        
                elif AB == 'double':
                    dblcnt += 1
                    if third == 'runner':
                        runs += 1
                        third = 'empty'
                    if second == 'runner':
                        runs += 1
                        second = 'empty'
                    if first == 'runner':
                        third = 'runner'
                        first = 'empty'
                    second = 'runner'
                     
    #                print(first, second, third)
                    
                elif AB == 'triple':
                    trpcnt += 1
                    if third == 'runner':
                        runs += 1
                        third = 'empty'
                    if second == 'runner':
                        runs += 1
                        second = 'empty'
                    if first == 'runner':
                        runs += 1
                        first = 'empty'
                    third = 'runner'
                    
    #                print(first, second, third)
        
                elif AB == 'homerun':
                    hrcnt += 1
                    if third == 'runner':
                        runs += 1
                        third = 'empty'
                    if second == 'runner':
                        runs += 1
                        second = 'empty'
                    if first == 'runner':
                        runs += 1
                        first = 'empty'
                    runs += 1
                    
    #                print(first, second, third)
        
                elif AB == 'out':
                    outcnt += 1
                    outs +=1
                 
                if batter < 9:
                    batter += 1
                elif batter == 9:
                    batter = 1
    #                print(first, second, third) 
        
    #    print('runs =', runs)
                
        runsgame.append(runs)
        totab.append(abcnt)
        tot1b.append(sngcnt)
        tot2b.append(dblcnt)
        tot3b.append(trpcnt)
        tothr.append(hrcnt)
        totout.append(outcnt)
        
    print(runsgame)
    print(totab)
    print(tot1b)
    print(tot2b)
    print(tot3b)
    print(tothr)
    print(totout)
    
    # SUM AND AVG OF runsgame ARRAY
    sumrunsgame = 0   #summation of all of the runs
    sumtotab = 0
    sumtot1b = 0
    sumtot2b = 0
    sumtot3b = 0
    sumtothr = 0
    sumtotout = 0
    
    print('num of games =', len(runsgame))
    
    for i in range (0,len(runsgame)):   #len(runsgame) is the length of the array
        sumrunsgame = sumrunsgame + runsgame[i]
        sumtotab = sumtotab + totab[i]
        sumtot1b = sumtot1b + tot1b[i]
        sumtot2b = sumtot2b + tot2b[i]
        sumtot3b = sumtot3b + tot3b[i]
        sumtothr = sumtothr + tothr[i]
        sumtotout = sumtotout + totout[i]
        
    avgrunsgame = sumrunsgame / len(runsgame)   #avg of runs
    print('avgrunsgame = ', avgrunsgame)
    
    avgtotab = sumtotab / len(runsgame)   #avg of runs
    print('avgtotab = ', avgtotab)
    
    avgtot1b = sumtot1b / len(runsgame)   #avg of runs
    print('avgtot1b = ', avgtot1b)
    
    avgtot2b = sumtot2b / len(runsgame)   #avg of runs
    print('avgtot2b = ', avgtot2b)
    
    avgtot3b = sumtot3b / len(runsgame)   #avg of runs
    print('avgtot3b = ', avgtot3b)
    
    avgtothr = sumtothr / len(runsgame)   #avg of runs
    print('avgtothr = ', avgtothr)
    
    avgtotout = sumtotout / len(runsgame)   #avg of runs
    print('avgtotout = ', avgtotout)
    
    #sng = 0.2024
    #dbl = 0.0585
    #trp = 0.0145
    #hr = 0.0628
    #out = 0.6618
    #sngper = float(avgtot1b/avgtotab)
    
    print ('sngper =', (float(avgtot1b/avgtotab)))
    print ('dblper =', (float(avgtot2b/avgtotab)))
    print ('trpper =', (float(avgtot3b/avgtotab)))
    print ('hrper =', (float(avgtothr/avgtotab)))
    print ('outper =', (float(avgtotout/avgtotab)))
    
    print('mix\'s sngper = 0.1646')
    print('mix\'s dblper = 0.0496')
    print('mix\'s trpper = 0.0077')
    print('mix\'s hrper = 0.0785')
    print('mix\'s outper = 0.6996')
    
    reps.append(avgrunsgame)
    
#    max2nd.append(max2ndh)   #after 100 years add max2ndh to max2nd array
print()
print('reps =', reps)

#print 'max2nd =', max2nd  #all 30 rep's values for max2ndh

sumreps = 0
for i in range (0, len(reps)):
    sumreps = sumreps + reps[i]
avgreps = sumreps / len(reps)
print('avgreps =', avgreps)


## SUM AND AVG OF max2nd ARRAY
#summax2nd = 0   #summation of all of the max2ndh
#for i in range (0,len(max2nd)):   #len(max2nd) is the length of the array
#    summax2nd = summax2nd + max2nd[i]
#avgmax2nd = summax2nd / len(max2nd)   #avg of max2nd
#print 'avgmax2nd = ', avgmax2nd
