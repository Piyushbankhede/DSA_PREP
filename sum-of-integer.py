finalScore=0
finallevel=5
currentlevel=1
while (currentlevel  <= finallevel):
   finalScore = finalScore + currentlevel
   currentlevel = currentlevel + 1
  print (finalScore)

# using function in a same code 
def sumint():
    finalScore=0
    finallevel=5
    currentlevel=1
    
    
    while (currentlevel  <= finallevel):
      finalScore = finalScore + currentlevel
      currentlevel = currentlevel + 1
    return finalScore
