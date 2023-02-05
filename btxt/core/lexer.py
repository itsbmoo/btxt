from colorama import Fore


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
            print(f'{Fore.RED}ERROR: {e}')
