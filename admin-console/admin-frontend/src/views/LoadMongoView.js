import React, { useState } from 'react';
import axios from 'axios';
import ErrorModal from "../components/ErrorModal";
import SuccessModal from "../components/SuccessModal";
import Loader from "../components/Loader";

const LoadMongoView = ({ apiUrl }) => {
    const [numRecords, setNumRecords] = useState('');
    const [loading, setLoading] = useState(false);
    const [showSuccessModal, setShowSuccessModal] = useState(false);
    const [showErrorModal, setShowErrorModal] = useState(false);

    const handleLoadMongo = async () => {
        if (!numRecords) return;

        setLoading(true);

        try {
            const response = await axios.post(`${apiUrl}/load/mongo`, {
                numRecords: Number(numRecords),
            });
            console.log('MongoDB data loaded:', response.data);
            setShowSuccessModal(true);
        } catch (error) {
            console.error('Error loading MongoDB data:', error.message);
            setShowErrorModal(true);
        }

        setLoading(false);
    };

    const handleCloseSuccessModal = () => setShowSuccessModal(false);
    const handleCloseErrorModal = () => setShowErrorModal(false);

    return (
        <div>
            <h2>Load MongoDB Data</h2>
            <div className="input-group mb-3">
                <input
                    type="number"
                    className="form-control"
                    value={numRecords}
                    onChange={(e) => setNumRecords(e.target.value)}
                    placeholder="Enter number of records"
                />
                <button className="btn btn-primary" onClick={handleLoadMongo}>
                    Load MongoDB Data
                </button>
            </div>

            {loading && <Loader/>}

            <ErrorModal showModal={showErrorModal} onClose={handleCloseErrorModal}/>
            <SuccessModal showModal={showSuccessModal} onClose={handleCloseSuccessModal}/>

        </div>
    );
};

export default LoadMongoView;
