from flask import Blueprint, render_template
import pandas as pd
from models.database import get_connection
from services.regression import train_model

analysis_bp = Blueprint('analysis', __name__)

@analysis_bp.route('/analysis')
def analysis():
    conn = get_connection()
    df = pd.read_sql_query("SELECT * FROM evaluations", conn)
    conn.close()

    if len(df) < 2:
        return "Pas assez de données"

    model = train_model(df)

    return render_template(
        "analysis.html",
        coef=round(model.coef_[0], 2),
        intercept=round(model.intercept_, 2)
    )