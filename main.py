import locale
from typing import Dict

employees: Dict[str, str] = {
    "Кузін":       "м. Суми, вул. Заливна, 5",
    "Куравльов":   "м. Суми, вул. Збройних Сил України, 63",
    "Іващенко":    "м. Суми, вул. Харківська, 10",
    "Пасішніченко":    "м. Суми, вул. Героїв Сумщини, 7",
    "Шевченко":    "м. Суми, вул. В'ячеслава Чорновола, 51",
    "Кудін":       "м. Суми, вул. Івана Сірка, 9",
    "Статівка":   "м. Суми, вул. Михайла Лушпи, 3",
    "Кубиків":      "м. Суми, вул. Козацький Вал, 1",
    "Кульков":     "м. Суми, вул. Білопільський шлях, 11",
    "Лозовська":     "м. Суми, вул. Петропавлівська, 16",
}

def print_all(book: Dict[str, str]) -> None: #Виведення всіх значень словника.
    if not book:
        print("Словник порожній.")
        return
    for surname, address in book.items():
        print(f"{surname:15} -> {address}")

def add_record(book: Dict[str, str]) -> None: #Додавання нового запису з обробкою помилок.
    try:
        surname = input("Введіть прізвище: ").strip()
        if not surname:
            raise ValueError("Порожнє прізвище.")
        if surname in book:
            print("Такий запис уже існує. Спробуйте інше прізвище.")
            return
        address = input("Введіть адресу: ").strip()
        if not address:
            raise ValueError("Порожня адреса.")
        book[surname] = address
        print(f"Додано: {surname} -> {address}")
    except ValueError as e:
        print("Помилка введення:", e)

def delete_record(book: Dict[str, str]) -> None: #Видалення запису зі словника.
    key = input("Введіть прізвище для видалення: ").strip()
    try:
        del book[key]
        print(f"Видалено запис: {key}")
    except KeyError:
        print("Помилка: запису з таким прізвищем не існує.")

def print_sorted(book: Dict[str, str]) -> None: #Перегляд словника за відсортованим ключем (за алфавітом).
    if not book:
        print("Словник порожній.")
        return

    try:
        locale.setlocale(locale.LC_ALL, 'uk_UA.UTF-8')
    except locale.Error:
        locale.setlocale(locale.LC_ALL, '')

    print("Відсортований за алфавітом список:")
    for surname in sorted(book.keys(), key=locale.strxfrm):
        print(f"{surname:15} -> {book[surname]}")

def solve_variant_task(book: Dict[str, str]) -> None:  #Перевірка, чи працюють у фірмі люди з прізвищами Кузін, Куравльов, Кудін, Кульков або Кубиків.
    targets = ["Кузін", "Куравльов", "Кудін", "Кульков", "Кубиків"]
    print("Перевірка наявності працівників Кузін, Куравльов, Кудін, Кульков або Кубиків")
    found_any = False

    lowered = {k.casefold(): k for k in book.keys()}
    for t in targets:
        if t.casefold() in lowered:
            real_key = lowered[t.casefold()]
            print(f"Знайдено: {real_key:15} -> {book[real_key]}")
            found_any = True

    if not found_any:
        print("Жодного з перелічених прізвищ у словнику не знайдено.")

def menu() -> None:
    actions = {
        "1": ("Вивести всі записи словника", print_all),
        "2": ("Додати новий запис", add_record),
        "3": ("Видалити запис", delete_record),
        "4": ("Переглянути за відсортованим ключем (за алфавітом)", print_sorted),
        "5": ("Пошук конкретних прізвищ", solve_variant_task),
        "0": ("Вийти з програми", None),
    }

    while True:
        print("\n===================== МЕНЮ =====================")
        for k, (title, _) in actions.items():
            print(f"{k}. {title}")
        choice = input("Оберіть пункт меню: ").strip()

        if choice == "0":
            print("До побачення!")
            break

        action = actions.get(choice)
        if not action:
            print("Невірний вибір. Спробуйте ще раз.")
            continue

        try:
            action[1](employees)
        except Exception as e:
            print("Помилка під час виконання:", e)

if __name__ == "__main__":
    menu()