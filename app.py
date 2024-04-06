from website import create_app

# comment added for git hub
app = create_app()
app.run(host='0.0.0.0', port=8080)
