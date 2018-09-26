# AdvSimPrj1_3_PY_sims

IMSE  865  ADV  SIM  
Dr.  Easton  PROJECT  1  
Derek  Christensen  

The  goal  of  this  project  is  to  create  three  simulation  models  using  Python  and  a  generic  random  number  generator.  

Part  A  

Design  a  dam  for  the  Army  Corp  of  Engineers  that  would  only  fail  once  every  100  years.  The  model  should  be  run  for  100  years  for  30  replications.  The  lake  height  is  measured  once  each  day  and  the  normal  height  is  1108͛  above  sea  level.  

Assumptions  

 20%  chance  of  precipitation  each  day  

 If  there  is  precipitation,  the  type  is:  
o 75%  Shower  
o 20%  Rain  
o 5%  Downpour  

 Amount  of  precipitation  per  type:
o Shower:  Uniform  Distribution  [0.05͟,  0.  60͟]  
o Rain:  Uniform  Distribution  [0.40͟,  1.20͟]  
o Downpour:  Uniform  Distribution  [1.00͟,  5.00͟]  

 Amount  the  lake  loses  each  day:  
o If  lake  height  is  5͛  or  more  above  normal,  then  it  loses  ½͟
o Otherwise,  ¼͟

 Amount  the  lake  gains  each  day  of  precipitation,  based  on  the  amount  of  precipitation:  
o <  0.40͟:  Gain  =  Precipitaion  
o >=  0.40͟  and  <=  1.00͟:  Gain  =  2  *  Precipitation  
o >  1.00͟:  Gain  =  5*  Precipitaion  

Technical  Report  

The  model  was  written  in  Python  2.7  with  one  library  imported  (Random).  Since  the  goal  is  to  build  a  dam  that  will  fail  once  every  100  years,  we  must  predict  what  the  second  highest  point  would  be  on  average  over  the  30  replications  and  build  to  that  height,  so  we  will  keep  track  of  the  maximum  height  in  each  of  the  30  one-hundred  year  replications  (maxmax)  in  an  array  and  also,  the  2nd  highest  height  reached  in  an  array  as  well  (max2nd).  Randomness  will  be  determined  using  the  random.randint(lv,  uv)  function  from  the  Random  library,  where  lv  and  uv  are  the  lower  and  upper  bounds  (inclusively)  on  the  range  from  which  we  need  a  random  integer  picked.  

The  main  part  of  the  code  is  two  nested  For  loops.  The  outer  loop  is  iterated  30  times  to  generate  the  30  replications  and  the  inner  loop  is  iterated  36,500  times  to  generate  the  100  years  needed.

Part  B  

This  simulation  will  simulate  a  simplified  baseball  game  (hits  and  outs  only)  and  compare  a  contact  hitter  (Gwynn)  and  a  homerun  hitter  (McGwire)  by  using  Gwynn  as  all  9  batters  for  one  team  and  McGwire  as  all  nine  batters  for  the  other  team  and  see  which  one  scores  the  most  runs  on  average  over  100  games.  

A  third  team  is  also  to  be  compared  which  with  the  first  two  batters  being  Gwynn,  the  middle  four  being  McGwire  and  the  last  3  being  Gwynn.  

Assumptions  

 McGwire  Career  Stats  
o Single  .1269  
o Double  .0407  
o Triple  .0010  
o Home  Run  .0942  
o The  remainder  are  outs.  

 Gwynn’s  Career  Stats  
o Single  .2024  
o Double  .0585  
o Triple  .0145  
o Home  Run  .0628  
o The  remainder  are outs.

Part  C  

This  project  will  simulate  an  M/M/1  queue  from  scratch  using  Python,  for  160  hours.  

Assumptions  

 Arrival  Distribution:  Exponential  4/hr  
 Service  Distribution:  Exponential  5/hr  
 NB:  U(0,1)  Distribution  can  be  converted  into  an  Exponential  Distribution  with  a  rate  of  lambda  as  follows:  -ln(u)/lambda
