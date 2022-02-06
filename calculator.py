from sys import flags
from tkinter import Event
import PySimpleGUI as sg
#sg.theme_previewer()


sg.theme('GrayGrayGray')

layout =[
    #[sg.Frame('', [],size=(400,600))],
    [sg.Text(key='out',font=('Arial',30),pad=((30,30),(30,30)))],
    [sg.Button('AC',size=(8,4),key='99'),sg.Button('+/-',size=(8,4),key='ps'),sg.Button('%',size=(8,4),key='per'),sg.Button('/',size=(8,4),key='24')],
    [sg.Button('7',size=(8,4),key='7'),sg.Button('8',size=(8,4),key='8'),sg.Button('9',size=(8,4),key='9'),sg.Button('*',size=(8,4),key='23')],
    [sg.Button('4',size=(8,4),key='4'),sg.Button('5',size=(8,4),key='5'),sg.Button('6',size=(8,4),key='6'),sg.Button('-',size=(8,4),key='22')],
    [sg.Button('1',size=(8,4),key='1'),sg.Button('2',size=(8,4),key='2'),sg.Button('3',size=(8,4),key='3'),sg.Button('+',size=(8,4),key='21')],
    [sg.Button('happy',size=(8,4),key='bh'),sg.Button('0',size=(8,4),key='0'),sg.Button('.',size=(8,4),key='bd'),sg.Button('=',size=(8,4),key='29')]
    ]

window = sg.Window('Calculator', layout, resizable=False,size=(400,600))

su1=su2=sign=esi=bd1=bd2=fi=flag=Err=eq=ch2=ff=flag2=0
#suf1=suf2=sumf=0.0
sum1=9999
#sign=
#1:+, 2:-, 3:*, 4:/
#i=range(10)

while True:
    event,values = window.read()

    if event is None:
        print('exit')
        break
    '''
    if event=='ac':
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
        else:
            su2=1
            fi=2
            esi=0
'''
    #if event in range(10):
    if int(event) in range(10):
        if eq==1:
            #su1=su2=flag=flag2=eq=sum1=ch2=0
            su1=su2=flag=eq=sum1=ch2=ff=0
        if flag2==0:         #first
            print('event=',event)
            su1=su1*10+int(event)
            window['out'].update(su1)
        else:
            print('event=',event)
            ch2=1
            su2=su2*10+int(event)
            window['out'].update(su2)
    elif int(event) in range(21,25):
        print('event=',event)
        if eq==0:
            if flag2==0:
                flag2=int(event)
                print('flag2=',flag)
                print('range21-25-1')
            #elif ff==1:
                #flag=flag2
                #flag2=ff=0
                #flag2=int(event)
                #print('flag=',flag)
                #print('flag2=',flag2)
                #print('ff=',ff)
            else:
                flag=flag2
                flag2=int(event)
                print('flag=',flag)
                print('flag2=',flag2)
                ff=1
                print('ff=',ff)
                print('range21-25-2')

            if ch2==1:
                if ff==1:
                    if flag==21:
                        su1+=su2
                    elif flag==22:
                        su1-=su2
                    elif flag==23:
                        su1*=su2
                    elif flag==24:
                        su1/=su2
                elif flag2==21:
                    su1+=su2
                elif flag2==22:
                    su1-=su2
                elif flag2==23:
                    su1*=su2
                elif flag2==24:
                    su1/=su2
                su2=0
                window['out'].update(su1)
        elif eq==1:
            su1=sum1
            eq=su2=0
            flag2=int(event)

    elif event=='29':
        print('event=',event)
        eq=1
        if flag2==0:
            flag=flag2
        if flag2 == 21:    
            sum1=su1+su2
        elif flag2 ==22:     
            sum1=su1-su2
        elif flag2==23:
            sum1=su1*su2
        elif flag2==24:
            sum1=su1/su2
        else:
            window['out'].update('Error')
            Err=1
        if Err==1:
            Err=su1=su2=flag=0
            pass
        else:
            window['out'].update(sum1)
            flag=flag2=ff=ch2=0
            print('flag=',flag)
    elif event=='99':
        su1=su2=flag=eq=sum1=ch2=ff=flag2=0
        window['out'].update(sum1)
        print('\n-----AC-----\n')
        
'''
    elif event=='b2':
        window['out'].update('2')
        if su1==0:
            su1=2
            fi=1
        elif esi==1:
            sum1=su1=su2=esi=0
            su1=2
        elif fi==1:
            su1=su1*10+2
            window['out'].update(su1)
        elif fi==2:
            su2=su2*10+2
            window['out'].update(su2)
        else:
            su2=2
            fi=2
            esi=0
    elif event=='b3':
        window['out'].update('3')
        if su1==0:
            su1=3
            fi=1
        elif esi==1:
            sum1=su1=su2=esi=0
            su1=3
        elif fi==1:
            su1=su1*10+3
            window['out'].update(su1)
        elif fi==2:
            su2=su2*10+3
            window['out'].update(su2)
        else:
            su2=3
            fi=2
            esi=0
    elif event=='b4':
        window['out'].update('4')
        if su1==0:
            su1=4
            fi=1
        elif esi==1:
            sum1=su1=su2=esi=0
            su1=4
        elif fi==1:
            su1=su1*10+4
            window['out'].update(su1)
        elif fi==2:
            su2=su2*10+4
            window['out'].update(su2)
        else:
            su2=4
            fi=2
            esi=0'''



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