from flask import Flask, render_template
import logic

app = Flask(__name__)

@app.route('/')
def index():
    tenPlanets = logic.giveMeTenPlanets()
    return render_template('planets.html', tenPlanets = tenPlanets)


if __name__ == '__main__':
  app.run(port=5000, debug=True)