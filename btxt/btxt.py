import os
import sys
import colorama
from core.lexer import Lexer

colorama.init(autoreset=True)


def usage(error: str|None) -> str|None:
    [print(f'{colorama.Fore.RED}ERROR: {error}') if error != None else None]
    print('USAGE:\n\t* btxt <filename>     -     Render the file;')

    
if __name__ == '__main__':
    os.system('cls')
    match len(sys.argv):
        case 2:
            Lexer(sys.argv[1]).read_file()
        case _:
            usage('you have to provide an argument (filename)')
