#This function will repeat for each person
Score = 0


#while function that will be true 
running = True

while running:
  Choice = int(input("1 or 2?: "))
  if Choice > 20:
    running == True 
    #adding our inputted number to the score
    Score += Choice
  print(Score)
else:
  running = False
  
  
#Make the function stop when 20 is hit