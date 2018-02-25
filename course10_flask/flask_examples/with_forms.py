import datetime
from flask import Flask, request

# pip install flask-WTF
from flask_wtf import FlaskForm
from wtforms import StringField, validators, DateField


class ContactForm(FlaskForm):
    name = StringField(label='Name', validators=[
        validators.Length(min=4, max=25)
    ])
    email = StringField(label='E-mail', validators=[
        validators.Length(min=6, max=35), validators.Email()
    ])

    # class work: сделать валидатор для job:
    # 1. job должны быть только такие: IT, Bank, HR
    # 2. job поле должно быть обязательнным
    job = StringField(label='Job', validators=[
        validators.DataRequired(),
        validators.AnyOf(values=['IT', 'Bank', 'HR'])
    ])
    # валидация дня рождения пользователя
    # 1. валидируем месяц, если он равен текущему - все хорошо, иначе - плохо
    birthday = DateField(label='Birthday')  # '1988-05-02' format

    def validate(self):
        rv = FlaskForm.validate(self)

        if self.birthday.data.month == datetime.date.today().month and rv:
            return True
        else:
            return False


app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='This key must be secret!',
    WTF_CSRF_ENABLED=False,
)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        print(request.form)
        form = ContactForm(request.form)
        print(form.validate())

        if form.validate():
            return ('valid', 200)
        else:
            return ('invalid', 400)

    if request.method == 'GET':
        return 'hello world!', 200


if __name__ == '__main__':
    app.run()
