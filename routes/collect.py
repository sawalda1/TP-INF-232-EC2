from flask import Blueprint, render_template, request, redirect
from models.database import get_connection

collect_bp = Blueprint('collect', __name__)

@collect_bp.route('/')
def form():
    return render_template("form.html")

@collect_bp.route('/submit', methods=['POST'])
def submit():
    data = request.form

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO evaluations (cours, note_cours, clarte, organisation, difficulte)
    VALUES (?, ?, ?, ?, ?)
    """, (
        data['cours'],
        float(data['note_cours']),
        float(data['clarte']),
        float(data['organisation']),
        float(data['difficulte'])
    ))

    conn.commit()
    conn.close()

    return redirect("/dashboard")