import React from 'react';
import CreateTopicForm from './CreateTopicForm';
import PublishMessageForm from './PublishMessageForm';

const apiUrl = 'http://localhost:5000';

const App = () => {
    return (
        <div>
            <CreateTopicForm apiUrl={apiUrl} />
            <PublishMessageForm apiUrl={apiUrl} />
        </div>
    );
};

export default App;
