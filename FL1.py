from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def f1():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    lines = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
             'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']
    lines = '<br>'.join(lines)
    return lines


@app.route('/image_mars')
def image_mars():
    return f'''
    <!doctype html>
        <html lang="en">
            <head>
              <h1>Жди нас, Марс!</h1>
              <img src="{url_for('static', filename='img/mars2.jpg')}">
              <p>Вот она какая, красная планета</p>
            </head>
    </html>
            '''


@app.route('/promotion_image')
def promotion_image():
    return f'''
        <!doctype html>
            <html lang="en">
                <head>
                  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
                   integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" 
                   crossorigin="anonymous">
                  <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                  <h1>Жди нас, Марс!</h1>
                  <img src="{url_for('static', filename='img/mars2.jpg')}">
                  <div class="alert alert-danger" role="alert">
                      Человечество вырастает из детства
                    </div>
                  <div class="alert alert-warning" role="alert">
                      Человечеству мала одна планета
                    </div>
                  <div class="alert alert-success" role="alert">
                      Мы сделаем обитаемыми безжизненные пока планеты
                    </div>
                  <div class="alert alert-info" role="alert">
                      И начнем с Марса!
                    </div>
                  <div class="alert alert-primary" role="alert">
                      Присоединяйся!
                    </div>
                </head>
        </html>
                '''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
