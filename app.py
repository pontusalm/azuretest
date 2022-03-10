from flask import Flask,render_template
from models import User,user_manager,db
from flask_migrate import Migrate

app=Flask(__name__)
app.config.from_object('config.ConfigDebug')

db.app = app
db.init_app(app)
migrate = Migrate(app,db)
user_manager.app = app
user_manager.init_app(app,db,User)

@app.route("/")
def index():
    persons=User.query.all()
    return render_template("index.html", persons=persons)
if __name__ == "__main__":
    app.run(debug=True)
    




