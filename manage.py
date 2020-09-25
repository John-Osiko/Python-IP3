from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server

from app import create_app,db
from app.models import User, Post, Comment

app = create_app('development')

manager = Manager(app)
manager.add_command('server', Server(use_debugger=True))

#migrate = Migrate(app, db)
#manager.add_command('db', MigrateCommand)


@manager.shell
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Comment': Comment}


@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=4).run(tests)


if __name__ == "__main__":
    manager.run()
