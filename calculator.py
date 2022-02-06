#from sys import flags
#from tkinter import Event
import PySimpleGUI as sg
#sg.theme_previewer()

def hpy():
    #sg.popup('Are you Ready???',title="OK?",keep_on_top=True)
    hlayout = [
        [sg.Text('Happy?',font=('Arial',29),pad= ((30,30),(30,30)))],
        [sg.Button('Yes',size=(10,6),key='Y'),sg.Button('No',size=(10,6),key='N')]
        ]

    hwindow = sg.Window('Happy?', hlayout, resizable=False,size=(215,250))
     
    while True:
        event,values=hwindow.read()

        if event is None:
            print('exit')
            break
        elif event =='N':
            print('exit')
            break

        if event=='Y':
            go()
            break
    hwindow.close()
    return 0

def go():
    go=[[sg.Text('You are already HAPPY.',font=('Arial',100),pad= ((30,30),(30,30)))]]
    gow = sg.Window('hahaha',go,resizable=False)

    while True:
        event,values=gow.read()

        if event is None:
            print('exit')
            gow.close()
            break
    gow.close()
    return 0

sg.theme('GrayGrayGray')

layout =[
    #[sg.Frame('', [],size=(400,600))],
    [sg.Text(key='out',font=('Arial',40),pad=((30,30),(30,30)))],
    [sg.Button('AC',size=(8,4),key='99'),sg.Button('+/-',size=(8,4),key='31'),sg.Button('%',size=(8,4),key='32'),sg.Button('/',size=(8,4),key='24')],
    [sg.Button('7',size=(8,4),key='7'),sg.Button('8',size=(8,4),key='8'),sg.Button('9',size=(8,4),key='9'),sg.Button('*',size=(8,4),key='23')],
    [sg.Button('4',size=(8,4),key='4'),sg.Button('5',size=(8,4),key='5'),sg.Button('6',size=(8,4),key='6'),sg.Button('-',size=(8,4),key='22')],
    [sg.Button('1',size=(8,4),key='1'),sg.Button('2',size=(8,4),key='2'),sg.Button('3',size=(8,4),key='3'),sg.Button('+',size=(8,4),key='21')],
    [sg.Button('happy',size=(8,4),key='999'),sg.Button('0',size=(8,4),key='0'),sg.Button('.',size=(8,4),key='33'),sg.Button('=',size=(8,4),key='29')]
    ]

window = sg.Window('Calculator', layout, resizable=False,size=(350,550))

su1=su2=fi=flag=Err=eq=ch2=ff=flag2=sy=sco=0
sum1=9999

while True:
    event,values = window.read()

    if event is None:
        print('exit')
        break

    if int(event) in range(10):
        if eq==1:
            su1=su2=flag=eq=sum1=ch2=ff=sy=0
        if flag2==0:       
            if sy==0:
                if su1>=0:
                    print('event=',event)
                    su1=su1*10+int(event)
                    window['out'].update(su1)
                else:
                    print('event=',event)
                    su1=su1*10+int(event)*-1
                    window['out'].update(su1)
            else:
                if su1>=0:
                    print('event=',event)
                    su1=su1+0.1**sco*int(event)
                    sco+=1
                    window['out'].update(su1)
                else:
                    print('event=',event)
                    su1=su1+0.1**sco*int(event)*-1
                    sco+=1
                    window['out'].update(su1)
        else:
            if sy==0:
                print('event=',event)
                ch2=1
                su2=su2*10+int(event)
                window['out'].update(su2)
            else:
                print('event=',event)
                ch2=1
                su2=su2+0.1**sco*int(event)
                sco+=1
                window['out'].update(su2)
    elif int(event) in range(21,25):
        print('event=',event)
        sy=0
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
            Err=su1=su2=flag=sy=0
            pass
        else:
            window['out'].update(sum1)
            flag=flag2=ff=ch2=sy=0
            print('flag=',flag)
    elif event=='99':
        su1=su2=flag=eq=sum1=ch2=ff=flag2=sy=0
        window['out'].update(sum1)
        print('\n-----AC-----\n')
    elif event=='31':
        if flag2==0:
            su1*=-1
            window['out'].update(su1)
        else:
            su2*=-1
            window['out'].update(su2)
    elif event=='32':
        if flag2==0:
            su1*=0.01
            window['out'].update(su1)
        else:
            su2*=0.01
            window['out'].update(su2)
    elif event=='33':
        sy=sco=1
    elif event=='999':
        hpy()

window.close()
