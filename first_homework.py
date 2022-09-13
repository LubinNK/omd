"""First homework from AAA"""


def get_user_answer():
    """ Call answer from user """
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    return options[option]


def step1():
    """Starting step for duck"""
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    user_answer = get_user_answer()
    if user_answer:
        step2_umbrella()
    else:
        step2_no_umbrella()


def step2_umbrella():
    """Second step for duck with umbrella"""
    print(
        'Утка приняла зонтик!\n'
        'Теперь она не промокнет, если пойдет дождь :)\n'
        'Утка добралась до места, взять ей пиво?'
    )
    user_answer = get_user_answer()
    if user_answer:
        step3_beer()
    else:
        step3_no_beer()


def step2_no_umbrella():
    """Second step for duck without umbrella"""
    print(
        'Утке повезло, дождя не было, она дошла до бара!\n'
        'Она просит пиво, вы ей разрешаете?'
    )
    user_answer = get_user_answer()
    if user_answer:
        step3_beer()
    else:
        step3_no_beer()


def step3_beer():
    """Third step for duck with beer"""
    print('Утка довольна, она любит Немецкое Нефильтрованное ...')


def step3_no_beer():
    """Third step for duck without beer"""
    print(
        'Утка расстроилась :(\n'
        'Она недовольна и ушла домой ...'
    )


if __name__ == '__main__':
    step1()
