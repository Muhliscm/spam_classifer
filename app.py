from flask_app import create_app

# comment added for git hub
app = create_app()

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
