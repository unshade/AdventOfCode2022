def txtToListF():
  with open('d1.txt', 'r') as file:
    elfs = []
    elf = []
    for line in file:
      if not line == '\n':
        elf.append(int(line))
      else :
        elfs.append(elf)
        elf = []
    return elfs

def main():

  def elfsTotalF(elfs):
    res = []
    for elf in elfs:
      res.append(sum(elf))

    return res
  
  def biggestCaloryElfF(elfsTotal):
    maximum = max(elfsTotal)
    i = elfsTotal.index(maximum)
    return i, maximum

  return biggestCaloryElfF(elfsTotalF(txtToListF()))

print(main())