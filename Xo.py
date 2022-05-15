from tkinter.messagebox import showinfo
import tkinter as tk

win=tk.Tk()

win.title('بازی دوز')
win.minsize(240, 250)
win.maxsize(240, 250)

global turn, results, player_points
turn='X'
results=['', '', '', '', '', '', '', '', '']
player_points=[0, 0]


def clicked(btn):
    global turn
    btn=int(btn)

    if results[btn] == '':
        if turn == 'X':
           results[btn]='X'
           buttons[btn]['bg']='black'
           buttons[btn]['fg']='white'
           buttons[btn]['text']='X'
           buttons[btn]['relief']=tk.GROOVE
           buttons[btn]['state']=tk.DISABLED
           turn='O'
        else:
           results[btn]='O'
           buttons[btn]['bg']='blue'
           buttons[btn]['fg']='white'
           buttons[btn]['text']='O'
           buttons[btn]['state']=tk.DISABLED
           turn='X'
    rule()

def rule():
    if (results[0]==results[1]==results[2] and results[0]!=''):
        winner(results[0])
    elif (results[3]==results[4]==results[5] and results[3]!=''):
        winner(results[3])
    elif (results[6]==results[7]==results[8] and results[6]!=''):
        winner(results[6])
    elif (results[0]==results[3]==results[6] and results[0]!=''):
        winner(results[0])
    elif (results[1]==results[4]==results[7] and results[1]!=''):
        winner(results[1])
    elif (results[2]==results[5]==results[8] and results[2]!=''):
        winner(results[2])
    elif (results[0]==results[4]==results[8] and results[0]!=''):
        winner(results[0])
    elif (results[2]==results[4]==results[6] and results[2]!=''):
        winner(results[2])
    else:
        check()

def winner(winner):
    if winner == 'X':
        player_points[0] += 1
        showinfo('اتمام بازی', 'بازیکن شماره 1 پیروز شد')
        reset()
    else:
        player_points[1] += 1
        showinfo('اتمام بازی', 'بازیکن شماره 2 پیروز شد')
        reset()
        
def reset():
    global results, turn

    results=['', '', '', '', '', '', '', '', '']
    turn='X'
    points()
    board()

def check():
    if '' not in results:
        showinfo('اتمام بازی', 'بازی مساوی شد!')
        reset()

def points():
    global points

    board_frame=tk.Frame(win)
    board_frame.grid(row=0)
    label_player_1=tk.Label(board_frame, text='بازیکن 1', padx=10)
    label_player_2=tk.Label(board_frame, text='بازیکن 2', padx=10)    
    label_player_1.grid(row=0, column=0)
    label_player_2.grid(row=0, column=2)
    point_frame=tk.Frame(win)
    point_frame.grid(row=1)
    player_1=tk.Label(point_frame, text=player_points[0], padx=20)
    player_2=tk.Label(point_frame, text=player_points[1], padx=20)
    player_1.grid(row=0, column=0)
    player_2.grid(row=0, column=1)

def board():
    global buttons
    buttons=[]
    counter=0
    board_frame=tk.Frame(win)
    board_frame.grid(row=2)
    for row in range(1, 4):
        for column in range(1, 4):
            index=counter
            buttons.append(index)
            buttons[index]=tk.Button(board_frame, command=lambda x=f'{index}':clicked(x))
            buttons[index].config(width=10, height=4)
            buttons[index].grid(row=row, column=column)
            counter += 1

points()
board()

win.mainloop()