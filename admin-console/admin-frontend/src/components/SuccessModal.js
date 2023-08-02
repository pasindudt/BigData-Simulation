import React from 'react';

const SuccessModal = ({ showModal, onClose }) => {
    return (
        <div className={`modal fade ${showModal ? 'show' : ''}`} style={{ display: showModal ? 'block' : 'none' }}>
            <div className="modal-dialog">
                <div className="modal-content">
                    <div className="modal-body">
                        Data loaded successfully!
                    </div>
                    <div className="modal-footer">
                        <button type="button" className="btn btn-primary" onClick={onClose}>Close</button>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default SuccessModal;
