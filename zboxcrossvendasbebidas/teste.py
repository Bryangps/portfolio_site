from zboxcrossvendasbebidas import database, app
from zboxcrossvendasbebidas.models import Usuario


# with app.app_context():
#     usuario = Usuario(username='Bryan', email='bryan.gps18@gmail.com', senha='123123')
#     database.session.add(usuario)
#     database.session.commit()
#

# with app.app_context():
#     meu_usuario = Usuario.query.all()
#     print(meu_usuario)

with app.app_context():
    database.drop_all()
    database.create_all()
