from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine, Base
from app.routers import users

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI PostgreSQL API",
    description="API with FastAPI and PostgreSQL",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Include routers
app.include_router(users.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI PostgreSQL API"}
