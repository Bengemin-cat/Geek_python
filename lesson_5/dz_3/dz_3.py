tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
Classes = [
    '9А', '7В', '9Б', '9В', '8Б', '10А'
]

gen = ((tutors[i], Classes[i]) if len(Classes) > i else (tutors[i], None) for i in range(len(tutors)))

print(type(gen))

for i in range(len(tutors) + 1):
    print(next(gen, 'Истощился'))
