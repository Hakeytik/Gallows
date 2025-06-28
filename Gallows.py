import random
words = ["кот", "собака", "слон", "жираф", "тигр", "лев", "зебра", "панда", "волк", "лиса", "медведь", "олень", "кролик", "енот", "белка", "яблоко", "банан", "апельсин", "груша", "виноград", "манго", "киви", "арбуз", "дыня", "морковь", "огурец", "помидор", "картофель", "перец", "лук", "стол", "стул", "лампа", "книга", "чашка", "телефон", "окно", "дверь", "зеркало", "полка", "ножницы", "карандаш", "бумага", "сумка", "очки", "врач", "учитель", "повар", "инженер", "художник", "музыкант", "актер", "спортсмен", "полицейский", "пожарный", "пилот", "строитель", "журналист", "ученый", "фермер", "россия", "канада", "бразилия", "япония", "германия", "франция", "италия", "испания", "австралия", "индия", "китай", "мексика", "египет", "греция", "турция"]
words = [item.lower() for item in words]

def draw_hangman(lives):
    stages = [
        r"""
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
        =========
        """,
        r"""
        +---+
        |   |
        O   |
       /|\  |
       /    |
            |
        =========
        """,
        r"""
        +---+
        |   |
        O   |
       /|\  |
            |
            |
        =========
        """,
        r"""
        +---+
        |   |
        O   |
       /|   |
            |
            |
        =========
        """,
        r"""
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========
        """,
        r"""
        +---+
        |   |
        O   |
            |
            |
            |
        =========
        """,
        r"""
        +---+
        |   |
            |
            |
            |
            |
        =========
        """
    ]
    print(stages[lives])


empty = '_'
ind = random.randint(0,74)
change_word = words[ind]
leng = len(change_word)
correct = True
check_letters = []
def Gallows(lives):
    print('В выбранном слове:', leng, ' букв')
    guess_word = empty * leng
    guess = list(guess_word)
    while lives != 0 and '_' in guess:

        print("Ваши жизни: ", lives)
        draw_hangman(lives)
        print('Использованные буквы: ', list(set(check_letters)))
        print(guess) # _ _ _ _ _

        letter = input().lower()
#Тут я проверяю чтобы вводили именно символ
        if len(letter) != 1:
            print("Некорректно")
            continue
        if letter in check_letters:
            print("Эта буква уже была!")
        word = list(change_word)
#Тут я проверяю на наличие буквы
        if letter in word:
            check_letters.append(letter)
            count = word.count(letter)
            for i in range(0, count):
                index = word.index(letter, i)
                guess[index] = letter #Тут я вношу угаданную букву
        else:
            if letter not in check_letters:
                lives -= 1
                check_letters.append(letter)
        if lives == 0:
            print('Вы проиграли')
            draw_hangman(0)
    return f"слово было '{change_word}'"

print(Gallows(6))



