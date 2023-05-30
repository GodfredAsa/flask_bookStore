from db import db


class UserModel(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(20))
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    username = db.Column(db.String(80))
    email = db.Column(db.String(80), unique=True)
    imageUrl = db.Column(db.String(250))
    wallet = db.Column(db.Float)
    is_admin = db.Column(db.Boolean, default=False)
    password = db.Column(db.String(80))

    def __init__(self, firstName, lastName, username, email, imageUrl,  password, wallet):
        self.first_name = firstName
        self.last_name = lastName
        self.email = email
        self.wallet = wallet
        self.imageUrl = imageUrl
        self.username = username
        self.password = password
        self.is_admin = False
        self.wallet = 50.0

    def __str__(self):
        return f"<User: ID:{self.id}, Email:{self.email}, Username:{self.username} wallet:{self.wallet}>"

    def json(self):
        return {
            "userId": self.user_id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email,
            "imageUrl": self.imageUrl,
            "isAdmin": self.is_admin,
            "wallet": self.wallet,
            "username": self.username
        }

    @classmethod
    def find_by_email(cls, email: str) -> 'UserModel':
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_id(cls, _id: int):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
