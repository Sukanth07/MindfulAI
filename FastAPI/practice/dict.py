dataset = {
    1: {
        'name': 'Sukanth',
        'reg_no': 50,
        'height': 170.0,
        'age': 20
    },
    2: {
        'name': 'Soorya',
        'reg_no': 45,
        'height': 165.45,
        'age': 21
    }
}

updated_data = {
    'age': 23
}

dataset[1].update(updated_data)
print(dataset)