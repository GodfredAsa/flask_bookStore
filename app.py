from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from db import db
from resources.admin import Admin
from resources.user import RegisterUser, User, Users, UserLogin
from resources.book import CreateBook, Books, Book
from resources.sale import Sale


app = Flask(__name__)
jwt = JWTManager(app)
api = Api(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["JWT_SECRET_KEY"] = "admin"


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(RegisterUser, "/register")
api.add_resource(Users, "/users")
api.add_resource(User, "/users/<string:email>")
api.add_resource(CreateBook, "/books")
api.add_resource(Books, "/books/")
api.add_resource(Book, "/books/<string:title>")
api.add_resource(Sale, "/sales")
api.add_resource(Admin, "/admin")
api.add_resource(UserLogin, "/login")


if __name__ == "__main__":
    db.init_app(app)
    app.run(port=5001, debug=True)


