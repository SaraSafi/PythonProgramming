import string
ch='abcdefghijklmnopqrstuvwxyz'
print('ch:',ch)
res=''
res1=''
l=[]
tile=input('tile: ')
for k in tile:
    l.append(k)
    l.sort()
print('l:',l)

sub1=tile[0]
sub2=tile[-1]
print('the first and last char:',sub1,sub2)
p1=ch.index(sub1)+1
p2=ch.index(sub2)+1
print('the first and last index:',p1,p2)
#ordered char like AFGO
if l[0]==sub1:
    res = ch[p1-1: p2]
    print('main:',res)
    print('limited chars:',res)
    for char in l:
        if char in res:
            idx = tile.index(char) + 1
            print(f'tile of jumping:{idx}', end=' \n')
    for letter in res:
        if letter in tile:
            index_of_letter = ch.index(letter) + 1
            print(f'the index of {letter} in alphabet order: {index_of_letter}')
#for reversing char like LOGIC
else:
    res=ch[p2-1:p1]
    res1=res[::-1]
    print('reverse:',res1)
    for char in res1:
        if char in tile:
            idx = tile.index(char) + 1
            print(f'tile of jumping:{idx}',end=' \n')
    for letter in res1:
        if letter in tile:
            index_of_letter = ch.index(letter) + 1
            print(f'the index of {letter} in alphabet order: {index_of_letter}')














