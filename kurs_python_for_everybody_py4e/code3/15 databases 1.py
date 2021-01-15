import sqlite3

# this gonna create a file with name in ""
conn = sqlite3.connect("emaildb.sqlite")
cur = conn.cursor()

# it just delete table if exist (but should not exist yet)
cur.execute("DROP TABLE IF EXISTS Counts")

cur.execute("CREATE TABLE Counts (email TEXT, count INTEGER)")

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith("From: "):
        continue
    pieces = line.split()
    email = pieces[1]
    # this ask mark (?) is only placeholder
    # protect from SQL injection attacks
    cur.execute("SELECT count FROM Counts WHERE email = ? ", (email, ))
    row = cur.fetchone()
    if row is None:
        cur.execute("INSERT INTO Counts (email, count) VALUES (?, 1)", (email, ))
    else:
        cur.execute("INSERT INTO Counts SET count = count + 1 WHERE email = ?", (email, ))
    conn.commit()

# https://sqlite.org/lang/select.html
sqlstr = "SELECT email, count FROM Count ORDER BY count DESC LIMIT 10"

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
# "emaildb.py" 34L, 942C written
