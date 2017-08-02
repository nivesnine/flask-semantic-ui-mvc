from wtforms import form, fields, validators
from wtforms.widgets import TextArea


class ContactForm(form.Form):
    name = fields.StringField(validators=[validators.required()])
    phone = fields.StringField(validators=[validators.required()])
    email = fields.StringField(validators=[validators.required()])
    message = fields.StringField(widget=TextArea())
