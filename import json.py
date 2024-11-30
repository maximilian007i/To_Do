import json
import os


DATA_FILE = 'tasks.json'

def load_tasks():
    """Загрузить задачи из файла"""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_tasks(tasks):
    """Сохранить задачи в файл"""
    with open(DATA_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def add_task(tasks):
    """Добавить новую задачу"""
    task = {
        'id': len(tasks) + 1,
        'title': input('Введите название задачи: '),
        'description': input('Введите описание задачи: '),
        'category': input('Введите категорию задачи: '),
        'deadline': input('Введите срок выполнения задачи: '),
        'priority': input('Введите приоритет задачи (низкий, средний, высокий): '),
        'done': False
    }
    tasks.append(task)
    save_tasks(tasks)
    print('Задача добавлена!')

def view_tasks(tasks):
    """Просмотреть все задачи"""
    for task in tasks:
        print(f"ID: {task['id']}")
        print(f"Название: {task['title']}")
        print(f"Описание: {task['description']}")
        print(f"Категория: {task['category']}")
        print(f"Срок выполнения: {task['deadline']}")
        print(f"Приоритет: {task['priority']}")
        print(f"Выполнено: {'Да' if task['done'] else 'Нет'}")
        print('---')

def view_tasks_by_category(tasks):
    """Просмотреть задачи по категориям"""
    category = input('Введите категорию: ')
    for task in tasks:
        if task['category'] == category:
            print(f"ID: {task['id']}")
            print(f"Название: {task['title']}")
            print(f"Описание: {task['description']}")
            print(f"Категория: {task['category']}")
            print(f"Срок выполнения: {task['deadline']}")
            print(f"Приоритет: {task['priority']}")
            print(f"Выполнено: {'Да' if task['done'] else 'Нет'}")
            print('')

def edit_task(tasks):
    """Редактировать задачу"""
    task_id = int(input('Введите ID задачи: '))
    for task in tasks:
        if task['id'] == task_id:
            task['title'] = input('Введите новое название задачи: ')
            task['description'] = input('Введите новое описание задачи: ')
            task['category'] = input('Введите новую категорию задачи: ')
            task['deadline'] = input('Введите новый срок выполнения задачи: ')
            task['priority'] = input('Введите новый приоритет задачи (низкий, средний, высокий): ')
            save_tasks(tasks)
            print('Задача отредактирована')
            return
    print('Задача не найдена')

def delete_task(tasks):
    """Удалить задачу"""
    task_id = int(input('Введите ID задачи: '))
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print('Задача удалена')
            return
    print('Задача не найдена')

def search_tasks(tasks):
    """Поиск задач"""
    query = input('Введите ключевое слово: ')
    for task in tasks:
        if query in task['title'] or query in task['description'] or query in task['category']:
            print(f"ID: {task['id']}")
            print(f"Название: {task['title']}")
            print(f"Описание: {task['description']}")
            print(f"Категория: {task['category']}")
            print(f"Срок выполнения: {task['deadline']}")
            print(f"Приоритет: {task['priority']}")
            print(f"Выполнено: {'Да' if task['done'] else 'Нет'}")
            print('')

def main():
    tasks = load_tasks()
    while True:
        print("1. Просмотреть все задачи")
        print("2. Добавить новую задачу")
        print("3. Просмотреть задачи по категории")
        print("4. Редактировать задачу")
        print("5. Удалить задачу")
        print("6. Поиск задач")
        print("7. Выход")
        choice = input("Введите номер действия: ")
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            view_tasks_by_category(tasks)
        elif choice == "4":
            edit_task(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            search_tasks(tasks)
        elif choice == "7":
            break
        else:
            print("Неправильный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()