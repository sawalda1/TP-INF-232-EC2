from flask import Blueprint, render_template
import pandas as pd
from models.database import get_connection

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard')
def dashboard():
    conn = get_connection()
    df = pd.read_sql_query("SELECT * FROM evaluations", conn)
    conn.close()

    moyenne = df['note_cours'].mean() if len(df) > 0 else 0

    return render_template("dashboard.html",
                           data=df.to_dict(orient="records"),
                           moyenne=round(moyenne, 2))