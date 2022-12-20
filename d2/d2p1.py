def txtToListF():
  with open('d2.txt', 'r') as file:
    rounds = []
    for line in file:
      strLine = str(line)
      rounds.append([strLine[0], strLine[2]])
    return rounds

# A X = rock 1
# B Y = paper 2
# C Z = scissors 3
def main():
  def calcPointsRound(round):
    opponent = round[0]
    me = round[1]
    if opponent == 'A':
      if me == 'X':
        return 1 + 3
      elif me == 'Y':
        return 2 + 6
      else:
        return 3 + 0
    elif opponent == 'B':
      if me == 'X':
        return 1 + 0
      elif me == 'Y':
        return 2 + 3
      else:
        return 3 + 6
    elif opponent == 'C':
      if me == 'X':
        return 1 + 6
      elif me == 'Y':
        return 2 + 0
      else:
        return 3 + 3

  res = 0
  for round in txtToListF():
    res += calcPointsRound(round)


  return res

print(main())