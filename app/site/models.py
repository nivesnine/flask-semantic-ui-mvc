from app import db


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120))
    phone = db.Column(db.String(25))
    message = db.Column(db.Text)

    def get_id(self):
        return self.id
