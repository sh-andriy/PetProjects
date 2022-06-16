f = open('../../../../Andriy/Projects/PetProjects/FileManagement/data.txt', 'r')
text = f.read()
c1 = text.count('n')
c2 = text.count('N')
print(c1 + c2)

f.close()

