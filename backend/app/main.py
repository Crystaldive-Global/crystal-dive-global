from fastapi import FastAPI
from http://fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Crystaldive Global")

http://app.add_middleware(
    CORSMiddleware,
    allow_origins=["_"],
    allow_credentials=True,
    allow_methods=["_"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Crystaldive Global API is running"}

@app.get("/health")
def health():
    return {"status": "ok", "app": "Crystaldive Global"}

---

First line: from fastapi import FastAPI
Last line: return {"status": "ok", "app": "Crystaldive Global"}
