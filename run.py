from app import app

# If you need to make the application visible outside, change the
# ip address to your own ip. You can also change the port that
# the application will be listening.
IP = '127.0.0.1'
PORT = 5008

context = ('NCBCert.pem', 'NCBKey.pem')


app.run(host=IP, debug=True, port=PORT, ssl_context=context, threaded=True)

