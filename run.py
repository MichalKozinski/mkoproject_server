# import sys
# #sys.path.insert(0, '/root/mkoproject/mkoproject_root')

# from app import app

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)