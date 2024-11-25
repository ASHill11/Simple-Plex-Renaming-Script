
import os, sys, time

def error():
    print('Invalid filepath!')
    print('Exiting...')
    time.sleep(3)
    exit()


def rename(name, dir, ext):
    named = 0
    skipped = 0

    backup = []
    for file in os.listdir(dir):
        backup.append(file)

    e = 1
    for file in os.listdir(dir):
        checked_ext = file[file.rfind('.'):]
        if checked_ext == ext:
            filename = name + f' S{dir[34:36]}E{e:02d}'
            os.replace(dir + file, dir + filename + ext)
            named += 1
        else:
            #print(f'Skipped over {file}') # DEBUG
            skipped += 1
        e+=1
    
    return named, skipped, backup


def revert_changes(backup, dir):
    iterator = 0
    for file in os.listdir(dir):
        os.replace(dir + file, dir + backup[iterator])
        iterator += 1


def main():
    target = sys.argv[1]

    raw = target.split('\\')
   
    if len(raw) < 4:
        error()

    info = [0,1,2,3,4]
    info[0] = target
    info[1] = raw[-3]
    info[2] = raw[-2]
    ext = target[target.rfind('.'):]
    dir = target[:target.rfind('\\') + 1]

    info[3], info[4], backup = rename(info[1], dir, ext)

    flag = 0
    while True:
        os.system('cls||clear')
        print('------------------------------------------')
        print(f'{info[0]}\n{info[1]}\n{info[2]}\n{info[3]} episodes renamed\n{info[4]} files skipped')
        print('------------------------------------------')
        if flag == 1: print('PRESS ENTER AGAIN TO EXIT')
        selection = input('Enter UNDO to revert changes or EXIT to quit:\n>')

        if selection.lower() == 'undo':
            revert_changes(backup, dir)
            print('\nChanges reverted!')
            print('------------------------------------------\nExiting...')
            time.sleep(3)
            exit()
        if selection.lower() == 'exit':
            exit()
        
        if flag == 1:
            exit()
        else:
            flag = 1

               
main()