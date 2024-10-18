from flask import Flask, render_template, request
from analysis import fetch_lap_times, detect_pit_stops, compare_average_lap_times, visualize_position_progression

app = Flask(__name__)

# Home page with options for different analyses
@app.route('/')
def home():
    return render_template('home.html')

# Route to handle user selection and show results
@app.route('/analyze', methods=['POST'])
def analyze():
    analysis_type = request.form['analysis_type']
    race_selection = request.form['race_selection']  # Get the selected race
    
    # Fetch the lap times for the selected race
    df = fetch_lap_times(race_selection)
    
    if df is None:
        result = "Failed to retrieve data for the selected race."
    else:
        if analysis_type == 'lap_times':
            result = df.head().to_html()  # Display the first few rows as a table
        elif analysis_type == 'pit_stops':
            result = detect_pit_stops(df).to_html()
        elif analysis_type == 'avg_lap_times':
            compare_average_lap_times(df)  # Display as a plot
            result = "Average lap times visualized."
        elif analysis_type == 'position_progression':
            visualize_position_progression(df)
            result = "Position progression visualized."
    
    return render_template('result.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
