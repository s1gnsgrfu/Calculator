print('This is a Calculator.')

'''
char=input('>>')

print('\nYou entered',char,'.')
'''

print('\nEnter numbers.')
print('If you need helping , enter "- -".')

#f1,f2=(int(x) for x in input().split())
f1,f2=(int (x) for x in input('>>').split())

#print('You entered',f1,',',f2,'.')
print('\nSymbols of four arithmetic operations.')
si=input('>>')

if si == '+':
    fi=f1 + f2
elif si == '-':
    fi=f1 - f2
elif si == '*':
    fi=f1 * f2
elif si == '/':
    fi=f1 / f2
else:
    print('Error occured')

print('\n\n----------result----------')
print(f1,si,f2,'=',fi)
