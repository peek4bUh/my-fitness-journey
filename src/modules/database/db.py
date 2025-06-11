from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


### Probando como insertar datos en la base de datos ###
# with app.app_context():
#     db.create_all()

#     db.session.add(UserModel(username="example1"))

#     db.session.commit()

#     users = db.session.execute(db.select(UserModel)).scalars()

#     for user in users:
#         print(user.username)
