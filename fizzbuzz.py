
def generate_list_of_numbers():
    return range(1, 100)


def num_to_fizz_string(number):
    if number % 3 == 0 and number % 5 == 0:
        return 'FizzBuzz'
    if number % 3 == 0:
        return 'Fizz'
    if number % 5 == 0:
        return 'Buzz'

    return str(number)


def run_fizzbuzz():
    numbers = generate_list_of_numbers()

    for number in numbers:
        num_str = num_to_fizz_string(number)
        print(num_str)


if __name__ == '__main__':
    run_fizzbuzz()






