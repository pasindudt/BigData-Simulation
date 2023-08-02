import React, {useState} from 'react';
import axios from 'axios';
import ErrorModal from "../components/ErrorModal";
import SuccessModal from "../components/SuccessModal";

const DataLoadComponent = ({apiUrl}) => {
    const [showSuccessModal, setShowSuccessModal] = useState(false);
    const [showErrorModal, setShowErrorModal] = useState(false);

    const handleLoadKafkaMessages = async () => {
        try {
            const response = await axios.post(`${apiUrl}/load/kafka`);
            setShowSuccessModal(true);
            console.log('Kafka messages loaded:', response.data);
        } catch (error) {
            setShowErrorModal(true);
            console.error('Error loading Kafka messages:', error.message);
        }
    };

    const handleLoadMongoDBData = async () => {
        try {
            const response = await axios.post(`${apiUrl}/load/mongodb`);
            setShowSuccessModal(true);
            console.log('MongoDB data loaded:', response.data);
        } catch (error) {
            setShowErrorModal(true);
            console.error('Error loading MongoDB data:', error.message);
        }
    };

    const handleLoadLogFiles = async () => {
        try {
            const response = await axios.post(`${apiUrl}/load/logfiles`);
            setShowSuccessModal(true);
            console.log('Log files loaded:', response.data);
        } catch (error) {
            setShowErrorModal(true);
            console.error('Error loading log files:', error.message);
        }
    };

    const closeModal = () => {
        setShowSuccessModal(false);
        setShowErrorModal(false);
    };

    return (
        <div className="container mt-4">
            <h2>Data Load Options</h2>
            <SuccessModal showModal={showSuccessModal} onClose={closeModal}/>
            <ErrorModal showModal={showErrorModal} onClose={closeModal}/>
            <div className="d-flex flex-column align-items-center">
                <button className="btn btn-primary btn-lg mb-3" onClick={handleLoadKafkaMessages}>
                    Load Kafka Messages
                </button>
                <button className="btn btn-success btn-lg mb-3" onClick={handleLoadMongoDBData}>
                    Load MongoDB Data
                </button>
                <button className="btn btn-info btn-lg mb-3" onClick={handleLoadLogFiles}>
                    Load Log Files
                </button>
            </div>
        </div>
    );
};

export default DataLoadComponent;
