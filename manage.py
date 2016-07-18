
"""the book said to use flask.ext.scripts but the terminal says that
 this value has been depricated and to change it to what I now have"""

from sched.app import app

from flask_script import Manager
manager = Manager(app)
app.config['DEBUG'] = True # Ensure debugger will load

if __name__=='__main__':
    manager.run()

