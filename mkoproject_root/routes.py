from mkoproject_root import app

@app.route('/')
def home():
    return "Hello, World!"
