def number_sequence(elements: int) -> str:
    rezult = ''
    for element in range(1, elements + 1):
        rezult += str(element) * element
    return rezult


if __name__ == '__main__':
    elements = int(input('Введите число:\n'))
    print(number_sequence(elements))
