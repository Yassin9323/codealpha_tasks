#!/usr/bin/python3
"""
starts a Url Shortener web application
"""
from flask import Flask, request, redirect, jsonify, render_template
import string
import random
from __init__ import storage
from core.models import URL

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """ rendering home page of project """
    return render_template('index.html')

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    short_code = ''.join(random.choice(characters) for _ in range(length))
    # short_code = f'http://127.0.0.1:5000/{short_code}'
    return (short_code)

@app.route('/shorten', methods=['POST'])
def shorten_url():
    # data = request.form.get_json()
    original_url = request.form.get('original_url')
    
    if not original_url:
        return jsonify({"error": "Original URL is required"}), 400
    
    original_url = original_url.strip()

    if not original_url.startswith(('http://', 'https://')):
        # Prepend https://www. if not present
        original_url = f'https://www.{original_url}'
        
    # Generate a short code
    short_code = generate_short_code()
    # Store the URL and short code in the database
    new_url = URL(original_url=original_url, short_code=short_code)
    storage.new(new_url)
    storage.save()
    
    # short_code = short_code[22:]
    return render_template('index.html', short_code=short_code)


@app.route('/<short_code>')
def redirect_to_url(short_code):
    # Query the database for the original URL
    # short_code = f"{short_code}"
    print(short_code)
    print(short_code)
    short_code = short_code.strip()
    url_entry = storage.get(URL, short_code)
    # link = url_entry.original_url
    # print(link)
    if url_entry:
        return redirect(url_entry.original_url)
    else:
        return jsonify({"error": "Short code not found"}), 404
    
    
if __name__ == "__main__":
    app.run()
