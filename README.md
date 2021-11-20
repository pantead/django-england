# django-england
#base.html
<html>
    <head>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"
         integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        {% block head %}
        <title>Base</title>
        {% endblock %}
    </head>
    <body>
        <br>
        <div class="container">
            <nav class="navbar navbar-default">
            <div class="container-fluid">
              <div class="navbar-header">
                <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
                  <span class="sr-only">Toggle navigation</span>
                  <span class="icon-bar"></span>
                  <span class="icon-bar"></span>
                  <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="/">Social Network</a>
                <a class="navbar-brand" href="/account/login">Login</a>
                <a class="navbar-brand" href="/account/register">Signup</a> 
              </div>
              <div id="navbar" class="navbar-collapse collapse">
                {% if user.is_authenticated %}
                <ul class="nav navbar-nav">
               
                  {% comment %} <li><a href="{% url 'accounts:view_profile' %}">Profile</a></li>
                  <li><a href="{% url 'accounts:edit_profile' %}">Edit Profile</a></li>
                  <li><a href="{% url 'accounts:change_password' %}">Change Password</a></li>  {% endcomment %}
                </ul>
                {% comment %} <ul class="nav navbar-nav navbar-right">
                    <li><a href="{% url 'accounts:logout' %}">Log out</a></li>
                </ul> {% endcomment %}
                {% else %}
                {% comment %} <ul class="nav navbar-nav">
                    <li><a href="{% url 'accounts:reset_password' %}">Reset Password</a></li>
                </ul> {% endcomment %}
                <ul class="nav navbar-nav navbar-right">
                  <li><a href="{% url 'accounts:login' %}">Login</a></li>
                  <li><a href="{% url 'accounts:register' %}">Register</a></li>
                  <li><a href="{% url 'accounts:reset_password' %}">Reset Password</a></li>
                </ul>
                {% endif %}
              </div><!--/.nav-collapse -->
            </div><!--/.container-fluid -->
          </nav>
        </div>
        {% block body %}
            <h1>Base</h1>
        {% endblock %}
    </body>

</html>
