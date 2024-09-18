from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {'author' : 'Cosmas',
        'title' : 'First Blog',
        'content' : 'Paragraph of contents',
        'post_date' : 'Sept 7, 2024'
        },
        {
        'author' : 'Albert',
        'title' : 'Second Blog',
        'content' : 'Paragraph of contents',
        'post_date' : 'Sept 9, 2024'  
        },
        {
            'author' : 'Willy',
        'title' : 'Third Blog',
        'content' : 'Paragraph of contents',
        'post_date' : 'Sept 12, 2024' 
        }
        ] 
      


@app.route('/')
def home():
    return render_template ('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', )

@app.route('/contacts')
def contacts():
    return render_template ('contact.html', ) 

@app.route('/register')
def register():
    return render_template ('register.html',) 

@app.route('/login')
def login():
    return render_template('login.html', )

if __name__=='__main__':
    app.run(debug=True)