import React, {useState} from 'react';
import axios from 'axios';
import Loader from "../components/Loader";
import SuccessModal from "../components/SuccessModal";
import ErrorModal from "../components/ErrorModal";

const PublishMessageForm = ({apiUrl}) => {
    const [loading, setLoading] = useState(false);
    const [topicName, setTopicName] = useState('');
    const [messageContent, setMessageContent] = useState('');
    const [successMessage, setSuccessMessage] = useState('');
    const [errorMessage, setErrorMessage] = useState('');
    const [showSuccessModal, setShowSuccessModal] = useState(false);
    const [showErrorModal, setShowErrorModal] = useState(false);

    const handlePublishMessage = async (e) => {
        e.preventDefault();
        setLoading(true);
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
        } finally {
            setLoading(false);
        }
    };

    const closeModal = () => {
        setShowSuccessModal(false);
        setShowErrorModal(false);
    };

    return (
        <div className="container mt-4">
            <h2>Publish Message to Kafka</h2>
            <SuccessModal showModal={showSuccessModal} onClose={closeModal}/>
            <ErrorModal showModal={showErrorModal} onClose={closeModal}/>
            {!loading && <form onSubmit={handlePublishMessage}>
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
            </form>}
            {loading && <Loader/>}
        </div>
    );
};

export default PublishMessageForm;
