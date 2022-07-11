from flask import Flask
from flask import redirect
from flask import render_template
from flask import url_for
from flask import request

app = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            template_folder='template')


@app.route("/")
def home_view():
        return render_template("index.html")

@app.route("/login", methods=['POST'])
def redirect_form():
    data = request.form
    print(data)
    if data["username"] != "rafa" and data["passwd"] != "rafa":
        print(data["username"], data["passwd"])
        return "Error"
    return redirect(url_for("dashboard"))

@app.route("/dashboard", methods=['GET'])
def dashboard():
        return render_template("dashboard.html")


# if __name__ == "__main__":
#     app.run(debug=True, host='0.0.0.0')


