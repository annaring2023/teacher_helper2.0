# імпортуємо все

from fpdf import FPDF
import random
import colorama
from colorama import Fore, Back
colorama.init(autoreset=True)
# головна функція


def operations():
    while True:
        try:
            operation = int(input(
                f"{Fore.WHITE}{Back.WHITE}\n1 - розподілити на команди\n2 - похвала для учня\n3 - хто йде до дошки?\n4 - створити нотатку для учня\n5 - створеня тесту\n6 - математичні операції\n7 - вийти\nВаш вибір: "))
        except ValueError:
            print(f"{Fore.RED}Введіть число: ")
            continue

        if operation == 1:
            create_teams()
        elif operation == 2:
            create_congrats()
        elif operation == 3:
            single_students()
        elif operation == 4:
            new_note()
        elif operation == 5:
            random_questions()
        elif operation == 6:
            math()
        elif operation == 7:
            print("Завершення роботи...")
            break
        else:
            print(f"{Fore.RED}🆘 Недопустимий тип даних!")

# дістає одного студента


def single_students() -> None:
    stud_list = get_students()
    if not stud_list:
        print(f"{Fore.RED}🆘 Список учнів порожній, спочатку введіть список!")
        return
    single_student = random.choice(stud_list)
    print(f"{Fore.GREEN}{single_student}")

# конвертує файл похвали


def get_congrats() -> list:
    with open("congrats.txt", "r", encoding="utf-8") as f:
        return [line.strip() for line in f]

# виводить одну похвалу


def create_congrats() -> None:
    cong_list = get_congrats()
    if not cong_list:
        print(f"{Fore.RED}🆘 Список похвали порожній, спочатку введіть список!")
        return
    congratul_message = random.choice(cong_list)
    print(f"{Fore.GREEN}{congratul_message}")

# конвертує файл студентів


def get_students() -> list:
    with open("children.txt", "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

# розподіляє команди зі списку


def create_teams():
    stud_list = get_students()

    if not stud_list:
        print(f"{Fore.RED}🆘 Список учнів порожній, спочатку введіть список😡")
        return

    random.shuffle(stud_list)
    quantity_of_students = len(stud_list)
    try:
        team_quantity = int(input("Введіть кількість бажаних команд: "))
    except ValueError:
        print(f"{Fore.RED}Недопустимий тип даних!")
        return

    if team_quantity <= 0 or team_quantity > quantity_of_students:
        print(f"{Fore.RED}Недопустима кількість команд")

    teams = [[] for _ in range(team_quantity)]

    for i, student in enumerate(stud_list):
        teams[i % team_quantity].append(student)

    for i, team in enumerate(teams, 1):
        print(f"{Fore.GREEN}\nКоманда {i}:")
        for student in team:
            print(f"{Fore.GREEN} - {student}")

# створення похвали


def new_note() -> dict:
    notes = {}
    stud_list = get_students()
    print(f"{Fore.GREEN}\nУчні:")
    for i, student in enumerate(stud_list):
        print(f"{Fore.GREEN}{i + 1}. {student}")
    try:
        choice = int(input("Якому номеру учня ви хочете зробити замітку?"))
    except ValueError:
        print(f"{Fore.RED}🆘 Недопустимий тип даних!")
        return

    if choice > len(stud_list) or choice <= 0:
        print(f"{Fore.RED}🆘 Недопустиме число!")
        return
    student = stud_list[choice - 1]
    note = input(f"Введіть примітку для {student}: ")
    notes[student] = note
    save_notes(notes)
    print(f"{Fore.GREEN}✅ Примітку збережено!")
    return notes

# створення похвали в файлі


def save_notes(notes):
    with open("admire.txt", "a", encoding="utf-8") as f:
        for name, note in notes.items():
            f.write(f"{name}: {note}\n")


# запуск головної функції


with open("easy.txt", "r", encoding="utf-8") as file_easy:
    easy_questions = [q.strip()
                      for q in file_easy.read().split('\n\n') if q.strip()]

with open("medium.txt", "r", encoding="utf-8") as file_med:
    medium_questions = [q.strip()
                        for q in file_med.read().split('\n\n') if q.strip()]

with open("hard.txt", "r", encoding="utf-8") as file_hard:
    hard_questions = [q.strip()
                      for q in file_hard.read().split('\n\n') if q.strip()]

# генерація питань


def random_questions():
    try:
        easy_num = int(input("Введіть к-ть запитань легкого рівня: "))
        medium_num = int(input("Введіть к-ть запитань середнього рівня: "))
        hard_num = int(input("Введіть к-ть запитань складного рівня: "))
    except ValueError:
        print(f"{Fore.RED}🆘 Недопустимий тип даних!")
        return

    if easy_num <= len(easy_questions):
        easy_q = random.sample(easy_questions, easy_num)
    else:
        print(f"{Fore.RED}🆘Кількість більша ніж запитань")

    if medium_num <= len(medium_questions):
        medium_q = random.sample(medium_questions, medium_num)
    else:
        print(f"{Fore.RED}🆘Кількість більша ніж запитань")

    if hard_num <= len(hard_questions):
        hard_q = random.sample(hard_questions, hard_num)
    else:
        print(f"{Fore.RED}🆘Кількість більша ніж запитань")

    with open("test.txt", "w", encoding="utf-8") as f:
        f.write("Легка легкість:\n")
        for question in easy_q:
            f.write(f"{question}\n")
        f.write("\nСередня середність:\n")
        for question in medium_q:
            f.write(f"{question}\n")
        f.write("\nВажка важкість:\n")
        for question in hard_q:
            f.write(f"{question}\n")
        print(f"{Fore.GREEN}✅ Ваш файл готовий")
# генерація педофайлу


def generate_pdf(input_file, output_file):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=20)
    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            pdf.cell(200, 10, txt=line.strip(), ln=1, align='L')
    pdf.output(output_file)
    print(f"{Fore.GREEN}\n✅ Ваш файл готовий: {output_file}")

# вся логіка математичної функції


def math():
    while True:
        try:
            decision_of_operation = int(input(
                f"{Fore.WHITE}{Back.WHITE}\nВведіть яку дію ви хочете тренувати:\n1 - додавання\n2 - віднімання\n3 - множення\n4 - ділення\n5 - вийти\nВаш вибір: "))
            if decision_of_operation == 5:
                print("Повертаємось на головну...")
                break
            quantity_of_operation = int(
                input(f"{Fore.WHITE}{Back.WHITE}Скільки прикладів хочете вивести у файл? "))

        except ValueError:
            print(f"{Fore.RED}Введіть число: ")
            continue

        if decision_of_operation == 1:
            adding_function(quantity_of_operation)
        elif decision_of_operation == 2:
            substraction_function(quantity_of_operation)
        elif decision_of_operation == 3:
            multiply_function(quantity_of_operation)
        elif decision_of_operation == 4:
            division_function(quantity_of_operation)
        else:
            print(f"{Fore.RED}🆘 Недопустимий тип даних!")
            return

# віднімання


def substraction_function(quantity_of_operation):
    i = 1
    with open("math_sub.txt", "w", encoding='utf8') as file:
        while i <= quantity_of_operation:
            number1 = random.randint(1, 100)
            number2 = random.randint(1, 100)
            correct = number1 - number2
            if correct < 0:
                continue
            i += 1
            correct = (f"{number1} - {number2} = \n")
            file.write(correct)
    generate_pdf("math_sub.txt", "math_sub.pdf")

# ділення


def division_function(quantity_of_operation):
    i = 1
    with open("math_div.txt", "w", encoding='utf8') as file:
        while i <= quantity_of_operation:
            number1 = random.randint(1, 100)
            number2 = random.randint(1, 100)
            if number1 % number2 != 0:
                continue
            i += 1
            correct = f"{number1} / {number2} = \n"
            file.write(correct)
    generate_pdf("math_div.txt", "math_div.pdf")

# множення


def multiply_function(quantity_of_operation):
    i = 1
    with open("math_mul.txt", "w", encoding='utf8') as file:
        while i <= quantity_of_operation:
            number1 = random.randint(1, 100)
            number2 = random.randint(1, 100)
            correct = f"{number1} * {number2} = \n"
            i += 1
            file.write(correct)

    generate_pdf("math_mul.txt", "math_mul.pdf")

# додавання


def adding_function(quantity_of_operation):
    i = 1
    with open("math_add.txt", "w", encoding='utf8') as file:
        while i <= quantity_of_operation:
            number1 = random.randint(1, 100)
            number2 = random.randint(1, 100)
            correct = f"{number1} + {number2} = \n"
            i += 1
            file.write(correct)
    generate_pdf("math_add.txt", "math_add.pdf")


# кінець
if __name__ == "__main__":
    operations()
