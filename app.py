from flask import Flask, render_template, flash, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired, ValidationError
from flask_mail import Mail, Message
from datetime import datetime
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Avestruz.123@localhost/player6_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()
migrate = Migrate(app, db)
app.config['SECRET_KEY'] = 'outerwilds'
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'luccalucheti@gmail.com'
app.config['MAIL_PASSWORD'] = 'zilu dbjc rcfa rzve'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

class register(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team = db.Column(db.String(64), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    player1 = db.Column(db.String(64), nullable=False, unique=True)
    player2 = db.Column(db.String(64), nullable=False, unique=True)
    player3 = db.Column(db.String(64), nullable=False, unique=True)
    player4 = db.Column(db.String(64), nullable=False, unique=True)
    player5 = db.Column(db.String(64), nullable=False, unique=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Team %r>' % self.team

class RegisterForm(FlaskForm):
    team = StringField('nome da equipe', validators=[DataRequired()])
    email = EmailField('e-mail', validators=[DataRequired()])
    player1 = StringField('player 1 (capitão)', validators=[DataRequired()])
    player2 = StringField('player 2', validators=[DataRequired()])
    player3 = StringField('player 3', validators=[DataRequired()])
    player4 = StringField('player 4', validators=[DataRequired()])
    player5 = StringField('player 5', validators=[DataRequired()])
    submit = SubmitField('Inscreva-se')

    def validate_email(self, field):
        if register.query.filter_by(email=field.data).first():
            raise ValidationError('Esse e-mail já está em uso.')

@app.route('/', methods=['GET','POST'])
def index():
    form = RegisterForm()
    if form.validate_on_submit():
        try:
            registration = register(team=form.team.data, email=form.email.data, player1=form.player1.data, player2=form.player2.data, player3=form.player3.data, player4=form.player4.data, player5=form.player5.data)
            db.session.add(registration)
            db.session.commit()
            msg = Message('Seu time está inscrito!', 
                        sender='noreply@gmail.com', 
                        recipients=[form.email.data])
            msg.body = 'Obrigado por se inscrever no campeonato conosco, entre em nosso discord: https://discord.gg/MgQhzEDY'
            mail.send(msg)
            form.team.data=''
            form.email.data=''
            form.player1.data=''
            form.player2.data=''
            form.player3.data=''
            form.player4.data=''
            form.player5.data=''
            flash('Seu time foi inscrito com sucesso!')
            return render_template('index.html', form=form)
        except:
            flash('Algum dos seus dados ja foi cadastrado.')
            return render_template('index.html', form=form)
    return render_template('index.html', form=form)

@app.route('/registered')
def registered():
    return render_template('registered.html')

if __name__ == '__main__':
    app.run(debug=True)