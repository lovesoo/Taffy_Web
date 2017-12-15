from app import app
from flask_bootstrap import Bootstrap
app.config['SECRET_KEY'] = 'Life is short,You need Taffy!'
bootstrap = Bootstrap(app)
app.run(debug=True)
