'https://dailypythonprojects.substack.com/p/what-is-if-__name__-__main__-for?utm_source=post-email-title&publication_id=2286155&post_id=146875128&utm_campaign=email-post-title&isFreemail=true&r=21houv&triedRedirect=true&utm_medium=email'

'''
What is "if __name__ == "__main__" for?
You have probably seen the code in the title at the end of many programs. 
If you still don't know what that code does, please watch the video. 
You will understand some inner working of Python as well.
'''

# http://127.0.0.1:5000

from flask import Flask, render_template, request

app = Flask(__name__)

def miles_to_km(miles):
    return miles * 1.60934

@app.route('/', methods=['GET', 'POST'])
def index():
    km = None
    if request.method == 'POST':
        miles = request.form.get('miles', type=float)
        if miles is not None:
            km = miles_to_km(miles)
    return render_template('index.html', km=km)


if __name__ == '__main__':
    app.run(debug=True)