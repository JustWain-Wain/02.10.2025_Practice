def check_winners(list_of_competitors, score=0):
    unique_scores = list(set(list_of_competitors))
    unique_scores.sort(reverse=True)
    return "Вы в тройке победителей!" if score in unique_scores[:3] else "Вы не попали в тройку победителей."

student_score = int(input("Введите количество баллов: "))
competitors = input("Введите список баллов (оставьте пустым для использования данного в задаче значения): \n").split()
if not competitors:
    competitors = [20, 48, 52, 38, 36, 13, 7, 41, 34, 24, 5, 51, 9, 14, 28]
    print(competitors)
print(check_winners(competitors, student_score))