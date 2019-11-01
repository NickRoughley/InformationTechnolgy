import sqlite3
from guizero import App, Text, TextBox, PushButton

app = App(title="Nick's Database", bg="Blue", width=1920, height=1080)

database = 'world.db'  # create variable name for database

conn = sqlite3.connect(database)  # opens/connects to database


# def select_population():
#     print(record)
#
#
# def select_life():
#     print(record1)


Population = PushButton(app, text="Population")#, command=select_population)
LifeExpectancy = PushButton(app, text="LifeExpectancy",)# command=select_life)
Submit3 = PushButton(app, text="Governemnt")
Submit4 = PushButton(app, text="IndepYear")
record = conn.execute('SELECT Name, Population FROM Country WHERE Population < 1000000')
record1 = conn.execute('SELECT Name, LifeExpectancy FROM Country WHERE LifeExpectancy > 60')
record2 = conn.execute(
    'SELECT Name,continent,LifeExpectancy,GovernmentForm FROM Country WHERE GovernmentForm=="Republic"')
record3 = conn.execute('SELECT Name, Population, IndepYear, LifeExpectancy FROM Country WHERE IndepYear > 1900')


for row in record:
    print(row)
for row in record1:
    print(row)
for row in record2:
    print(row)
for row in record3:
    print(row)
conn.close

app.display()

# record = conn.execute('SELECT * FROM Country;')




