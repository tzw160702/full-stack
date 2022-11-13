#!usr/bin/python3
# -*- coding: UTF-8 -*-

from flask_script import Manager
from ylshini import create_app

app = create_app()
manager = Manager(app)


if __name__ == "__main__":
    app.run(
        host=app.config['HOSTNAME'], port=app.config['HOSTPORT'],
        debug=True, threaded=True)



