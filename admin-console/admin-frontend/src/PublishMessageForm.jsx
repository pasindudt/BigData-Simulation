import React, { useState, useEffect } from 'react';
import axios from 'axios';

const PublishMessageForm = ({ apiUrl }) => {
    const [topicName, setTopicName] = useState('');
    const [message, setMessage] = useState('');
    const [successMessage, setSuccessMessage] = useState('');
    const [errorMessage, setErrorMessage] = useState('');
    const [topicList, setTopicList] = useState([]);

    console.log('inside publish message')

    useEffect(() => {
        // Fetch the list of topics when the component mounts
        fetchTopics();
    }, []);

    const fetchTopics = async () => {
        try {
            const response = await axios.get(`${apiUrl}/kafka/topics`);
            setTopicList(response.data.topics);
        } catch (error) {
            console.error('Error fetching topics:', error.message);
        }
    };

    const handlePublishMessage = async (e) => {
        e.preventDefault();
        if (topicName.trim() === '' || message.trim() === '') {
            setErrorMessage('Please enter both topic name and message content.');
            return;
        }

        try {
            const response = await axios.post(`${apiUrl}/kafka/publish`, {
                topicName,
                message,
            });
            setSuccessMessage('Message published successfully.');
            setErrorMessage('');
            console.log('Message published successfully:', response.data);
            setTopicName('');
            setMessage('');
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
                    {/* Render the topic name field as a drop-down */}
                    <select
                        className="form-control"
                        value={topicName}
                        onChange={(e) => setTopicName(e.target.value)}
                    >
                        <option value="">Select a topic</option>
                        {topicList.map((topic) => (
                            <option key={topic} value={topic}>
                                {topic}
                            </option>
                        ))}
                    </select>
                    <input
                        type="text"
                        className="form-control"
                        value={message}
                        onChange={(e) => setMessage(e.target.value)}
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
