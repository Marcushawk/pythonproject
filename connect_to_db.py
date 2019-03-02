import numpy as np # we will use this later, so import it now

from bokeh.io import output_file, show
from bokeh.plotting import figure	
#output_file("blah.png")
# create a new plot with default tools, using figure
p = figure(plot_width=400, plot_height=400)
l = figure(plot_width=400, plot_height=400)

# add a line renderer with x and y coordinatescolor, and alpha
# p.line([1, 2, 3, 4, 5], [1,2, 3, 4, 5]5, line_color="navy", ="red")
# p.line([1, 2, 4, 4, 5], [1,2, 3, 4, 5]5, line_color="navy", ="blue")


# show(p) # show the results

import sqlite3

import matplotlib.pyplot as plt
import numpy as np

conn = sqlite3.connect('database.sqlite')
c = conn.cursor()

average_score = []
pub_year_genres= []

score_rap = []
pub_year_rap = []

score_rock = []
pub_year_rock = []

score_jazz = []
pub_year_jazz = []

score_electronic = []
pub_year_electronic = []

score_experimental = []
pub_year_experimental = []

#for row in c.execute('SELECT * FROM reviews'):
# for row in c.execute('select * from reviews inner join genres on reviews.reviewid = genres.reviewid where genres.genre=\'rap\';'):
#     print(row)
#     score_rap.append(row[4])
#     pub_year_rap.append(row[12])
# for row in c.execute('select * from reviews inner join genres on reviews.reviewid = genres.reviewid where genres.genre=\'rock\';'):
#     print(row)
#     score_rock.append(row[4])
#     pub_year_rock.append(row[12])
# for row in c.execute('select * from reviews inner join genres on reviews.reviewid = genres.reviewid where genres.genre=\'jazz\';'):
#     print(row)
#     score_jazz.append(row[4])
#     pub_year_jazz.append(row[12])
# for row in c.execute('select * from reviews inner join genres on reviews.reviewid = genres.reviewid where genres.genre=\'electronic\';'):
#     print(row)
#     score_electronic.append(row[4])
#     pub_year_electronic.append(row[12])
# for row in c.execute('select * from reviews inner join genres on reviews.reviewid = genres.reviewid where genres.genre=\'experimental\';'):
#     print(row)
#     score_experimental.append(row[4])
#     pub_year_experimental.append(row[12])
for row in c.execute('select avg(score),genre,pub_year from reviews inner join genres on reviews.reviewid = genres.reviewid group by genre,pub_year;'):
    print(row)
    if row[1] == 'rap':
        score_rap.append(row[0])
        pub_year_rap.append(row[2])
    elif row[1] == 'jazz':
        score_jazz.append(row[0])
        pub_year_jazz.append(row[2])
    elif row[1] == 'electronic':
        score_electronic.append(row[0])
        pub_year_electronic.append(row[2])
    elif row[1] == 'experimental':
        score_experimental.append(row[0])
        pub_year_experimental.append(row[2])
    elif row[1] == 'rock':
        score_rock.append(row[0])
        pub_year_rock.append(row[2])


# https://docs.python.org/2/library/sqlite3.html

p.line(pub_year_rap, score_rap, line_color="red")
p.line(pub_year_rock, score_rock, line_color="blue")
p.line(pub_year_jazz, score_jazz, line_color="orange")
p.line(pub_year_electronic, score_electronic, line_color="green")
p.line(pub_year_experimental, score_experimental, line_color="black")
# p.line(pub_year_genres, average_score, line_color="red", ="red")


show(p)

#splitting: https://www.pythonforbeginners.com/dictionary/python-split

"""
JOINING STUFF AND SPLITTING STUFF
>>> x = ['a','n','d','y']
>>> ",".join(x)
'a,n,d,y'
>>> "-".join(x)
'a-n-d-y'
>>> "".join(x)
'andy'
>>> "---------".join(x)
'a---------n---------d---------y'
"""
###