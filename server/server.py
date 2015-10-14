from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

app = Flask(__name__);


@app.route('/<username>')
def hello(username):
  return 'Hello %s' % username

if __name__ == '__main__':
  app.run()