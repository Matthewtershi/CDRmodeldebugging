import React, { useState, useEffect } from 'react'
import api from "../api"
import Note from "../components/Note"
import Form from "../components/Form"

const Home = () => {
    const [notes, setNotes] = useState([])
    const [content, setContent] = useState("")
    const [title, setTitle] = useState("")

    useEffect(() => {
        getNotes();
    }, [])

    const getNotes = () => {
        api.get("/api/notes/")
        .then((res) => res.data)
        .then((data) => { setNotes(data); console.log(data) })
        .catch((err) => alert(err))
        // from backend-backend-urls to backend-api-urls because 
        // anything /api that isnt in backend-backend-urls gets forwarded to backend-api-urls
    };

    const deleteNote = (id) => {
        api.delete(`/api/notes/delete/${id}/`)
        .then((res) => {
            if (res.status === 204) alert("Note was deleted!")
            else alert("Failed to delete note!")
            getNotes();
        }).catch((error) => alert(error))
        // this call is just to update after deleteNote is called
    };

    const createNote = (e) => {
        e.preventDefault()
        api.post("/api/notes/", {content, title})
        .then((res) => {
            if (res.status === 201) alert("Note created!")
            else alert("Failed to make note!")
            getNotes();
        }).catch((error) => alert(error))
    }

    return (
        <div>
            <div>
                <h2> Notes </h2>
                {notes.map((note) => (
                    <Note note={note} onDelete={deleteNote} key={note.id} />
                ))}
            </div>

            <h2> Create a Note </h2>
            <Form onSubmit={createNote}>
                <label htmlFor="title"> Title: </label>
                <br/>
                <input 
                    type="text" 
                    id="title" 
                    name="title"
                    required
                    onChange={(e) => setTitle(e.target.value)}
                    value = {title}
                />
                <br/>

                <label htmlFor="content"> Content: </label>
                <br/>
                <textarea 
                    id="content" 
                    name="content" 
                    required 
                    value={content} 
                    onChange={(e) => setContent(e.target.value)}
                ></textarea>
                <br/>
                <input type="submit" value="Submit"></input>
            </Form>
        </div>

    )
}

export default Home