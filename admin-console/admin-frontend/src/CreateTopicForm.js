import React, { useState } from 'react';
import axios from 'axios';

const CreateTopicForm = ({ apiUrl }) => {
    const [topicName, setTopicName] = useState('');
    const [successMessage, setSuccessMessage] = useState('');
    const [errorMessage, setErrorMessage] = useState('');

    const handleCreateTopic = async (e) => {
        e.preventDefault();
        if (topicName.trim() === '') {
            setErrorMessage('Please enter a topic name.');
            return;
        }

        try {
            const response = await axios.post(`${apiUrl}/kafka/topics?topicName=${topicName}&numPartitions=${1}&replicationFactor=${1}`);
            setSuccessMessage(`Topic "${topicName}" created successfully.`);
            setErrorMessage('');
            setTopicName('');
            console.log('Topic created successfully:', response.data);
        } catch (error) {
            setErrorMessage('Error creating topic. Please try again.');
            setSuccessMessage('');
            console.error('Error creating topic:', error.message);
        }
    };

    const hideMessages = () => {
        setSuccessMessage('');
        setErrorMessage('');
    };

    return (
        <div className="container mt-4">
            <h2 className="mb-3">Create Kafka Topic</h2>
            <form onSubmit={handleCreateTopic}>
                <div className="input-group mb-3">
                    <input
                        type="text"
                        className="form-control"
                        value={topicName}
                        onChange={(e) => setTopicName(e.target.value)}
                        placeholder="Enter topic name"
                    />
                    <button type="submit" className="btn btn-primary">Create Topic</button>
                </div>
                {successMessage && (
                    <div className="alert alert-success mt-3" onClick={hideMessages}>
                        {successMessage}
                    </div>
                )}
                {errorMessage && (
                    <div className="alert alert-danger mt-3" onClick={hideMessages}>
                        {errorMessage}
                    </div>
                )}
            </form>
        </div>
    );
};

export default CreateTopicForm;
