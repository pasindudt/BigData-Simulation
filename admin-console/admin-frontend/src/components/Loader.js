import React from 'react';

const Loader = () => {
    return (
        <div className="d-flex justify-content-center mt-4">
            <span className="sr-only">Loading...</span>
            <div className="spinner-border" role="status"/>
        </div>
    );
};

export default Loader;
