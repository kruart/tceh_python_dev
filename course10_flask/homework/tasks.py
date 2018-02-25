# Реализовать на Flask
from flask import Flask, jsonify, request
from flask_wtf import FlaskForm
from wtforms import StringField, validators

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='This key must be secret!',
    WTF_CSRF_ENABLED=False,
)


# 1. По адресу /locales должен возвращаться массив в формате json с тремя локалями: ['ua', 'en', 'it']
@app.route('/locales')
def get_locales():
    return jsonify(['ua', 'en', 'it'])


# 2. По адресу /sum/<int:first>/<int:second> должен получать в url-адресе два числа, возвращать их сумму
@app.route('/sum/<int:first>/<int:second>')
def get_sum(first, second):
    return str(first + second)


# 3. По адресу /greet/<user_name> должен получать имя пользователя, возвращать текст 'Hello, имя_которое_прислали'
@app.route('/greet/<user_name>')
def print_greet(user_name):
    return 'Hello, {}'.format(user_name)


# 4. По адресу /form/user должен принимать POST запрос с параментрами: email, пароль и подтверждение пароля.
# Необходимо валидировать email, что обязательно присутствует, валидировать пароли, что они минимум 6 символов в длину и совпадают.
# Возрващать пользователю json вида:
# "status" - 0 или 1 (если ошибка валидации),
# "errors" - список ошибок, если они есть,
# или пустой список.
@app.route('/form/user', methods=['POST'])
def check_user():
    form = UserForm(request.form)

    if form.validate():
        return jsonify('0')
    else:
        if form.password != form.confirm_password:
            form.errors['passwords'] = ['Passwords are not equal']
        error_msg = ''
        for errors in form.errors.values():
             error_msg += errors[0] + '\n'
        return error_msg, 400


class UserForm(FlaskForm):
    email = StringField(label='Email', validators=[
        validators.Length(min=6, max=35), validators.Email()
    ])

    password = StringField(label='Password', validators=[
        validators.Length(min=6, max=17)
    ])

    confirm_password = StringField(label='ConfirmPassword', validators=[
        validators.Length(min=6, max=17)
    ])

    def validate(self):
        r = FlaskForm.validate(self)

        if self.password == self.confirm_password and r:
            return True
        else:
            return False


# 5. По адресу /serve/<path:filename> должен возвращать содержимое запрашиваемого файла из папки ./files.
# Файлы можно туда положить любые текстовые. А если такого нет - 404.
@app.route('/serve/<path:filename>')
def get_content_file(filename):
    try:
        with open('files/' + filename) as file:
            return file.read()
    except FileNotFoundError:
        return 'No such file: {}'.format(filename), 404


if __name__ == '__main__':
    app.run()