from flask import Flask, request, jsonify, render_template



app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')




@app.route('/predict',methods=['POST'])
def predict():
	#user = request.form["User Response"]
	#heman = user + "player"
	return render_template('index.html', prediction_text='Will be predicted soon. Working on Model')

if __name__ == "__main__":
    app.run(debug=True)