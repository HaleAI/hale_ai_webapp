from flask import Flask, request, jsonify, render_template

app = Flask(__name__,);

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
	<html lang="en">
	<head>
		<meta charset="utf-8">	
		<title>
			HaleAI
		</title>
		<link rel="shortcut icon" href="/static/assets/img/logo.png">
		<link rel="stylesheet" type="text/css" href="static/assets/css/style.css">
	</head></a>
	<body>
		<div id="hello2">
			<header id="nav">
				<a href="/">
					<img src="static/assets/img/logo.png" height=120 width=120>
				</a>
				<ul>
					<li id="hello">
						<a href="/">
							Home
						</a>
					</li>
					<li>
						<a href="">
							Services
						</a>
					</li>
					<li>
						<a href="">
							Contact us
						</a>
					</li>
				</ul>
			</header>
			<br><br>
			<h1>
				&nbsp;
				<a href="/">
					&nbsp;HaleAI
				</a>
			</h1>
			<br><br><br><br><br><br><br>
			<div id="aboutback">
				<h1 id="about_head">
					About us
				</h1><br>
				<h1 id="about">
					In these times, health is a major issue and quality healthcare isn't available to all. We, at HaleAI, aim at providing support to healthcare professionals using artificial intelligence. It can help in diagnosis as well as prognosis of various diseases that can sometimes be overlooked or not have obvious symptoms. Hence, the company provides a platform for faster detection of diseases using technology that will benefit the doctors, as more optimum solutions can be found. Our mission is to help healthcare professionals and transform the healthcare industry. Ultimately, it is the life that wins.
					<br>
			</div>
		</div>
		<div id="teamback">
			<br><br>
			<h1 id="team_head">
				Our Team
			</h1>
			<br>
			<br>
		</div>
		<div id="teamback">
			<div class="container">
				<div class ="row">
					<div class="col order-xs-1 order-sm-1 order-md-2">
						<center>
							<div id="teamcircle">
								<img src="/static/assets/img/team/Snehil.jpg">
							</div>
						</center>
						<div id="teamdesig">
							<div class ="row">
								<div class="col">
									<div class="row">
										<div class="col">
											Snehil Kumar
										</div>
									</div>
									<div class="row">
										<div class="col">
											CEO & CTO
										</div>
									</div>
									<div class="row">
										<div class="col">
											<a href="https://www.linkedin.com/in/snehil-kumar-88b609142/">
												<img src="/static/assets/img/linkedin.png" height="25" width="25">
											</a>
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>
					<div class="col order-xs-2 order-sm-2 order-md-1">
						<center>
							<div id="teamcircle">
								<img src="/static/assets/img/team/AmitKumar.jpg">
							</div>
						</center>
						<div id="teamdesig">
							<div class ="row">
								<div class="col">
									<div class="row">
										<div class="col">
											Amit Kumar
										</div>
									</div>
									<div class="row">
										<div class="col">
											Mentor
										</div>
									</div>
									<div class="row">
										<div class="col">
											<a href="https://www.linkedin.com/in/amit-kumar-6a215b36/">
												<img src="/static/assets/img/linkedin.png" height="25" width="25">
											</a>
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>
						<div class="col order-xs-3 order-sm-3 order-md-3">
							<center>
								<div id="teamcircle">
									<img src="/static/assets/img/team/ShubhangNandan.jpg">
								</div>
							</center>
							<div id="teamdesig">
								<div class ="row">
									<div class="col">
										<div class="row">
											<div class="col">
												Shubhang Nandan
											</div>
										</div>
										<div class="row">
											<div class="col">
												COO
											</div>
										</div>
										<div class="row">
											<div class="col">
												<a href="https://www.linkedin.com/in/shubhang-nandan-b2444b12a/">
													<img src="/static/assets/img/linkedin.png" height="25" width="25">
												</a>
											</div>
										</div>
									</div>
								</div>
						</div>
					</div>
				</div>
				<br>
				<div class ="row">
					<div class="col">
						<center>
							<div id="teamcircle">
								<img src="/static/assets/img/team/Divyam.jpg">
							</div>
						</center>
						<div id="teamdesig">
							<div class ="row">
								<div class="col">
									<div class="row">
										<div class="col">
											Divyam Tiwari
										</div>
									</div>
									<div class="row">
										<div class="col">
											Content team lead
										</div>
									</div>
									<div class="row">
										<div class="col">
											<a href="https://www.linkedin.com/in/divyam-bb7411184">
												<img src="/static/assets/img/linkedin.png" height="25" width="25">
												</a>
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>
						<div class="col">
							<center>
								<div id="teamcircle">
									<img src="/static/assets/img/team/Suvashish.jpg">
								</div>
							</center>
							<div id="teamdesig">
								<div class ="row">
									<div class="col">
										<div class="row">
											<div class="col">
												Suvasish Pandey
											</div>
										</div>
										<div class="row">
											<div class="col">
												Lead Bio-sciences Scientist
											</div>
										</div>
										<div class="row">
											<div class="col">
												<a href="https://in.linkedin.com/in/suvashish-pandey-a5b0a719b">
													<img src="/static/assets/img/linkedin.png" height="25" width="25">
												</a>
											</div>
										</div>
									</div>
								</div>
							</div>
						</div>
						<div class="col">
							<center>
								<div id="teamcircle">
									<img src="/static/assets/img/team/Thejaswi.jpg">
								</div>
							</center>
							<div id="teamdesig">
								<div class ="row">
									<div class="col">
										<div class="row">
											<div class="col">
												Thejaswi B K
											</div>
										</div>
										<div class="row">
											<div class="col">
												Lead Devops engineer
											</div>
										</div>
										<div class="row">
											<div class="col">
												<a href="https://www.linkedin.com/in/thejaswibk">
													<img src="/static/assets/img/linkedin.png" height="25" width="25">
												</a>
											</div>
										</div>
									</div>
								</div>
						</div>
					</div>
				</div>
				<div class ="row">
					<div class="col">
						<center>
							<div id="teamcircle">
								<img src="/static/assets/img/team/AnirudhBelwadi.jpg">
							</div>
						</center>
						<div id="teamdesig">
							<div class ="row">
								<div class="col">
									<div class="row">
										<div class="col">
											Anirudh Belwadi
										</div>
									</div>
									<div class="row">
										<div class="col">
											Full stack Developer
										</div>
									</div>
									<div class="row">
										<div class="col">
											<a href="https://www.linkedin.com/in/anirudh-belwadi-7a8707182/">
												<img src="/static/assets/img/linkedin.png" height="25" width="25">
											</a>
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>
						<div class="col">
							<center>
								<div id="teamcircle">
									<img src="/static/assets/img/team/Saili.jpg">
								</div>
							</center>
							<div id="teamdesig">
								<div class ="row">
									<div class="col">
										<div class="row">
											<div class="col">
												Saili Myana
											</div>
										</div>
											<div class="row">
											<div class="col">
												AI Developer
											</div>
										</div>
										<div class="row">
											<div class="col">
												<a href="https://www.linkedin.com/in/saili-myana">
													<img src="/static/assets/img/linkedin.png" height="25" width="25">
												</a>
											</div>
										</div>
									</div>
								</div>
							</div>
						</div>
						<div class="col">
							<center>
								<div id="teamcircle">
									<img src="/static/assets/img/team/K.SaiRithvik.jpg">
								</div>
							</center>
							<div id="teamdesig">
								<div class ="row">
									<div class="col">
										<div class="row">
											<div class="col">
												Sai Rithvik Kanakamedala
											</div>
										</div>
										<div class="row">
											<div class="col">
													AI Developer
											</div>
										</div>
										<div class="row">
											<div class="col">
												<a href="http://linkedin.com/in/rithvik7">
													<img src="/static/assets/img/linkedin.png" height="25" width="25">
												</a>
											</div>
										</div>
									</div>
								</div>
						</div>
					</div>
				</div>
				<div class ="row">
					<div class="col">
						<center>
							<div id="teamcircle">
								<img src="/static/assets/img/team/PrincePandey.jpg">
							</div>
						</center>
						<div id="teamdesig">
							<div class ="row">
								<div class="col">
									<div class="row">
										<div class="col">
											Prince Pandey
										</div>
									</div>
									<div class="row">
										<div class="col">
											Full stack Intern
										</div>
									</div>
									<div class="row">
										<div class="col">
											<a href="https://www.linkedin.com/in/prince-pandey-5a76b0178/">
												<img src="/static/assets/img/linkedin.png" height="25" width="25">
											</a>
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>
						<div class="col">
							<center>
								<div id="teamcircle">
									<img src="/static/assets/img/team/Manas.jpg">
								</div>
							</center>
							<div id="teamdesig">
								<div class ="row">
									<div class="col">
										<div class="row">
											<div class="col">
												Manas Churi
											</div>
										</div>
										<div class="row">
											<div class="col">
												AI Research Intern
											</div>
										</div>	
										<div class="row">
											<div class="col">
												<a href="https://www.linkedin.com/in/manaschuri11">
													<img src="/static/assets/img/linkedin.png" height="25" width="25">
												</a>
											</div> 
										</div>
									</div>
								</div>
							</div>
						</div>
						<div class="col">
							<center>
								<div id="teamcircle">
									<img src="/static/assets/img/team/UjjawalGupta.jpg">
								</div>
							</center>
							<div id="teamdesig">
								<div class="row">
									<div class="col">
										<div class="row">
											<div class="col">
												Ujjawal Gupta
											</div>
										</div>
										<div class="row">
											<div class="col">
												AI Research Intern
												</div>
										</div>
										<div class="row">
											<div class="col">
												<a href="https://www.linkedin.com/in/ujjawal-gupta-015ba6168">
													<img src="/static/assets/img/linkedin.png" height="25" width="25">
												</a>
											</div>
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
		<div id="freetrial">
		<br><br>
		<div id="trialtext">Sign Up for a Free trial!</div>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
		<form id="trialform">
			<input type="text" id="texttrial" placeholder="Email address">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<button id="trialbutton">Sign Up</button>
		</form>
		<br><br><br>
		</div>
		<hr id="freetrial2">
		<footer id="foot"><br><center>
				<a href="/">
					<img src="/static/assets/img/logo.png" height=150 width=150>
				</a></center>
			<div id="footname">
				<center>HaleAI</center>
			</div><br><br>
			<div id="socialmediahead">
				<ul>IMPORTANT LINKS<br>
					<li><a href="/">Home</a></li>
					<li><a href="">Services</a></li>
				</ul>
				<ul>GET IN TOUCH<br>
					<li><a href="mailto:haleai1994@gmail.com">Email</a></li>
					<li><a href="tel:+917004171728">Contact</a></li>
				</ul>
				<ul>SOCIAL MEDIA<br>
					<li><a href="https://www.instagram.com/haleai03/"><img src="/static/assets/img/insta.jpg" height="30" width="30"></a></li>
					<li><a href="https://www.linkedin.com/company/hale-ai/LinkedIn"><img src="/static/assets/img/linkedin.png" height="30" width="30"></a></li>
					<li><a href="https://www.facebook.com/haleai/"><img src="/static/assets/img/facebook.jpg" height="30" width="30"></a></li>
				</ul>
				<ul>ARTICLES
					<li><a href="https://snehil03july.wixsite.com/website-4/file-name">Diabetic Retinopathy Diagnosis</a></li>
				</ul>
			</div><br>
			<center><hr id="footruler"></center><br><br><br><br>
		</footer>
	</body>
</html>
'''
@app.route('/contact.html')
def contact():
    return '''
    
    '''

if __name__ == "__main__":
    app.run(debug=True);