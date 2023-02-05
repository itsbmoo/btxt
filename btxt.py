import os
import re
import sys
import colorama

colorama.init(autoreset=True)



class Lexer:
    def __init__(self, filename) -> None:
        self.filename = filename
        self.counter = 0
        
    def analyze(self, rows: list[str]) -> str:
        for row in rows:
            print(row)
    
    
    def read_file(self) -> str|None:
        try:
            with open(self.filename, 'r') as f:
                Lexer.analyze(self, f.read().splitlines())
                f.close()
        except Exception as e:
            print(f'{colorama.Fore.RED}ERROR: {e}')


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
