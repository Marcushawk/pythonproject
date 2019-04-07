from flask import render_template, request
import numpy as np # we will use this later, so import it now
import sqlite3
import matplotlib.pyplot as plt
import numpy as np
from bokeh.layouts import row
from bokeh.io import output_file, show
from bokeh.plotting import figure	
from app import app
from bokeh.embed import components
def setup():
	#output_file("blah.png")
	# create a new plot with default tools, using figure
	p1 = figure(plot_width=400, plot_height=400, title="Average Ratings vs Publication Year")
	p2 = figure(plot_width=400, plot_height=400, title="Some Random Crap")
	# add a line renderer with x and y coordinatescolor, and alpha
	# p.line([1, 2, 3, 4, 5], [1,2, 3, 4, 5]5, line_color="navy", ="red")
	# p.line([1, 2, 4, 4, 5], [1,2, 3, 4, 5]5, line_color="navy", ="blue")


	# show(p) # show the results

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

	#for dbrow in c.execute('SELECT * FROM reviews'):
	# for dbrow in c.execute('select * from reviews inner join genres on reviews.reviewid = genres.reviewid where genres.genre=\'rap\';'):
	#     print(dbrow)
	#     score_rap.append(dbrow[4])
	#     pub_year_rap.append(dbrow[12])
	# for dbrow in c.execute('select * from reviews inner join genres on reviews.reviewid = genres.reviewid where genres.genre=\'rock\';'):
	#     print(dbrow)
	#     score_rock.append(dbrow[4])
	#     pub_year_rock.append(dbrow[12])
	# for dbrow in c.execute('select * from reviews inner join genres on reviews.reviewid = genres.reviewid where genres.genre=\'jazz\';'):
	#     print(dbrow)
	#     score_jazz.append(dbrow[4])
	#     pub_year_jazz.append(dbrow[12])
	# for dbrow in c.execute('select * from reviews inner join genres on reviews.reviewid = genres.reviewid where genres.genre=\'electronic\';'):
	#     print(dbrow)
	#     score_electronic.append(dbrow[4])
	#     pub_year_electronic.append(dbrow[12])
	# for dbrow in c.execute('select * from reviews inner join genres on reviews.reviewid = genres.reviewid where genres.genre=\'experimental\';'):
	#     print(dbrow)
	#     score_experimental.append(dbrow[4])
	#     pub_year_experimental.append(dbrow[12])
	for dbrow in c.execute('select avg(score),genre,pub_year from reviews inner join genres on reviews.reviewid = genres.reviewid group by genre,pub_year;'):
	    print(dbrow)
	    if dbrow[1] == 'rap':
	        score_rap.append(dbrow[0])
	        pub_year_rap.append(dbrow[2])
	    elif dbrow[1] == 'jazz':
	        score_jazz.append(dbrow[0])
	        pub_year_jazz.append(dbrow[2])
	    elif dbrow[1] == 'electronic':
	        score_electronic.append(dbrow[0])
	        pub_year_electronic.append(dbrow[2])
	    elif dbrow[1] == 'experimental':
	        score_experimental.append(dbrow[0])
	        pub_year_experimental.append(dbrow[2])
	    elif dbrow[1] == 'rock':
	        score_rock.append(dbrow[0])
	        pub_year_rock.append(dbrow[2])


	# https://docs.python.org/2/library/sqlite3.html
	z = 3
	a = 4
	p1.line(pub_year_rap, score_rap, line_color="red")
	p1.line(pub_year_rock, score_rock, line_color="blue")
	p1.line(pub_year_jazz, score_jazz, line_color="orange")
	p1.line(pub_year_electronic, score_electronic, line_color="green")
	p1.line(pub_year_experimental, score_experimental, line_color="black")

	p2.vbar(x=[1, 2, 3], width=0.5, bottom=0,
	       top=[1.2, 2.5, 3.7], color="firebrick")

	# p.line(pub_year_genres, average_score, line_color="red", ="red")

	array_thingy = [p1,p2]
	return array_thingy

@app.route('/')
def index():
    z = setup()
    script, div = components(z[0])
    variable = request.args.get('template_name')
    return render_template("html_temp.html", script = script, div = div)
    return variable
def about():
    return render_template("html_temp.html")
    