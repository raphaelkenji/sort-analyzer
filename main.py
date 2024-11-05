from lexer import lexer
from parser import parser

def main():
    print("Example: compare 10 bubble_sort, selection_sort, insertion_sort")
    print("Enter a command (or type 'exit' to quit):")
    while True:
        s = input('>')
        if s.lower() == 'exit':
            break
        elif s.strip():
            parser.parse(s, lexer=lexer)
            print('\n')
        else:
            print("Invalid input. Please enter a valid command.")
                
if __name__ == '__main__':
    main()