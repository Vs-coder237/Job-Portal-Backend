from flask import Blueprint, render_template, request
from app.search import search_jobs 

main_routes = Blueprint('main', __name__)

@main_routes.route('/')
def home():
    return "<p>Welcome to the Job Portal</p>"

@main_routes.route('/search')
def search():
    query = request.args.get('q', '') 
    print(query)
    if query:
        results = search_jobs(query)
        return render_template('search_results.html', results=results, query=query)
    return render_template('search_results.html', results=[], query=query)
