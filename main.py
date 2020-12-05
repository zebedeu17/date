# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sqlite3

from elev import Elev
from profesor import Profesor
from admin import Admin

conn1 = sqlite3.connect('elev.db')
conn2 = sqlite3.connect('profesor.db')
conn3 = sqlite3.connect('admin.db')

c1 = conn1.cursor()
c2 = conn2.cursor()
c3 = conn3.cursor()

#c1.execute("""CREATE TABLE elev (
#            first text,
#            last text,
#            clasa text,
#            nota_mate text,
#            nota_info text,
#            nota_romana text,
#            nota_fizica text,
#            absenta_mate text,
#            absenta_info text,
#            absenta_romana text,
#            absenta_fizica text
#    )""")

#c2.execute("""CREATE TABLE profesor (
#            first text,
#            last text,
#             materie text
#    )""")

#c3.execute("""CREATE TABLE admin (
#            first text,
#            last text
#    )""")

c3.execute("INSERT INTO admin VALUES ('Lion', 'Moroz')")

elev1 = Elev('Alin', 'Roib', 'IXB', '0', '0', '0', '0', '0', '0', '0', '0')

c3.execute("SELECT * FROM admin WHERE last='Moroz'")

#c1.execute("SELECT * FROM elev WHERE last='Roib'")

print(elev1.first)

print(c3.fetchone())

# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
