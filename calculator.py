'''
calculator.py

Copyright (c) 2022 s1gnsgrfu

This software is released under the GNU LGPLv3.
see https://github.com/s1gnsgrfu/Calculator/blob/master/LICENSE
'''

import PySimpleGUI as sg

def hpy():
    #sg.popup('Are you Ready???',title="OK?",keep_on_top=True)
    hlayout = [
        [sg.Text('Happy?',font=('Segoe UI Variable Small Light',29),pad= ((30,30),(30,30)),background_color='azure2')],
        [sg.Button('Yes',size=(10,6),key='Y',button_color=('black','Slategray1')),sg.Button('No',size=(10,6),key='N',button_color=('black','Slategray1'))]
        ]

    hwindow = sg.Window('Happy?', hlayout, resizable=False,size=(215,250),background_color='azure2')
     
    while True:
        event,values=hwindow.read()

        if event is None:
            print('exit')
            break
        elif event =='N':
            #print('exit')
            gon()
            break

        if event=='Y':
            go()
            break
    hwindow.close()
    return 0

def gon():
    go=[[sg.Text('Oh... I wish you will be happy.',font=('Segoe UI Variable Small Light',50),pad= ((30,30),(30,30)))]]
    gow = sg.Window('hahaha',go,resizable=False)

    while True:
        event,values=gow.read()

        if event is None:
            print('exit')
            gow.close()
            break
    gow.close()
    return 0

def go():
    go=[[sg.Text('HAPPY HAPPY HAPPY!!!',font=('Segoe UI Variable Small Light',50),pad= ((30,30),(30,30)))]]
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
    [sg.Text(key='out',font=('Segoe UI Variable Small Light',40),pad=((30,30),(30,30)),background_color='azure2')],
    [sg.Button('AC',size=(8,4),key='99',button_color=('black','Slategray3')),sg.Button('+/-',size=(8,4),key='31',button_color=('black','Slategray3')),sg.Button('%',size=(8,4),key='32',button_color=('black','Slategray3')),sg.Button('/',size=(8,4),key='24',button_color=('black','Slategray3'))],
    [sg.Button('7',size=(8,4),key='7',button_color=('black','Slategray1')),sg.Button('8',size=(8,4),key='8',button_color=('black','Slategray1')),sg.Button('9',size=(8,4),key='9',button_color=('black','Slategray1')),sg.Button('*',size=(8,4),key='23',button_color=('black','Slategray3'))],
    [sg.Button('4',size=(8,4),key='4',button_color=('black','Slategray1')),sg.Button('5',size=(8,4),key='5',button_color=('black','Slategray1')),sg.Button('6',size=(8,4),key='6',button_color=('black','Slategray1')),sg.Button('-',size=(8,4),key='22',button_color=('black','Slategray3'))],
    [sg.Button('1',size=(8,4),key='1',button_color=('black','Slategray1')),sg.Button('2',size=(8,4),key='2',button_color=('black','Slategray1')),sg.Button('3',size=(8,4),key='3',button_color=('black','Slategray1')),sg.Button('+',size=(8,4),key='21',button_color=('black','Slategray3'))],
    [sg.Button('Happy',size=(8,4),key='999',button_color=('black','Slategray1')),sg.Button('0',size=(8,4),key='0',button_color=('black','Slategray1')),sg.Button('.',size=(8,4),key='33',button_color=('black','Slategray1')),sg.Button('=',size=(8,4),key='29',button_color=('black','cadet blue'))]
    ]

window = sg.Window('Calculator', layout, resizable=False,size=(350,550),background_color='azure2')

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
