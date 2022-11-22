""" Avito Python second homework. Working with CSV """


def read_csv(file_path: str) -> list:
    """ Read csv-file Corp_Summary """
    data = []
    with open(file_path, encoding='utf-8') as file:
        for string in file.readlines()[1:]:
            data_string = string.split(';')
            data_string[-2:] = map(float, data_string[-2:])
            data.append(data_string)
    return data


def get_hierarchy(data: list) -> dict:
    """ Make dictionary of departments """
    departments = {}
    for elem in data:
        if elem[1] in departments:
            if elem[2] in departments[elem[1]]:
                departments[elem[1]][elem[2]].append(elem[0])
            else:
                departments[elem[1]][elem[2]] = [elem[0]]
        else:
            departments[elem[1]] = {}
    return departments


def print_hierarchy(departments: dict):
    """ Print hierarchy of departments """
    print('-----')
    for department, sections in departments.items():
        print(department)
        print('-----')
        for section, names in sections.items():
            print(f'\t-> {section}')
            for name in names:
                print(f'\t\t{name}')
        print('-----')


def get_report_of_departments(data: list) -> dict:
    """ Make report about departments """
    def get_size_of_departments() -> dict:
        """ Counting size of department and make dict of sizes """
        sizes_departments = {}
        for elem in data:
            if elem[1] in sizes_departments:
                sizes_departments[elem[1]] += 1
            else:
                sizes_departments[elem[1]] = 1
        return sizes_departments

    def all_about_salary_of_department() -> dict:
        """
        Make dict of salaries (department -> list of salaries),
        count min-max and average salary
        """
        salaries_departments = {}
        for elem in data:
            if elem[1] in salaries_departments:
                salaries_departments[elem[1]].append(elem[5])
            else:
                salaries_departments[elem[1]] = []
        info_salary_departments = {}
        for department, salaries in salaries_departments.items():
            info_salary_departments[department] = {}
            info_salary_departments[department]['min-max'] = \
                f'{min(salaries)} - {max(salaries)}'
            info_salary_departments[department]['average'] = \
                float(sum(salaries)) / len(salaries)
        return info_salary_departments

    sizes = get_size_of_departments()
    info_about_salary = all_about_salary_of_department()
    report_departments = {}
    for dep, size in sizes.items():
        report_departments[dep] = [dep, str(size),
                                   info_about_salary[dep]['min-max'],
                                   str(info_about_salary[dep]['average'])]
    return report_departments


def print_report_departments(report_departments: dict):
    """ Printing report about departments """
    print('-----')
    for department, info in report_departments.items():
        print(department)
        print('-----')
        print(f'\tSize: {info[1]}\n'
              f'\tMin-max salary: {info[2]}\n'
              f'\tAverage salary: {info[3]}')
        print('-----')


def save_report_as_csv(report_departments: dict):
    """ Save report as csv """
    with open("Report.csv", 'wb') as file:
        file.write('Name;Size;Min-Max;Average\n'.encode('utf-8'))
        for _, item in report_departments.items():
            file.write((';'.join(item) + '\n').encode('utf-8'))


def print_menu():
    """ Just printing main menu """
    print('\n\n')
    print('*' * 20)
    print('Menu')
    print('-' * 20)
    print('\t1. Get the hierarchy of departments\n'
          '\t2. Get the report about departments\n'
          '\t3. Save the report about departments as CSV-file in \"Report.csv\"\n'
          '\t4. Exit')
    print('-' * 20)


def main_launch():
    """ Main function with launching menu """
    data = read_csv('Corp_Summary.csv')
    departments_hierarchy = get_hierarchy(data)
    departments_report = get_report_of_departments(data)
    print_menu()
    while True:
        user_command = input()
        if user_command == '1':
            print_hierarchy(departments_hierarchy)
            print_menu()
        elif user_command == '2':
            print_report_departments(departments_report)
            print_menu()
        elif user_command == '3':
            save_report_as_csv(departments_report)
            print_menu()
        elif user_command == '4':
            return
        else:
            print('Please, write the number of the command')


if __name__ == '__main__':
    main_launch()
