import React from 'react';
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import InitialDataLoadComponent from "./views/InitialDataLoadComponent";
import PublishMessageForm from "./views/PublishMessageForm";
import Navbar from "./components/Navbar";
import KafkaDataLoader from "./views/KafkaDataLoader";
import LoadLogsView from "./views/LoadLogsView";
import LoadMongoView from "./views/LoadMongoView";

function App() {

    return (
        <div className="App">
            <Router>
                <div>
                    <Navbar/>
                    <div className="container mt-4">
                        <Routes>
                            <Route path="/" element={<PublishMessageForm apiUrl/>}/>
                            <Route path="/publish-to-kafka" element={<PublishMessageForm apiUrl/>}/>
                            <Route path="/data-load" element={<InitialDataLoadComponent apiUrl/>}/>
                            <Route path="/load-kafka" element={<KafkaDataLoader apiUrl/>}/>
                            <Route path="/load-logs" element={<LoadLogsView apiUrl />} />
                            <Route path="/load-mongo" element={<LoadMongoView apiUrl />} />
                        </Routes>
                    </div>
                </div>
            </Router>
        </div>
    );
}

export default App;