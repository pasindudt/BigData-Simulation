import React, { useState } from 'react';
import axios from 'axios';
import Loader from "../components/Loader";
import ErrorModal from "../components/ErrorModal";
import SuccessModal from "../components/SuccessModal";

const LoadLogsView = ({ apiUrl }) => {
    const [numRecords, setNumRecords] = useState('');
    const [loading, setLoading] = useState(false);
    const [showSuccessModal, setShowSuccessModal] = useState(false);
    const [showErrorModal, setShowErrorModal] = useState(false);

    const handleLoadLogs = async () => {
        if (!numRecords) return;

        setLoading(true);

        try {
            const response = await axios.post(`${apiUrl}/load/logs`, {
                numRecords: Number(numRecords),
            });
            console.log('Logs loaded:', response.data);
            setShowSuccessModal(true);
        } catch (error) {
            console.error('Error loading logs:', error.message);
            setShowErrorModal(true);
        }

        setLoading(false);
    };

    const handleCloseSuccessModal = () => setShowSuccessModal(false);
    const handleCloseErrorModal = () => setShowErrorModal(false);

    return (
        <div>
            <h2>Load Logs</h2>
            <div className="input-group mb-3">
                <input
                    type="number"
                    className="form-control"
                    value={numRecords}
                    onChange={(e) => setNumRecords(e.target.value)}
                    placeholder="Enter number of records"
                />
                <button className="btn btn-primary" onClick={handleLoadLogs}>
                    Load Logs
                </button>
            </div>

            {loading && <Loader/>}

            <ErrorModal showModal={showErrorModal} onClose={handleCloseErrorModal}/>
            <SuccessModal showModal={showSuccessModal} onClose={handleCloseSuccessModal}/>
        </div>
    );
};

export default LoadLogsView;
