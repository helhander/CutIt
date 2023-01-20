from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, URLField
from wtforms.validators import DataRequired, Length, Optional


class URLMapForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[DataRequired(message='Обязательное поле'), Length(1, 256)]
    )
    custom_id = URLField(
        'Ваш вариант кототкой ссылки',
        validators=[Optional(), Length(1,16)]
    )
    submit = SubmitField('Создать')