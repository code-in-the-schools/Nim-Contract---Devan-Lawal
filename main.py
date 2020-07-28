Score = 0
running = True
while running:
  choice = int(input("Player 1: "))
  print(choice)
  if choice > 0 and choice < 3:
    Score += choice
    print(Score)
  else:
    print("Please enter 1 or 2")
  if Score == 20:
    running == False
    print("Congratulations! You Won!")
    exit()