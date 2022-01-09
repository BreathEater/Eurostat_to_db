import sqlite3

conn = sqlite3.connect('eurostat.db')

c = conn.cursor()

# c.execute('''CREATE TABLE units(unit_short TEXT, unit_long TEXT)''')

# insert DataFrame into units in db
# c.execute('''INSERT INTO units VALUES()''')

# commit execution into the db
# conn.commit()