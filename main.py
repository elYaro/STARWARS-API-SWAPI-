from flask import Flask, render_template, request
import logic

app = Flask(__name__)

# main route to main page with Page1 (10 planets)
@app.route('/')
def index():
    tenPlanets = logic.giveMeTenPlanets()
    return render_template('planets.html', tenPlanets = tenPlanets)

# route to 10 Previous Planets (Page + (-1) )
@app.route('/previous')
def previous():
    urlTo10PreviousPlanets = request.args.get('previous')
    tenPreviousPlanets = logic.giveMeTenPreviousPlanets(urlTo10PreviousPlanets)
    return render_template('planets.html', tenPlanets = tenPreviousPlanets)

# route to 10 Next Planets (Page + 1 )
@app.route('/next')
def next():
    urlTo10NextPlanets = request.args.get('next')
    tenNextPlanets = logic.giveMeTenNextPlanets(urlTo10NextPlanets)
    return render_template('planets.html', tenPlanets = tenNextPlanets)   



if __name__ == '__main__':
  app.run(port=5000, debug=True)