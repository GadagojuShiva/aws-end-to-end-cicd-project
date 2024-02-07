from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return """
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f0f0f0;
            text-align: center;
            padding: 50px;
        }

        h1 {
            color: #333;
        }
    </style>
    <body>
        <h1>Hello, world!</h1>
        <p>Welcome to my beautiful Flask application!</p>
        <pre>
            .--.
           |o_o |
           |:_/ |
          //   \ \
         (|     | )
        /'\_   _/`\
        \___)=(___/

        </pre>
    </body>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0')
