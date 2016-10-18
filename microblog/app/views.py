from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Pombo'}
	posts = [
				{
					'author': {'nickname': 'Pombo1'}, 
            		'body': 'Beautiful day in Pomboland!'
				},
				{
					'author': {'nickname': 'Pombo2'}, 
            		'body': 'The Avengers movie was so cool!'

				}
			]
	return render_template('index.html',
							title='Voando',
							user=user,
							posts=posts)