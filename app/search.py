from app import db

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)

def search_jobs(query):
    # Perform a search in the jobs database
    results = Job.query.filter(Job.title.ilike(f'%{query}%')).all()
    return results
