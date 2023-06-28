from flask_wtf import FlaskForm
from wtforms import StringField,FileField,SubmitField,IntegerField,TextAreaField
from wtforms.validators import DataRequired, Length, Email
from wtforms.validators import ValidationError
from flask_wtf.file import FileRequired, FileAllowed



class RegistrationForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired(),Length(min=2,max=20)],render_kw={"placeholder": "Enter Name"})
    email=StringField('Email',validators=[DataRequired(),Email()], render_kw={"placeholder": "Enter Email"})
    Mobile = IntegerField('Mobile',validators=[DataRequired()], render_kw={"placeholder": "Enter Mobile Number"})
    message = TextAreaField('Message', validators=[DataRequired()], render_kw={"placeholder": "Enter your message"})
    submit=SubmitField('SEND MESSAGE')

class ImageForm(FlaskForm):
    image = FileField('Image', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png', 'gif'])], render_kw={"placeholder": "Choose Image"})
    submit=SubmitField('SEND IMAGE')