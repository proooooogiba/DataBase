from mimesis import Person
from mimesis import Text
from mimesis import Food
from faker import Faker
import pandas as pd
import random
import json

person = Person('ru')
rand_text = Text()
food = Food()
faker = Faker()

speciality = [
    'Biologist',
    'Biomedical scientist',
    'Botanist',
    'Clinical pharmaceutical scientist',
    'Herpetologist',
    'Medical laboratory scientist',
    'Microbiologist',
    'Neuroscientist',
    'Physician',
    'Veterinarian',
    'Zoologist',
    'Aeronautical engineer',
    'Biomedical engineer',
    'Chemical engineer',
    'Civil engineer',
    'Computer engineer',
    'Educational technologist',
    'Electrical engineer',
    'Engineering technician',
    'Engineering technologist',
    'Mechanical engineer',
    'Petrochemical engineer',
    'Computational scientist',
    'Data scientist',
    'Economist',
    'Epidemiologist',
    'Geographer',
    'Geoscientist',
    'Historian',
    'Linguist',
    'Mathematician',
    'Medical statistician',
    'Operations researcher',
    'Psychologist',
    'Sociologist',
    'Statistician',
    'Anthropologist',
    'Archaeologist',
    'Archivist',
    'Conservator',
    'Curator',
    'Librarian',
    'Museum professional',
    'Architect',
    'Cartographer',
    'City planner',
    'Landscape architect',
    'Urban designer',
    'Astronomer',
    'Astrophysicist'
]

degree = ('phd', 'bachelor', 'master', 'college', 'proffesional', 'doctoral')
weight_degree = [0.1, 0.6, 0.3, 0.4, 0.3, 0.1]

def scientist(start, number_of_rows):
    return [{
        'code': x + 1,
        'name': person.first_name() + ' ' + person.last_name(),
        'degree': random.choices(degree, weights=weight_degree)[0],
        'speciality': random.choices(speciality)[0],
        'country': faker.country(),
        'workplace': faker.company(),
        'email': person.email(),
        'phone': person.telephone(),
        'menu': json.dumps({
            'breakfast': food.dish(),
            'lunch': food.dish(),
            'dinner': food.dish(),
            'drink': food.drink()
                }),
        'articles': [rand_text.title() for i in range(random.randint(1, 10))],
              } for x in range(start, start + number_of_rows, 1)
            ]

pd.DataFrame(scientist(0, 5000000)).to_csv('example.csv', index=False)

for i in range(1, 20):
  pd.DataFrame(scientist(5000000 * i, 5000000)).to_csv('example.csv', index=False, mode='a', header=False)
