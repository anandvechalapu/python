Fast API:

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        # validate the username and password
        if valid_credentials(username, password):
            session["logged_in"] = True
            flash("Login successful")
            return redirect(url_for("index"))
        else:
            flash("Invalid credentials")
            return redirect(url_for("login"))
    return render_template("login.html")

@app.route("/configure")
def configure():
    if session.get("logged_in"):
        return render_template("configure.html")
    else:
        flash("Please login to access this page")
        return redirect(url_for("login"))

@app.route("/configureJiraSoftware", methods=["GET", "POST"])
def configureJiraSoftware():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        url = request.form.get("url")
        repoName = request.form.get("repoName")
        # validate the credentials
        if valid_credentials(username, password, url, repoName):
            session["configured_jira_software"] = True
            flash("Configuration successful")
            return redirect(url_for("index"))
        else:
            flash("Invalid credentials")
            return redirect(url_for("configureJiraSoftware"))
    return render_template("configureJiraSoftware.html")

@app.route("/viewJiraSoftwareConfigs")
def viewJiraSoftwareConfigs():
    if session.get("logged_in"):
        # fetch the details of the configurations
        configs = get_configs()
        return render_template("viewJiraSoftwareConfigs.html", configs=configs)
    else:
        flash("Please login to access this page")
        return redirect(url_for("login"))

@app.route("/editConfig/<title>", methods=["GET", "POST"])
def editConfig(title):
    if request.method == "POST":
        username = request.form.get("username")
        url = request.form.get("url")
        # update the details
        if update_config(title, username, url):
            flash("Configuration updated successfully")
            return redirect(url_for("viewJiraSoftwareConfigs"))
        else:
            flash("Error while updating configuration")
            return redirect(url_for("editConfig", title=title))
    else:
        config = get_config(title)
        return render_template("editConfig.html", config=config)

@app.route("/deleteConfig/<title>")
def deleteConfig(title):
    # delete the configuration
    if delete_config(title):
        flash("Configuration deleted successfully")
        return redirect(url_for("viewJiraSoftwareConfigs"))
    else:
        flash("Error while deleting configuration")
        return redirect(url_for("viewJiraSoftwareConfigs"))

@app.route("/addConfig", methods=["GET", "POST"])
def addConfig():
    if request.method == "POST":
        title = request.form.get("title")
        username = request.form.get("username")
        url = request.form.get("url")
        # add the configuration
        if add_config(title, username, url):
            flash("Configuration added successfully")
            return redirect(url_for("viewJiraSoftwareConfigs"))
        else:
            flash("Error while adding configuration")
            return redirect(url_for("addConfig"))
    return render_template("addConfig.html")