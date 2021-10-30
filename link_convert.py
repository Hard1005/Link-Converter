filename = input("File Name:- ")
fhand = open(filename , 'r')
data = fhand.readlines()

fhand = open(filename.split('.txt')[0] + '_output.txt', 'w')
nlink = ''
for link in data:
    x = link.split('/')
    id = x[5]
    nlink += x[0] + '//' + x[2] + '/' + 'uc?id=' + id + '&export=download'
    fhand.write(nlink + '\n')
    nlink = ''
print("Done")