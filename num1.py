from random import randint


number: list[int] = [randint(1, 100) for _ in range(50)]
print(number)
#Question A1
print(list(filter(lambda x: x > 50, number)))
#Question A2
print(list(filter(lambda x: x % 7 == 0, number)))
#Question A3
print(list(filter(lambda x: 9 < x < 99, number)))
#Question A4
print(list(filter(lambda x: 9 < x < 100 and (x // 10) == (x % 10), number)))
#Question A5
print(list(filter(lambda x: (x // 10) + (x % 10) == 9, number)))
#Question A6
average = sum(number) / len(number)
print(list(filter(lambda x: x > average, number)))
#Question A7
max_value = max(number)
print(list(filter(lambda x: x > (max_value / 2), number)))

games: list[str] = ["Grand Theft Auto V", "Fortnite", "The Elder Scrolls V: Skyrim", "Dark Souls", "Overwatch"]

#Question B1
print(list(filter(lambda game: len(game) > 8, games)))
#Question B2
print(list(filter(lambda game: game[0] == 'F', games)))
#Question B3
print(list(filter(lambda game: game.count(' ') == 1, games)))
#Question B4
print(list(filter(lambda game: 'v' in game or 'V' in game, games)))

numbers = [randint(-50, 50) for _ in range(20)]
print("Original list:", numbers)

#Question C1
print(list(map(lambda num: num ** 3, numbers )))
#Question C2
print(list(map(lambda num: num % 10, numbers )))
#Question C3
print(list(map(lambda num: num * 9 / 5 + 32, numbers )))
#Question C4
print(list(map(lambda num: "positive" if num > 0 else "negative", numbers )))

fruits = ["Mango", "Orange", "Banana", "Apple", "Strawberry", "Pineapple", "Grapes", "Watermelon"]

#Question D1
print(list(map(lambda fruit: fruit[::-1], fruits )))
#Question D2
print(list(map(lambda fruit: fruit[0], fruits )))
#Question D3
print(list(map(lambda fruit: fruit.upper() , fruits )))
#Question D4
print(list(map(lambda fruit: fruit[len(fruit) // 2] , fruits )))
#Question D5
print(list(map(lambda fruit: fruit + '!' if fruit[-1] == 's' else fruit, fruits )))

# המשמעות של משתנה גלובי הוא שהמשתנה זמין רק בתוך הפונקציה ,
#  כלומר במילים אחרות אם נגדיר משתנה גלובלי בפונקציה הוא יהיה זמין רק בפונקציה

# החיסרון במשתנה גלובלי הוא קושי במעקב, קוד לא קריא אם יש הרבה משתנים גלובלים ותקלות לא צפויות עקב זה
# ובעתיד זה יכול לדרוש שינויים עתידיים בעיצוב התוכנית


x: int = 1
def foo():
   print(x)
   x = 4
foo()


# הטעות בפונקציה הזאת שהפונקציה קודם מדפיסה x ואז אחרכ משנה את ה- x ל-4 במילים אחרות הx - 4 הוא משתנה גלובלי משתנה ששייך רק לפונקציה אך הפייטון לא מבדיל בין האיקסים בין גלובלי למקומי
#  ולכן צריך להוסיף גלובלי בשביל שהקוד יהיה נכון