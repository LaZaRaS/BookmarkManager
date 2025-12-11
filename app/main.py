from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from . import models, schemas
from .database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Bookmark Manager")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Bookmark Manager API"}

@app.post("/bookmarks", response_model=schemas.BookmarkResponse)
def create_bookmark(bookmark: schemas.BookmarkCreate, db: Session = Depends(get_db)):
    db_bookmark = models.Bookmark(**bookmark.model_dump())
    db.add(db_bookmark)
    db.commit()
    db.refresh(db_bookmark)
    return db_bookmark

@app.get("/bookmarks", response_model=List[schemas.BookmarkResponse])
def list_bookmarks(db: Session = Depends(get_db)):
    bookmarks = db.query(models.Bookmark).all()
    return bookmarks

@app.get("/bookmarks/{bookmark_id}", response_model=schemas.BookmarkResponse)
def get_bookmark(bookmark_id: int, db: Session = Depends(get_db)):
    bookmark = db.query(models.Bookmark).filter(models.Bookmark.id == bookmark_id).first()
    if not bookmark:
        raise HTTPException(status_code=404, detail="Bookmark not found")
    return bookmark

@app.delete("/bookmarks/{bookmark_id}")
def delete_bookmark(bookmark_id: int, db: Session = Depends(get_db)):
    bookmark = db.query(models.Bookmark).filter(models.Bookmark.id == bookmark_id).first()
    if not bookmark:
        raise HTTPException(status_code=404, detail="Bookmark not found")
    db.delete(bookmark)
    db.commit()
    return {"message": "Bookmark deleted"}