with open("text.txt") as file:
    file_lines = file.readlines()
    str = 0
    for num , line in enumerate(file_lines):
        str += 1
        words = len(line.split())
        print(f'#{num + 1} - {words} words')
    print(f'{str} line!')



