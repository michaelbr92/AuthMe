from authme import app
debug, port = config_parser.flask_settings()
app.run(debug=debug, host="0.0.0.0", port=port, threaded=True)
