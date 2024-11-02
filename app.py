from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ai', methods=['GET', 'POST'])
def ai():
    if request.method == 'POST':
        question = request.form['question']
        # Integrate AI response logic here
        response = "AI response to the question"
        return render_template('ai.html', response=response)
    return render_template('ai.html')

@app.route('/weather')
def weather():
    # Integrate weather API logic here
    weather_data = "Live weather data"
    return render_template('weather.html', weather_data=weather_data)

@app.route('/database', methods=['GET', 'POST'])
def database():
    if request.method == 'POST':
        plant_name = request.form['plant_name']
        watering_instructions = request.form['watering_instructions']
        soil_instructions = request.form['soil_instructions']
        # Save to database logic here
    return render_template('database.html')

@app.route('/funfacts')
def funfacts():
    fun_facts = ["Fact 1", "Fact 2", "Fact 3"]
    return render_template('funfacts.html', fun_facts=fun_facts)

if __name__ == '__main__':
    app.run(debug=True)
