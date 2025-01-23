Drone controller: pi_controller.py
database frontend: database.py
website frontend: build.py
web client: index.html

Drone server: http://127.0.0.1:5001/drone
Web server: http://127.0.0.1:5000

drone controller writes directions to database frontend , and database frontend reads the old position from the redis database and writes the updated position to the redis database
the website frontend reads the updated position from the redis database, and the webclient reads the updated position from the website frontend