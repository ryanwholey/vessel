from flask import Flask
app = Flask (__name__)

@app.route('/')
def hell():
  return "Hello human!"

if __name__ == '__main__':
  app.run()