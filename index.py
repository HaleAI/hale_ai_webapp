from flask import Flask, request, jsonify, render_template

app = Flask(__name__,static_folder="static\\")

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
	<html lang="en">
	<head>
		<meta charset="utf-8">
		<script src="assets\js\jquery.js">
			jQuery('.scroll_to').click(function(e){
    			var jump = $(this).attr('href');
	    		var new_position = $(jump).offset();
    			$('html, body').stop().animate({ 
					scrollTop: new_position.top 
				}, 1000);
    			e.preventDefault();
			});
		</script>
		<title>
			Hale AI
		</title>
		<link rel="shortcut icon" href="assets\img\logo.jfif">
		<link rel="stylesheet" type="text/css" href="assets\css\style.css">
		<link href="https://fonts.googleapis.com/css2?family=Raleway:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap" rel="stylesheet">
		<link href="https://fonts.googleapis.com/css2?family=Dancing+Script&display=swap" rel="stylesheet">
		<link href="https://fonts.googleapis.com/css2?family=Open+Sans&display=swap" rel="stylesheet">
	</head></a>
	<body>
		<div id="hello2">
			<header id="nav">&nbsp;&nbsp;&nbsp;&nbsp;<a href="/"><img src="assets\img\logo.jfif" height=80 width=80></a>
				<ul>
					<li id="hello"><a href="/">
										Home
									</a>
									
					</li>
					<li><a href="">
							Services
						</a>
					</li>
					<li><a href="#team_head" class="scroll_to">
							About Us
						</a>
					</li>
					<li><a href="">
							Contact us
						</a>
					</li>
				</ul>
			</header>
			<h1>&nbsp;
				<a href="/">&nbsp;Hale AI
				</a>
			</h1>
		</div>
		<div id="teamback">
			<h1 id="team_head">About us</h1><br><br>
			<h1 id="about">In these times, health is a major issue and quality healthcare isn't available to all.<br>We, at HaleAI, aim at providing support to healthcare professionals using artificial intelligence. It can help in diagnosis as well as prognosis of various diseases that can sometimes be overlooked or not have obvious symptoms. Hence, the company provides a platform for faster detection of diseases using technology that will benefit the doctors, as more optimum solutions can be found.<br>Our mission is to help healthcare professionals and transformation in the healthcare industry. Ultimately, it is the life that wins.</h1>
		</div>
		<div id="teamback">
		<br><br>
		<h1 id="team_head">Our team</h1>
		<br><br>
		<div id="teamLead">
			<img src="assets/img/team/Snehil.jpg" height=200 width=200>
		</div>
		<br>
		<table id="team">
   			<tr>
      			<td>
					<div>
						<img src="assets/img/team/AmitKumar.jpg" height=200 width=200>
					</div>
				</td>
      			<td>
					<div>
						<img src="assets/img/team/Thejaswi.jpg" height=200 width=200>
					</div>
				</td>
				<td>
					<div>
						<img src="assets/img/team/Divyam.jpg" height=200 width=200>
					</div>
				</td>
				<td>
					<div>
						<img src="assets/img/team/Saili.jpg" height=200 width=200>
					</div>
				</td>
				<td>
					<div>
						<img src="assets/img/team/Suvashish.jpg" height=200 width=200>
					</div>
				</td>
			</tr>
		</table>
		<br>
		<table id="team">
			<tr>
				<td>
					<div>
						<img src="assets/img/team/K.SaiRithvik.jpg" height=200 width=200>
					</div>
				</td>
				<td>
					<div>
						<img src="assets/img/team/Manas.jpg" height=200 width=200>
					</div>
				</td>
				<td>
					<div>
						<img src="assets/img/team/AnirudhBelwadi.jpg" height=200 width=200>
					</div>
				</td>
				<td>
					<div>
						<img src="assets/img/team/PrincePandey.jpg" height=200 width=200>
					</div>
				</td>
				<td>
					<div>
						<img src="assets/img/team/UjjawalGupta.jpg" height=200 width=200>
					</div>
				</td>
   			</tr>
		</table>
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
