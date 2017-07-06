from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TextAreaField, FieldList
from wtforms.validators import DataRequired


class EntryForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    date = DateField('Date')
    time_spent = StringField('Time Spent', validators=[DataRequired()])
    learned = TextAreaField('What I Learned')
    resources = TextAreaField('Resources to Remember')
    tags = FieldList(StringField('Tag'))
