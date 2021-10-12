user_input = input('Sentence: ')

words = user_input.split()
for klt, word in enumerate(words):
    print(f'#{klt} - {word[:10]}')