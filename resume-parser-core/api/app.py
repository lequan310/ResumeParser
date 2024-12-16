from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes.files import router as files_router

# Create the FastAPI app
app = FastAPI(title="Resume Parser API", version="0.1.0")

# Include the routers
app.include_router(files_router)


@app.get("/")
def read_root():
    return {"message": "Welcome to Resume Parser API!"}


# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
