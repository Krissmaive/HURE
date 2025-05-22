# 4. Система управління задачами
tasks = {
    "Почати проект": "очікує",
    "Написати код": "в процесі",
    "Здати звіт": "виконано",
    "Провести тестування": "в процесі",
    "Оновити документацію": "виконано",
    "Очікування відгуку": "очікує"
}

def add_task(name, status):
    tasks[name] = status

def remove_task(name):
    if name in tasks:
        del tasks[name]

def change_status(name, status):
    if name in tasks:
        tasks[name] = status

def filter_tasks_by_status(status):
    return [task for task, stat in tasks.items() if stat == status]

def demo_tasks():
    add_task("Оформити README", "очікує")
    print("Всі задачі:")
    for name, status in tasks.items():
        print(f"- {name}: {status}")
    print("\nОчікуючі задачі:", filter_tasks_by_status("очікує"))
    print("В процесі:", filter_tasks_by_status("в процесі"))
    print("Виконані:", filter_tasks_by_status("виконано"))

if __name__ == "__main__":
    demo_tasks()