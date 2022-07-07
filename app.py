from flask import Flask

from covid_app import app

if __name__ == "__main__":
    app.run(debug=True)