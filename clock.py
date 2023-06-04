import time
import os
hour=0
mi=0
sec=0
bool=True
count=0
if bool==True:
    while bool:
        hour=0
        while hour<=12:
            mi=0
            while mi<=60:
                sec=0
                while sec<=60:
                     os.system('clear')
                     if count%2==0:
                         print( str(hour)+':'+str(mi)+':'+str(sec)+'AM')
                     else:                    
                         print(str(hour)+':'+str(mi)+':'+str(sec)+'PM')
                     time.sleep(1)
                     sec+=1
                mi+=1
            hour+=1
    count+=1
    


                
    
                

        