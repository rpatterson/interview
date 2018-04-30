"""
Make the Flask up runnable without an environment variable.
"""

from api import db

if __name__ == "__main__":
    db.create_all()
