from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

notes ={}

class Note(BaseModel):
    title: str
    content: str


@app.get("/")
def root():
    return {"message": "Notes API running!"}


@app.post("/create_note")
def create_note(note: Note):
    note_id = len(notes) +1
    notes[note_id] = note
    return {"message": "Note created successfully!", "id": note_id, "note": note}

@app.get("/get_note/{note_id}")
def get_note(note_id:int):
    if note_id not in notes:
        return {"message": "Note not found!"}
    return {"note": notes[note_id]}

