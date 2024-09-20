from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm,LoginForm
app = Flask(__name__)

app.config['SECRET_KEY']  = 'd4ab9a97f62ce0cabb424ff26d23d6ec'

posts = [
    {'author' : 'Cosmas',
        'title' : 'First Blog',
        'content' : 'When using Lorem Ipsum for creating dummy content for your newly created website, you can select the text formats you want from the tool. Like, words, sentences, or paragraphs.Then, you can select whether you want HTML markup in your dummy content or not Then, you can choose the number of words and paragraphs for your dummy content and execute the plan accordingly. You can use this tool at incrementors.com for free.',
        'post_date' : 'Sept 7, 2024'
        },
        {
        'author' : 'Albert',
        'title' : 'Second Blog',
        'content' : 'You can click on the ‘item to generate’ column and select the format you want content in.Below that, you can select if you want an HTML tag in your content or notAfter that, you can choose how many paragraphs you want in the ‘how many items to generate’ column.Then, you can choose the minimum and maximum words you want per sentence.',
        'post_date' : 'Sept 9, 2024'  
        },
        {
            'author' : 'Willy',
        'title' : 'Third Blog',
        'content' : 'The word Lorem Ipsum is derived from the Latin word which means “pain itself”. It is a kind of a text filler tool that is used by the webmaster on the website.Basically, this tool is used to create dummy content on the website when it’s new.',
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

@app.route('/register', methods=['GET', 'POST',])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'You have created an accout dear {form.username.data}', 'success')
        return redirect(url_for(home))
    return render_template('register.html', title = 'Register', form=form)
    


@app.route('/LoginForm')
def login():
    form = LoginForm()
    return render_template(login.html, title = 'Login', form=form)


if __name__=='__main__':
    app.run(debug=True)