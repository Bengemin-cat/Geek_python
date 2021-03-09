tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А'
]

g = ((tutors[i], klasses[i]) if len(klasses) > i else (tutors[i], None) for i in range(len(tutors)))

for i in range(len(tutors) + 1):
    print(next(g, 'Истощился'))
