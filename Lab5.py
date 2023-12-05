import csv
import os

db_file_path = "база_даних_книг.csv"

if not os.path.isfile(db_file_path):
    with open(db_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Назва", "Автор", "Рік видання", "Жанр"])

def add_book(title, author, year, genre):
    with open(db_file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([title, author, year, genre])

def read_database():
    with open(db_file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def search_by_year(year):
    with open(db_file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[2] == year:
                print(row)

def update_record(title_to_update, new_genre):
    rows = []
    with open(db_file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == title_to_update:
                row[3] = new_genre
            rows.append(row)

    with open(db_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

def delete_record(title_to_delete):
    rows = []
    with open(db_file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] != title_to_delete:
                rows.append(row)

    with open(db_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

def sort_database_by_year():
    
    with open(db_file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        headers = next(reader)
        sorted_rows = sorted(reader, key=lambda x: int(x[2]))

    with open(db_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(sorted_rows)

add_book("Книга 1", "Автор 1", "2000", "Жанр 1")
add_book("Книга 2", "Автор 2", "1995", "Жанр 2")
add_book("Книга 3", "Автор 3", "2010", "Жанр 3")
add_book("Книга 4", "Автор 4", "1980", "Жанр 1")
add_book("Книга 5", "Автор 5", "2022", "Жанр 2")

print("База даних після додавання:")
read_database()

print("\nПошук за роком видання 2000:")
search_by_year("2000")

update_record("Книга 1", "Новий жанр")

print("\nБаза даних після оновлення:")
read_database()

delete_record("Книга 2")

print("\nБаза даних після видалення:")
read_database()

sort_database_by_year()

print("\nБаза даних після сортування за роком видання:")
read_database()
