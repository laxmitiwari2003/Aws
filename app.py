
from flask import Flask

application = Flask(__name__)

@application.route("/")
def home():
    return """
    <html>
        <head>
            <title>My AWS Flask Project</title>
        </head>
        <body style="font-family: Arial; text-align: center; padding: 50px;">
            <h1>Welcome to My Flask Application!</h1>
            <p>My Python web application is running on AWS.</p>
            <h3>Deployment Successful!</h3>
        </body>
    </html>
    """

if __name__ == "__main__":
    application.run()
