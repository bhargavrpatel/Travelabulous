# Importing packages and modules
from flask import Flask, render_template
from flask.ext.mongoalchemy import MongoAlchemy


# Setup "app" as per Flask.
app = Flask(__name__)
app.config['MONGOALCHEMY_DATABASE'] = 'travelabulous'

# Hook an ORM to the app. We are using MongoAlchemy
db = MongoAlchemy(app)


## MODEL DEFINITION START

class Option(db.Document):
  text = db.StringField(required = True)
  isPictureOption = db.BoolField(required = True)

  def __unicode__(self):
    return self.text
  def __str__(self):
        return unicode(self).encode('utf-8')


class Question(db.Document):
  text = db.StringField(required = True)
  options = db.ListField(db.DocumentField('Option'), required = False)

  def __unicode__(self):
    return self.text
  def __str__(self):
    return unicode(self).encode('utf-8')

  def __repr__(self):
    return "Question: " + self.text + "\nOptions: " + ', '.join(str(x) for x in self.options)


class User(db.Document):
  username = db.StringField(required = True)
  answersArray = db.ListField(db.DocumentField('Option'), required = True)    # Here we are making an array of SELECTED options
  compiutedEpicenter = db.FloatField(default = None, allow_none = True, required = False) # this will be calculated by the Epicenter Calculating Subsytem


  def __unicode__(self):
    return self.text
  def __str__(self):
        return unicode(self).encode('utf-8')


## MODEL DEFINITION END


# Routes
@app.route('/')
def hello_world():
  return "Hello World!"

# Test route
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name = None):
  return render_template('hello.html', name=name)



# App runner
if __name__ == "__main__":
  app.run()
