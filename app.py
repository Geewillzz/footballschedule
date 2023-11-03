from flask import Flask, render_template

app = Flask(__name__)

# Dummy fixture schedule data (you can replace this with real data)
schedule = [
    {'home_team': 'Real Madrid', 'away_team': 'Barcelona', 'date': '2023-11-05'},
    {'home_team': 'Liverpool', 'away_team': 'Aresenal', 'date': '2023-11-10'},
    {'home_team': 'AC Milan', 'away_team': 'Inter Milan', 'date': '2023-11-15'},
    # Add more fixtures here
]

@app.route('/')
def index():
    return render_template('schedule.html', schedule=schedule)

if __name__ == '__main__':
    app.run(debug=True)
