import random
from tkinter import *
from tkinter import messagebox

score = 0
run = True

while run:
    root = Tk()
    root.geometry('900x700')
    root.title('HANG MAN')
    root.config(bg='#e7fff0')
    count = 0
    win_count = 0

    # choosing word
    index = random.randint(0, 100)
    file = open('words.txt', 'r')
    l = file.readlines()
    select_word = l[index].strip('\n')

    # creation of word dashes variables
    x = 250
    for i in range(0, len(select_word)):
        x += 60
        exec('d{}=Label(root,text="_",bg="#e7fff0",font=("arial",40))'.format(i))
        exec('d{}.place(x={},y={})'.format(i, x, 450))

    # letters icon
    al = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z']
    for let in al:
        exec('{}=PhotoImage(file="{}.png")'.format(let, let))

    # hangman images
    h123 = ['img1', 'img2', 'img3', 'img4', 'img5', 'img6', 'img7']
    for hangman in h123:
        exec('{}=PhotoImage(file="{}.png")'.format(hangman, hangman))

    # letters placement
    button = [['button1', 'A', 0, 595], ['button2', 'B', 70, 595], ['button3', 'C', 140, 595], ['button4', 'D', 210, 595],
              ['button5', 'E', 280, 595], ['button6', 'F', 350, 595], ['button7', 'G', 420, 595], ['button8', 'H', 490, 595],
              ['button9', 'I', 560, 595], ['button10', 'J', 630, 595], ['button11', 'K', 700, 595], ['button12', 'L', 770, 595],
              ['button13', 'M', 840, 595], ['button14', 'N', 0, 645], ['button15', 'O', 70, 645], ['button16', 'P', 140, 645],
              ['button17', 'Q', 210, 645], ['button18', 'R', 280, 645], ['button19', 'S', 350, 645], ['button20', 'T', 420, 645],
              ['button21', 'U', 490, 645], ['button22', 'V', 560, 645], ['button23', 'W', 630, 645], ['button24', 'X', 700, 645],
              ['button25', 'Y', 770, 645], ['button26', 'Z', 840, 645]]

    for q1 in button:
        exec('{}=Button(root,bd=0,command=lambda:check("{}","{}"),bg="#E7FFFF",activebackground="#E7FFFF",font=10,image={})'.format(
                q1[0], q1[1], q1[0], q1[1]))
        exec('{}.place(x={},y={})'.format(q1[0], q1[2], q1[3]))

    # hangman placement
    han = [['c1', 'img1'], ['c2', 'img2'], ['c3', 'img3'], ['c4', 'img4'], ['c5', 'img5'], ['c6', 'img6'], ['c7', 'img7']]
    for p1 in han:
        exec('{}=Label(root,bg="#e7fff0",image={})'.format(p1[0], p1[1]))



    # exit buton
    def close():
        global run
        answer = messagebox.askyesno('ALERT', 'YOU WANT TO EXIT THE GAME?')
        if answer == True:
            run = False
            root.destroy()


    e1 = PhotoImage(file='ExitButton.png')
    ex = Button(root, bd=0, command=close, bg="#e7fff0", activebackground="#e7fff0", font=10, image=e1)
    ex.place(x=770, y=10)
    s2 = 'SCORE:' + str(score)
    s1 = Label(root, text=s2, bg="#e7fff0", font=("arial", 25))
    s1.place(x=10, y=10)


    # button press check function
    def check(letter, button):
        global count, win_count, run, score
        exec('{}.destroy()'.format(button))
        if letter in select_word:
            for i in range(0, len(select_word)):
                if select_word[i] == letter:
                    win_count += 1
                    exec('d{}.config(text="{}")'.format(i, letter.upper()))
            if win_count == len(select_word):
                score += 1
                answer = messagebox.askyesno('CONGRATULATION', 'YOU WON!\nWANT TO PLAY AGAIN?')
                if answer == True:
                    run = True
                    root.destroy()
                else:
                    run = False
                    root.destroy()
        else:
            count += 1

            exec('c{}.place(x={},y={})'.format(count + 1, 300, -50))
            if count == 6:
                answer = messagebox.askyesno('GAME OVER', 'YOU LOST!\nWANT TO PLAY AGAIN?')
                if answer == True:
                    run = True
                    score = 0
                    root.destroy()
                else:
                    run = False
                    root.destroy()


    root.mainloop()

