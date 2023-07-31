import React, { useState } from 'react';
import axios from 'axios';

const PublishMessageForm = ({ apiUrl }) => {
    const [topicName, setTopicName] = useState('');
    const [messageContent, setMessageContent] = useState('');
    const [successMessage, setSuccessMessage] = useState('');
    const [errorMessage, setErrorMessage] = useState('');

    const handlePublishMessage = async (e) => {
        e.preventDefault();
        if (topicName.trim() === '' || messageContent.trim() === '') {
            setErrorMessage('Please enter both topic name and message content.');
            return;
        }

        try {
            const response = await axios.post(`${apiUrl}/kafka/publish`, {
                topicName,
                messageContent,
            });
            setSuccessMessage('Message published successfully.');
            setErrorMessage('');
            console.log('Message published successfully:', response.data);
            setTopicName('');
            setMessageContent('');
        } catch (error) {
            setErrorMessage('Error publishing message. Please try again.');
            setSuccessMessage('');
            console.error('Error publishing message:', error.message);
        }
    };

    const hideMessages = () => {
        setSuccessMessage('');
        setErrorMessage('');
    };

    return (
        <div className="container mt-4">
            <h2>Publish Message to Kafka</h2>
            <form onSubmit={handlePublishMessage}>
                <div className="input-group mb-3">
                    <input
                        type="text"
                        className="form-control"
                        value={topicName}
                        onChange={(e) => setTopicName(e.target.value)}
                        placeholder="Enter topic name"
                    />
                    <input
                        type="text"
                        className="form-control"
                        value={messageContent}
                        onChange={(e) => setMessageContent(e.target.value)}
                        placeholder="Enter message content"
                    />
                    <button type="submit" className="btn btn-primary">Publish Message</button>
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

export default PublishMessageForm;
