import PySimpleGUI as sg
#sg.theme_previewer()


sg.theme('GrayGrayGray')

layout =[
    #[sg.Frame('', [],size=(400,600))],
    [sg.Text(key='out',font=('Arial',30),pad=((30,30),(30,30)))],
    [sg.Button('AC',size=(8,4),key='ac'),sg.Button('+/-',size=(8,4),key='ps'),sg.Button('%',size=(8,4),key='per'),sg.Button('/',size=(8,4),key='di')],
    [sg.Button('7',size=(8,4),key='b7'),sg.Button('8',size=(8,4),key='b8'),sg.Button('9',size=(8,4),key='b9'),sg.Button('*',size=(8,4),key='ml')],
    [sg.Button('4',size=(8,4),key='b4'),sg.Button('5',size=(8,4),key='b5'),sg.Button('6',size=(8,4),key='b6'),sg.Button('-',size=(8,4),key='su')],
    [sg.Button('1',size=(8,4),key='b1'),sg.Button('2',size=(8,4),key='b2'),sg.Button('3',size=(8,4),key='b3'),sg.Button('+',size=(8,4),key='pl')],
    [sg.Button('happy',size=(8,4),key='bh'),sg.Button('0',size=(8,4),key='b0'),sg.Button('.',size=(8,4),key='bd'),sg.Button('=',size=(8,4),key='eq')]
    ]

window = sg.Window('Calculator', layout, resizable=False,size=(400,600))

su1=su2=sign=esi=bd1=bd2=fi=0
#suf1=suf2=sumf=0.0
sum1=9999
#sign=
#1:+, 2:-, 3:*, 4:/

while True:
    event,values = window.read()

    if event is None:
        print('exit')
        break
    elif event=='ac':
        su1=su2=sum1=esi=sign=fi=0
        window['out'].update('0')
    elif event=='ps':
        if fi==1:
            su1=su1*-1
            window['out'].update(su1)
        elif fi==2:
            su2=su2*-1
            window['out'].update(su2)
    elif event=='per':
        if fi==1:
            su1=su1*0.01
            window['out'].update(su1)
        elif fi==2:
            su2=su2*0.01
            window['out'].update(su2)
#    elif event=='bd':
#        if fi==1:
#            bd1=1
#            window['out'].update(su1)
#        elif fi==2:
#            bd2=1
#            window['out'].update(su2)
#        elif bd1!=0 and bd2!=0:
#            pass
    elif event=='eq':
        if sign==1:
#            if bd1==2:
#                sumf=suf1+suf2
#            else:
                sum1=su1+su2
        elif sign==2:
            sum1=su1-su2
        elif sign==3:
            sum1=su1*su2
        elif sign==4:
            sum1=su1/su2
        else:
            window['out'].update('Error')

        window['out'].update(sum1)
        esi=1
        fi=bd1=bd2=0

    elif event=='pl':
        window['out'].update('+')
        sign=1
        fi=0
        if esi==1:
            su1=sum1
            esi=0
        elif su1!=0 and su2!=0 and esi ==0 and fi!=1:
            su1=su1+su2
            window['out'].update(su1)
    elif event=='su':
        window['out'].update('-')
        sign=2
    elif event=='ml':
        window['out'].update('*')
        sign=3
    elif event=='di':
        window['out'].update('/')
        sign=4

    elif event=='b1':
        window['out'].update('1')
        if su1==0:
            su1=1
            fi=1
        elif esi==1:
            sum1=su1=su2=esi=0
            su1=1
        elif fi==1:
            su1=su1*10+1
            window['out'].update(su1)
        elif fi==2:
            su2=su2*10+1
            window['out'].update(su2)
#        elif bd1==1 or bd2==1:
#            if bd1==1 and bd2!=1:
#                suf1=float(su1)*0.1+0.1
#                bd1=2
#                window['out'].update(suf1)
#            elif bd2==1:
#                suf2=float(su2)*0.1+0.1
#                bd2=2
#                window['out'].update(suf2)
        #elif bd1==2 or bd2:

        else:
            su2=1
            fi=2
            esi=0
    elif event=='b2':
        window['out'].update('2')
        if su1==None:
            su1=2
        else:
            su2=2
    elif event=='b3':
        window['out'].update('3')
        if su1==None:
            su1=3
        else:
            su2=3



window.close()

'''


print('This is a Calculator.')


#char=input('>>')

#print('\nYou entered',char,'.')


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
'''