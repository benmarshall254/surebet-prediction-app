from flask import Flask, render_template_string
from predictions import get_predictions

app = Flask(__name__)

@app.route('/')
def home():
    predictions = get_predictions()
    return render_template_string("""
        <h1>Surebet Predictions</h1>
        <ul>
            {% for game in predictions %}
                <li>{{ game }}</li>
            {% endfor %}
        </ul>
    """, predictions=predictions)
