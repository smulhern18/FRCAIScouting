import './App.css';
import React from 'react';
import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";
import ComputeForm from './compute-form'
import Bracket from './bracket'

class App extends React.Component {
  handleSubmit() {

  }
  
  render() {
    return (
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<ComputeForm />} />
          <Route path="/display" element={<Bracket />} />
        </Routes>
      </BrowserRouter>
    );
  }
}

export default App;
