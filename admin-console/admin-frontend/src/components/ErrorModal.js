import React from 'react';

const ErrorModal = ({ showModal, onClose }) => {
    return (
        <div className={`modal fade ${showModal ? 'show' : ''}`} style={{ display: showModal ? 'block' : 'none' }}>
            <div className="modal-dialog">
                <div className="modal-content">
                    <div className="modal-body">
                        Error loading data. Please try again.
                    </div>
                    <div className="modal-footer">
                        <button type="button" className="btn btn-primary" onClick={onClose}>Close</button>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default ErrorModal;
