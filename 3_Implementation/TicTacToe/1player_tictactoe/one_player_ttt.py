import main
import takeinput


def ConsoleFront():
    while True:
        x = takeinput.take_input()
        if x.lower() == 'y':
            board = [' ' for x in range(10)]
            print('--------------------')
            main.main_function(board)
        else:
            break


ConsoleFront()
