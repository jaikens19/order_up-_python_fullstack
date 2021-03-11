from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, SelectField, BooleanField, SubmitField, PasswordField, SelectMultipleField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    employee_number = StringField('Employee number', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
    

class MenuItemAssignmentForm(FlaskForm):
    menu_item_ids = SelectMultipleField("Menu items", coerce=int)


class TableAssignmentForm(FlaskForm):
    assign = SubmitField("Assign")
    employee = SelectField("Servers", [DataRequired()], coerce=int)
    tables = SelectField("Tables", [DataRequired()], coerce=int)
