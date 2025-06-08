import os
import datetime
import json
from flask import Flask, render_template, request
import openai

app = Flask(__name__)

openai.api_key = os.environ.get('OPENAI_API_KEY')


def get_liturgical_year():
    year = datetime.datetime.now().year
    return ['A', 'B', 'C'][year % 3]


def fetch_passages(language):
    if not openai.api_key:
        # Placeholder result when no API key is provided
        return {
            'old_testament': 'Genesis 1:1-5',
            'new_testament': 'John 1:1-5',
            'commentary': 'In the beginning God created the heavens and the earth...'
        }

    prompt = f"""
    Select an Old Testament and a New Testament passage that correspond to the current liturgical year {get_liturgical_year()}. 
    Provide a short commentary explaining how they are related. Respond in {language}.
    Return your answer as JSON with keys old_testament, new_testament, commentary.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )
    # Attempt to parse JSON from the response
    try:
        text = response.choices[0].message['content']
        return json.loads(text)
    except Exception:
        return {
            'old_testament': 'Genesis 1:1-5',
            'new_testament': 'John 1:1-5',
            'commentary': text
        }


def detect_language():
    lang_header = request.headers.get('Accept-Language', 'en')
    return lang_header.split(',')[0].split('-')[0]


@app.route('/')
def index():
    lang = detect_language()
    passages = fetch_passages(lang)
    return render_template('index.html', passages=passages, lang=lang)


if __name__ == '__main__':
    app.run(debug=True)
