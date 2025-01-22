from flask import Flask, request
from flask_cors import CORS
import redis

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.secret_key = 'dljsaklqk24e21cjn!Ew@@dsa5'

# change this to connect to your redis server
# ===============================================
rs = redis.Redis(host="localhost",port=6379)
# ===============================================

rs.set('longitude', 13.21008)
rs.set('latitude', 55.71106)

#write your own movedrone fuction here, this function should
# 1. get the lastest longitude and latitude data
# 2. update longitude and latitude values with input movement data
# 3. write the updated data to the database
# ===============================================
def moveDrone(d_long, d_la):
    long = float(rs.get('longitude'))
    n_long = long + d_long
    rs.set('longitude', n_long)
    la = float(rs.get('latitude'))
    n_la = la + d_la
    rs.set('latitude', n_la)

# ===============================================

@app.route('/drone', methods=['POST'])
def drone():
    movement = request.get_json()
    d_long = movement['longitude']/10000
    d_la = movement['latitude']/10000
    moveDrone(d_long, d_la)
    return 'Get data'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='5001')
