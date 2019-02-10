import xml.etree.ElementTree

e = xml.etree.ElementTree.parse('Music Library.xml').getroot()

query = int(input('Select\n1. Song name\n2. Artist name\n3. Both\n'))

if query == 1:
    f = open('result.txt', 'a')
    f.write('Song\n')
    count=0
    for i in range(1839):
        if i%2==1:
            flag = False
            for child in e[0][15][i]:
                if flag:
                    count+=1
                    f.write(child.text+'\n')
                    flag = False
                if child.text == 'Name':
                    flag = True
    f.close()
elif query == 2:
    f = open('result.txt', 'a')
    f.write('Artist\n')
    count=0
    for i in range(1839):
        if i%2==1:
            flag = False
            for child in e[0][15][i]:
                if flag:
                    count+=1
                    f.write(child.text+'\n')
                    flag = False
                if child.text == 'Artist':
                    flag = True
    f.close()
else:
    f = open('result.txt', 'a')
    f.write('Song\tArtist\n')
    count=0
    for i in range(1839):
        if i%2==1:
            flag1, flag2 = False, False
            for child in e[0][15][i]:
                if flag1:
                    count+=1
                    song = child.text
                    flag1 = False
                if flag2:
                    f.write(song+'\t'+child.text+'\n')
                    flag2 = False
                if child.text == 'Name':
                    flag1 = True
                if child.text == 'Artist':
                    flag2 = True
    f.close()