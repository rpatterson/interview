"""
Make the Flask up runnable without an environment variable.
"""

from interview import app

if __name__ == "__main__":
    app.run(debug=True)
