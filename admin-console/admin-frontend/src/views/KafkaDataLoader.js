import React, { useState } from 'react';
import axios from 'axios';
import Loader from "../components/Loader";
import SuccessModal from "../components/SuccessModal";
import ErrorModal from "../components/ErrorModal";


const KafkaDataLoader = ({ apiUrl }) => {
    const [numRecords, setNumRecords] = useState('');
    const [loading, setLoading] = useState(false);
    const [successMessage, setSuccessMessage] = useState('');
    const [errorMessage, setErrorMessage] = useState('');
    const [showSuccessModal, setShowSuccessModal] = useState(false);
    const [showErrorModal, setShowErrorModal] = useState(false);

    const handleLoadKafkaData = async () => {
        setLoading(true);
        setSuccessMessage('');
        setErrorMessage('');

        try {
            const response = await axios.post(`${apiUrl}/load/kafka`, {
                numRecords: Number(numRecords),
            });
            console.log('Kafka data loaded:', response.data);
            setLoading(false);
            setSuccessMessage('Kafka data loaded successfully.');
        } catch (error) {
            setLoading(false);
            setErrorMessage('Error loading Kafka data. Please try again.');
            console.error('Error loading Kafka data:', error.message);
        }
    };

    const closeModal = () => {
        setShowSuccessModal(false);
        setShowErrorModal(false);
    };

    return (
        <div>
            <h2>Load Kafka Data</h2>
            <div className="input-group mb-3">
                <input
                    type="number"
                    className="form-control"
                    value={numRecords}
                    onChange={(e) => setNumRecords(e.target.value)}
                    placeholder="Enter number of records"
                />
                <button className="btn btn-primary" onClick={handleLoadKafkaData}>
                    Load Kafka Data
                </button>
            </div>
            {/* Loader */}
            {loading && <Loader />}

            {/* Success Modal */}
            {successMessage && (
                <SuccessModal message={successMessage} onClose={closeModal} />
            )}

            {/* Error Modal */}
            {errorMessage && (
                <ErrorModal message={errorMessage} onClose={closeModal} />
            )}
        </div>
    );
};

export default KafkaDataLoader;
