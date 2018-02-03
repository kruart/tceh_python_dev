riddles_and_answer = {
    'Яку мову ми вивчаємо?': 'Python',
    'Який тип даних використовується для цілих чисел?': 'int',
    'Остання версія Python, 2 чи 3': '3',
    'Все в Python є ...?': 'object',
    'Мапа в Python називається ...?': 'dict',
    'Як назвиється тип з плаваючою точкою': 'double',
    'Метод для виводу інфи на екран': 'print',
    'Які є цикли в Python?': 'for, while',
    'Як позначається list в Python?': '[]',
    'Як позначається tuple в Python?': '()'
}

count_right_answers = 0


for k, v in riddles_and_answer.items():
    answer = input(k)
    if v.lower() == answer.lower():
        count_right_answers += 1
        print("It's right!")
    else:
        print('Answer is wrong!')

print('Ваш результат:', count_right_answers, 'правильних відповідей з 10 питань!')