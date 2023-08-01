import React from 'react';
import PublishMessageForm from "./PublishMessageForm";
import CreateTopicForm from "./CreateTopicForm";
import {BrowserRouter, Route, Routes} from 'react-router-dom';
import Layout from "./Layout";

const apiUrl = 'http://localhost:5000/api';

const App = () => {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/*" element={<Layout/>}>
                    <Route exact path="create-topic" render={() => <CreateTopicForm apiUrl={apiUrl}/>}/>
                    <Route exact path="publish-message" render={() => <PublishMessageForm apiUrl={apiUrl}/>}/>
                </Route>
            </Routes>
        </BrowserRouter>
    );
};

export default App;
