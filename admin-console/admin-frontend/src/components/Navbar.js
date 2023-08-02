import React from 'react';
import {Link} from 'react-router-dom';

const Navbar = () => {
    return (
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
            <div className="container">
                <Link className="navbar-brand" to="/publish-to-kafka">
                    Admin Console
                </Link>
                <button
                    className="navbar-toggler"
                    type="button"
                    data-toggle="collapse"
                    data-target="#navbarNav"
                    aria-controls="navbarNav"
                    aria-expanded="false"
                    aria-label="Toggle navigation"
                >
                    <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse" id="navbarNav">
                    <ul className="navbar-nav ml-auto">
                        <li className="nav-item">
                            <Link className="nav-link" to="/publish-to-kafka">
                                Publish
                            </Link>
                        </li>
                        <li className="nav-item">
                            <Link className="nav-link" to="/data-load">
                                Initial Data Load
                            </Link>
                        </li>
                        <li className="nav-item">
                            <Link className="nav-link" to="/load-kafka">
                                Load Kafka
                            </Link>
                        </li>
                        <li className="nav-item">
                            <Link className="nav-link" to="/load-mongo">
                                Load MongoDB
                            </Link>
                        </li>
                        <li className="nav-item">
                            <Link className="nav-link" to="/load-logs">
                                Load Log files
                            </Link>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    );
};

export default Navbar;
