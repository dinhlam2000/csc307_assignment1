import React, {useState, useEffect} from 'react';
import Table from './Table';
import Form from './Form';
import axios from 'axios';




function MyApp() {
    const [characters, setCharacters] = useState([]);

    useEffect(() => {
        fetchAll().then(result => {
            if (result)
                setCharacters(result);
        });
    }, [] );

    return (
        <div className="container">
            <Table characterData={characters} removeCharacter={removeOneCharacter} />
            <Form handleSubmit={updateList} />
        </div>
    )


    async function makePostCall(person){
        try {
            const response = await axios.post('http://localhost:5000/users', person);
            return response;
        }
        catch (error) {
            console.log(error);
            return false;
        }
    }

    async function makeDeleteCall(person){
        try {
            const person_id = person.id;
            const url = 'http://localhost:5000/users/' + String(person_id)
            const response = await axios.delete(url);
            return response;
        }
        catch (error) {
            console.log(error);
            return false;
        }
    }

    function removeOneCharacter (person) {
        makeDeleteCall(person).then(result => {
            if (result.status === 204) {
                fetchAll().then(result => {
                    if (result)
                        setCharacters(result);
                });
            }
        })
    }

    function updateList(person) {
        makePostCall(person).then( result => {
            if (result.status === 201)
            {
                setCharacters(result.data.users_list );

            }
        });
    }


    async function fetchAll(){
        try {
            const response = await axios.get('http://localhost:5000/users');
            return response.data.users_list;
        }
        catch (error){
            //We're not handling errors. Just logging into the console.
            console.log(error);
            return false;
        }
    }





}
export default MyApp;
