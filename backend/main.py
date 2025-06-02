from fastapi import FastAPI
from routes import auth, system_users, students, roles
from models import init_db

app = FastAPI(title="LMS Backend", version="1.0")

# Initialize database tables upon startup
@app.on_event("startup")
def on_startup():
    init_db()

# Include routers
app.include_router(auth.router)
app.include_router(system_users.router)
app.include_router(students.router)
app.include_router(roles.router)

# Global error handler (can be extended for logging)
from fastapi.responses import JSONResponse
from fastapi.requests import Request

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"detail": "An error occurred."})
