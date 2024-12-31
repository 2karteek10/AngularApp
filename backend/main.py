from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

# Serve the Angular static files as the root
app.mount("/frontend", StaticFiles(directory="/app/frontend", html=True), name="frontend")

# Dynamically mount each subdirectory in /docs
DOCS_BASE_PATH = "/app/mkdocs"

# Dynamically mount the directories as soon as the app is created
projects = [
    project for project in os.listdir(DOCS_BASE_PATH)
    if os.path.isdir(os.path.join(DOCS_BASE_PATH, project))
]

if not projects:
    print(f"No projects found in {DOCS_BASE_PATH}.")
else:
    print(f"Found projects: {', '.join(projects)}")

for project in projects:
    project_path = os.path.join(DOCS_BASE_PATH, project)
    print(f"Mounting {project} from {project_path}...")
    app.mount(f"/mkdocs/{project}", StaticFiles(directory=project_path, html=True), name=f"docs-{project}")

@app.get("/api/health", response_class=HTMLResponse)
async def health_check():
    """Health check endpoint for the API."""
    return "API is running!"
