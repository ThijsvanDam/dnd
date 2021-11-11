{
      "name": "Python: Flask",
      "type": "python",
      "request": "launch",
      "module": "flask",
      "env": {
        "FLASK_APP": "application.py",
        "FLASK_ENV": "development",
        "DATABASE_URL": "postgres://localhost/cs50w_project1_development",
        "FLASK_DEBUG": 1,
        "SECRET_KEY": "abcefefe"
      },
      "args": [
        "run",
      ],
      "jinja": true
    },