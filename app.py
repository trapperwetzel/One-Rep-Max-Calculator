from flask import Flask, render_template, request
from proclasses import Lifter 

app = Flask(__name__)




@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        lifter_name = request.form['username']
        lifter_body_weight = request.form.get('bodyweight', 'N/A')
        lifter = Lifter(lifter_name, lifter_body_weight)
        for lift_name in ['squat', 'bench', 'deadlift']:
            lift_weight = request.form.get(f'{lift_name}_weight')
            lift_reps = request.form.get(f'{lift_name}_reps')
            if lift_weight and lift_reps:
                lifter.add_lift(lift_name, int(lift_weight), int(lift_reps))
        lifter_info = lifter.get_lifter_info()
        return render_template('lifter_info.html', lifter_info=lifter_info)
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html') 

@app.route('/contact') 
def contact():
    return render_template('contact.html') 







if __name__ == '__main__':
    app.run(debug=True)

























