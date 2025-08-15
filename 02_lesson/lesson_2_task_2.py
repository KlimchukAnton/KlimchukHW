def is_year_leap(year):
    return "Tru" if year % 4 == 0 else "False"

input_year = int(input("Введите год: "))
result = is_year_leap(input_year)
print(f"Год: {input_year} - {result}")
