

"""
Github @ ASHill11
Last revised July 10th, 2024
Only tested for Windows 11 and 10
"""

#TODO: Implement a logging system, and perhaps a way to restore changes from the log

import os, sys


def main():
    info = [0,1,2,3,4]
    marker = 1
    warning = ''
    target = ''
    global debug
    debug = 0

    while True:
        marker_dict = { -9: 'UNHANDLED EVENT!\n', 
                        -1: 'Invalid file path!\n',
                         99:'DEBUG ACTIVATED\n', 
                         1:'',
                         2:'', 
                         3: f'{info[0]}\n{info[1]}\n{info[2]}\n{info[3]} episodes renamed\n{info[4]} files skipped\n{warning}',
                         4:'Changes reverted!\n',
                         5:''}

        os.system('cls||clear')
        print(f'MARKER IS {marker}!') # DEBUG
        print( '------------------------------------------\n'
              f'{marker_dict[marker]}'        
               '------------------------------------------')
        
        if marker == -9:
            print('Exiting due to exception')
            exit()

        if abs(marker) == 1 or marker == 4 or marker == 5 or marker == 99:
            warning = ''
            target, marker = select(target, marker)
            if marker == 99:
                continue

            raw = target.split('\\')
            if len(raw) < 4:
                marker = -1

            if marker == -1:
                continue
            if 'season' not in target.lower():
                warning = 'WARNING: Directory may not be Plex media!\n'

            info[0] = target
            info[1] = raw[-3]
            info[2] = raw[-2]

            ext = target[target.rfind('.'):]

            continue
        

        elif abs(marker) == 2:
            dir = target[:target.rfind('\\') + 1]
            info[3], info[4], backup = rename(info[1], dir, ext)
            marker += 1
            continue

        elif marker == 3:
            while True:
                selection = input('Enter UNDO to revert changes, or input another file path\nEnter \"exit\" to quit\n>')

                if not selection:
                    delete_lines(2)
                    continue
                    
                if selection.isalpha():
                    if selection.lower() == 'undo':
                        revert_changes(backup, dir)
                        marker = 4
                        break

                    if selection.lower() == 'exit':
                       exit('Exiting!')
                    else:
                        delete_lines(2)
                        continue

                else:
                    if not os.path.isfile(selection):
                        marker = -1
                    else:
                        marker = 5
                    break
            continue
        
        else:
            marker = -9

        

def select(target, marker):
    global debug

    if marker == 5:
        pass
    else:
        target = input('Drag and drop or paste path to first episode:\n'
                        '>')
        
    if target == 'DEBUG':
        debug = 1
        
    if target:
        if target[0] == '&':
            target = target[2:].strip('\'')
        
        else:
            if target == 'DEBUG':
                return '', 99
            else:
                target = target.strip('"') 
                
    else:
        return '', -1
    
    if not os.path.isfile(target):
        if target.isalpha():
            if target.lower() == 'exit':
                exit('Exiting!')
        else:
            return '', -1
         
    return target, 2



def rename(name, dir, ext):
    global debug

    named = 0
    skipped = 0

    backup = []
    for file in os.listdir(dir):
        backup.append(file)
    
    e = 1
    for file in os.listdir(dir):
        checked_ext = file[file.rfind('.'):]
        if checked_ext == ext:
            filename = name + f' S{dir[-3:-1]}E{e:02d}'
            if debug == 1:
                pass
            else:
                os.replace(dir + file, dir + filename + ext)
            named += 1
        else:
            print(f'Skipped over {file}') # DEBUG
            skipped += 1
        e+=1
    
    return named, skipped, backup



def revert_changes(backup, dir):
    iterator = 0
    for file in os.listdir(dir):
        os.replace(dir + file, dir + backup[iterator])
        iterator += 1



def delete_lines(n):
    """Delete n lines in the STDOUT."""
    sys.stdout.write(f"\033[{n}A")  # cursor up n lines
    sys.stdout.write("\033[J")  # delete the last line
    


main()