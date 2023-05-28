import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import "./App.css";
import React from "react";
import Main from "./Components/Main";
import Patient from "./Components/Patient";
import Diagnosis from "./Components/Diagnosis";
import Doctor from "./Components/Doctor";
import DocD from "./Components/DocD";

function App() {
  return (
    <>
      <div className="App App-header">
        <Router>
          <Routes>
            <Route exact path="/" element={<Main />} />
        
            <Route exact path="/patient" element={<Patient />} />
            <Route exact path="/Diagnosis" element={<Diagnosis />} />
            <Route exact path="/Doctor" element={<Doctor />} />
            <Route exact path="/DocD" element={<DocD/>} />

          </Routes>
        </Router>
      </div>
    </>
  );
}

export default App;
