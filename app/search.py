from app.models import Job

def search_jobs(query):
    search = f"%{query}%"
    results = Job.query.filter(
        Job.title.ilike(search) | 
        Job.description.ilike(search) |
        Job.location.ilike(search) |
        Job.company.ilike(search)
    ).all()
    return results
