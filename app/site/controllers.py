from flask import Blueprint, request, render_template, \
                  flash, redirect, url_for
from app import db  
from app.site.forms import ContactForm
from app.site.models import Contact

site = Blueprint('site', __name__, url_prefix='')


# Set the route and accepted methods
@site.route('/', methods=['GET', 'POST'])
def index():
    contact = Contact()
    form = ContactForm(request.form)
    if request.method == "POST" and form.validate():
        form.populate_obj(contact)
        db.session.add(contact)
        db.session.commit()
        flash('form submitted')
        return redirect(url_for('site.index'))
    return render_template("site/index.html", form=form)
