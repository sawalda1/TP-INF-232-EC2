from flask import Flask
from models.database import init_db

from routes.collect import collect_bp
from routes.dashboard import dashboard_bp
from routes.analysis import analysis_bp

app = Flask(__name__)

init_db()

app.register_blueprint(collect_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(analysis_bp)


if name == "main":
    app.run(host="0.0.0.0", port=5000)
