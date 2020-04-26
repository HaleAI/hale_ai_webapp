from flask import Flask, request, jsonify, render_template

app = Flask(__name__,static_folder="static\\")

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
	<!-- Index file -->
	<html lang="en">
	<head>
		<meta charset="utf-8">
		<title>
			Hale AI
		</title>
		<link rel="shortcut icon" href="assets\img\logo.jfif">
		<link rel="stylesheet" type="text/css" href="assets\css\style.css">
		<link href="https://fonts.googleapis.com/css2?family=Raleway:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap" rel="stylesheet">
		<link href="https://fonts.googleapis.com/css2?family=Dancing+Script&display=swap" rel="stylesheet">
		<link href="https://fonts.googleapis.com/css2?family=Open+Sans&display=swap" rel="stylesheet">
	</head>
	<body>
		<div id="hello2">
			<header id="nav">
				<h1>&nbsp;
					<img href="assets\img\logo.jfif" height=80 width=80><a href="index.html">
																		<br>&nbsp;Hale AI
																	</a>
				</h1>
				<ul>
					<li id="hello"><a href="home.html">
										Home
									</a>
					</li>
					<li><a href="">
							Services
						</a>
					</li>
					<li><a href="">
							About Us
						</a>
					</li>
					<li><a href="">
							Contact us
						</a>
					</li>
				</ul>
			</header>
		</div>
	</body>
</html>
'''
@app.route('/contact.html')
def contact():
    return '''
    
    '''

if __name__ == "__main__":
    app.run(debug=True)
