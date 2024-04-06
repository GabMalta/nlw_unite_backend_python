from src.main.server.server import app
from src.models.settings.connection import db_connect

if __name__ == '__main__':
    
    db_connect.connect_to_db()
    app.run(host='127.0.0.1', port=8000, debug=True)