def get_grade(score):
    if 0 <= score <= 49:
        return "незадовільно"
    elif 50 <= score <= 69:
        return "задовільно"
    elif 70 <= score <= 89:
        return "добре"
    elif 90 <= score <= 100:
        return "відмінно"
    else:
        return "Некоректне значення балів"

try:
    score = int(input("Введіть кількість отриманих балів: "))
    print(f"Ваша оцінка: {get_grade(score)}")
except ValueError:
    print("Будь ласка, введіть ціле число.")