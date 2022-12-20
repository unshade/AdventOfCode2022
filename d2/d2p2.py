def txtToListF():
  with open('d2.txt', 'r') as file:
    rounds = []
    for line in file:
      strLine = str(line)
      rounds.append([strLine[0], strLine[2]])
    return rounds

# A = rock 1
# B = paper 2
# C = scissors 3
# Z = win
# X = loss
# Y = Draw
def main():
  def calcPointsRound(round):
    opponent = round[0]
    me = round[1]
    if opponent == 'A':
      if me == 'X':
        return 3 + 0
      elif me == 'Y':
        return 1 + 3
      elif me == 'Z':
        return 2 + 6
    elif opponent == 'B':
      if me == 'X':
        return 1 + 0
      elif me == 'Y':
        return 2 + 3
      elif me == 'Z':
        return 3 + 6
    elif opponent == 'C':
      if me == 'X':
        return 2 + 0
      elif me == 'Y':
        return 3 + 3
      elif me == 'Z':
        return 1 + 6

  res = 0
  for round in txtToListF():
    res += calcPointsRound(round)


  return res

print(main())