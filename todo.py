tasks, number = [], 1


def add_tasks():
    global number
    global tasks
    n = input('Введите задачу: ')
    while n != 'stop':
        tasks.append(f'{number} [ ] ' + n)
        n = input('Введите задачу: ')
        number += 1


def clear_tasks():
    global tasks
    global number
    tasks, number = [], 1


def interface():
    global tasks
    print('-' * 20, 'ЧТО СДЕЛАТЬ ДАЛЬШЕ?',
          '1. Посмотреть задачи\n2. Выполнить задачи\n3. Добавить задачи\n4. Очистить список\n5. Закрыть приложение',
          sep='\n')
    action = int(input())
    if action == 1:
        print('=' * 20, *tasks, sep='\n')
        interface()
    elif action == 2:
        print('#' * 20, 'Какие задачи выполнить?', sep='\n')
        cross = list(map(int, input().split()))
        for i in cross:
            if 0 <= i-1 < len(tasks):
                tasks[i - 1] = tasks[i - 1].replace('[ ]', '[#]')
            else:
                print(f'задачи {i} нет в списке')
        interface()
    elif action == 3:
        print('+' * 20)
        add_tasks()
        interface()
    elif action == 4:
        clear_tasks()
    elif action == 5:
        return
    else:
        print('!' * 20, 'Некорректная команда', sep='\n')


if __name__ == "__main__":
    print('Здравствуйте!')
    add_tasks()
    interface()
    print('До свидания!')
