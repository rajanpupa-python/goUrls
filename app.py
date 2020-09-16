from flask import Flask, redirect, render_template

app = Flask(__name__)


routes_map = {
    'google': 'http://www.google.com',
    'rajan': 'http://www.rajanu.com.np',
    'blog': 'http://blog.rajanu.com.np'
}

@app.route('/go/<name>')
def go_redirect(name):
    url = routes_map.get(name)
    if url:
        print('Found', url)
        return redirect(url, code=302)
    else:
        return render_template('error.html', name=name)


if __name__ == '__main__':
    app.run()
