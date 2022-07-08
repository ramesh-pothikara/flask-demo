from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import Length, EqualTo, Email, DataRequired, IPAddress


class S_Restart(FlaskForm):
    ip_addr = StringField(label='IP Addr:', validators=[Length(min=7), DataRequired()])
    submit = SubmitField(label='Submit', name = 'submit01')
    check_status  = SubmitField(label='check status')
    status = TextAreaField('status')


# {{ form.status(class="form-control") }}
# {{ form.check_status(class="btn btn-outline-primary") }}