from flask import Flask
app = Flask (__name__)

@app.route('/',methods=['GET'])
def hell():
  return "Hello human!"

if __name__ == '__main__':
  app.run()