import React, {useState} from 'react';
import axios from 'axios';
import SuccessModal from "../components/SuccessModal";
import ErrorModal from "../components/ErrorModal";
import Loader from "../components/Loader";

const CreateTopicForm = ({apiUrl}) => {
    const [loading, setLoading] = useState(false);
    const [topicName, setTopicName] = useState('');
    const [successMessage, setSuccessMessage] = useState('');
    const [errorMessage, setErrorMessage] = useState('');
    const [showSuccessModal, setShowSuccessModal] = useState(false);
    const [showErrorModal, setShowErrorModal] = useState(false);

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

    const closeModal = () => {
        setShowSuccessModal(false);
        setShowErrorModal(false);
    };

    return (
        <div className="container mt-4">
            <h2 className="mb-3">Create Kafka Topic</h2>
            <SuccessModal showModal={showSuccessModal} onClose={closeModal}/>
            <ErrorModal showModal={showErrorModal} onClose={closeModal}/>
            {!loading && <form onSubmit={handleCreateTopic}>
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
            </form>}
            {loading && <Loader/>}
        </div>
    );
};

export default CreateTopicForm;
