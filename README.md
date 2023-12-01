
FastAPI requires the installation of its prerequisite with the command 'pip install fastapi'
You will also need an ASGI server, for production such as Uvicorn or Hypercorn.
 'uvicorn' needs to be installed using the command 'pip install uvicorn.' In this repository, FastAPI is utilized for implementing GET, PUT, POST, and DELETE operations.

 To run the server:
 uvicorn main_1:app --host 0.0.0.0 --port 8000 --reload
