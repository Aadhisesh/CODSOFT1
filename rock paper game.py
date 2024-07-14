
from random import randint
print("WELCOME TO GAME")
print("1.RULES\n2.PLAY\n3.EXIT")
while(True):
    a=input("CHOOSE ANY")
    user=0
    computer=0
    tie=0
    Round=0
    while(a.upper()!="EXIT"):
       if(a.upper()=="RULES"):
           print("RULES:\n1]\t1=ROCK\n\t2=PAPER\n\t3=SCISSOR\n2]Rounds should be counted \n3]\ta] ROCK > SCISSOR\n\tb]PAPER > ROCK\n\tc]SCISSOR > PAPER") 
           break
       else:
          while(True):
               c=int(input("CHOOSE 1=ROCK OR 2=PAPER OR 3=SCISSOR"))
               if  c == 1:
                  b = "ROCK"
               elif c == 2:
                  b = "PAPER"
               else:
                  b = "SCISSOR"
               while c > 3 or c < 1:
                   c= int(input('Enter a valid choice please '))
                   if  c == 1:
                      b = "ROCK"
                   elif c == 2:
                      b = "PAPER"
                   else:
                      b = "SCISSOR"
               print("you choosed",b)
               print("COMPUTER CHOOSING ...")
               d=randint(1,3)
               if  d == 1:
                  h="ROCK"
               elif d == 2:
                  h="PAPER"
               else:
                  h="SCISSOR"
               if (b==h):
                  print("IT'S a Draw")
                  f= "DRAW"
               elif (c== 1 and d== 2):
                  print('paper wins ')
                  f= 'Paper'
               elif (c== 2 and d == 1):
                  print('paper wins ', end="")
                  f = 'Paper'
               elif (c == 1 and d == 3):
                  print('Rock wins \n')
                  f = 'Rock'
               elif (c == 3 and d == 1):
                  print('[Rock wins ]\n')
                  f = 'RocK'
               elif (c == 2 and d == 3):
                  print('[Scissors wins ]\n')
                  f= 'Scissors'
               elif (c== 3 and d == 2):
                  print("[Scissors win ]\n")
                  f= 'Rock'
               else:
                  break
            
               if f== "DRAW":
                  print("[IT'S A TIE]")
                  tie+=1
                  
               elif f == d:
                  print("[ USER WIN IN THIS ROUND]")
                  user+=1
                  

               else:
                  print("[ COMPUTER WIN IN THIS ROUND]")
                  computer+=1
                  
               Round+=1
               print ("score card :\nYou =",user,"\nComputer=",computer)
               if(computer==2 ):
                print("computer win")
                print("No of round:",Round)
                break
               else:
                 print("YOU win")
                 print("No of round:",Round)
                 break
       print("DO YOU WANT TO PLAY AGAIN (YES OR NO)?")
       a=input().upper()
       if (a== 'NO' or a.upper()=="EXIT"):
        break
    if (a.upper()=="EXIT" or a=="NO"):
      break
     
