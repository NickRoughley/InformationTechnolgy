import sqlite3, pyttsx3

database = 'world.db'

# tts = pyttsx3.init()
conn = sqlite3.connect(database)

# record = conn.execute('SELECT Name, HeadofState FROM Country WHERE GovernmentForm = "Republic" Order BY Name;')
# record = conn.execute('SELECT Name, GNP, Population FROM Country WHERE GNP > 10000 ORDER BY GNP')
# record = conn.execute('SELECT Name, Population, SurfaceArea FROM Country WHERE population > 1000000000 ORDER BY Population')
# record = conn.execute('SELECT Name, Population, SurfaceArea FROM Country WHERE SurfaceArea < 10000000 AND Population > '
#                       '1000000000')
for row in record:
    print(row)
    # tts.say(row)
    # tts.runAndWait()