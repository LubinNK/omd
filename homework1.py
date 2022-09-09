def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    
    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()

def step2_umbrella():
    print(
        'Утка приняла зонтик! \n' 
        'Теперь она не промокнет, если пойдет дождь :)'
    )

def step2_no_umbrella():
    print('Осторожно, утка может промокнуть!')

if __name__ == '__main__':
    step1()