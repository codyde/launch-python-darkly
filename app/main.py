from flask.templating import render_template
from flask import Flask, json, jsonify
import ldclient
from ldclient.config import Config

app = Flask(__name__)

user = {
    "key": "aa0ceb",
    "firstName": "Mara",
    "lastName": "Jade",
    "email": "mjade@coruscant.gov",
    "custom": {
      "groups": ["Jedi"]
    }
}

@app.route("/")
def get_feature():
    ldclient.set_config(Config("sdk-7e5424a3-01a1-43fb-93e1-f478f2bf9327"))
    show_feature = ldclient.get().variation("launchTheme", user, False)
    if show_feature == True:
        show_osmo = ldclient.get().variation("launchOsmo", user, "warning.png")
        print(show_osmo)
        ldclient.get().close()
        return render_template("home.html", osmo=show_osmo)
    else:
        ldclient.get().close()   
        return """
        <h1>Welcome to Python and LaunchDarkly</h1>
        <h2>This is highly boring and not on brand</h2>
        <h2>:(</h2>
        """

@app.route('/api')
def api_route():
    j = {"test":"data"}
    return jsonify(j)


if __name__ == '__main__':
    app.run(debug=True)
