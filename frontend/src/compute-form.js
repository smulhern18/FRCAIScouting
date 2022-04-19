import './App.css';
import React from 'react';

class ComputeForm extends React.Component {
  handleSubmit() {

  }
  
  render() {
    return (
        <div className="App">
            <header className="App-header">
                <label>Competition: </label>
                <input type='text' id='team'></input>
                <label>Team: </label>
                <input type='text' id='team'></input>
                <button type='submit'>Compute!</button>

                <label>Manual Entry: </label>
                <textarea id='manual-entry'></textarea>
                <button type='submit'>Compute!</button>

            </header>
        </div>
    );
  }
}

export default ComputeForm;
