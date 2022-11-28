def baby_shark_lyrics():
    arr_shark = ['Baby shark', 'Mommy shark', 'Daddy shark', 'Grandma shark',
                'Grandpa shark', 'Let\'s go hunt']
    answer = ''
    for i in arr_shark:
        answer += (i + ',' + ' doo' * 6 + '\n') * 3 + i + '!\n'
    return answer + 'Run away,…'
