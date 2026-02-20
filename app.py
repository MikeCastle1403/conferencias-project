from flask import Flask, render_template
from data import events, speakers
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    # Detalles de la conferencia
    conference_info = {
        "name": "Día de Google Cloud 2026",
        "date": "15 de Octubre de 2026",
        "location": "Moscone Center, San Francisco, CA",
        "description": "Únase a nosotros para un día de innovación, aprendizaje y networking con las mejores mentes en computación en la nube."
    }
    
    return render_template(
        'index.html', 
        events=events, 
        speakers=speakers, 
        conference=conference_info,
        now=datetime.datetime.now()
    )

if __name__ == '__main__':
    app.run(debug=True)
