import './App.css';
import React from 'react';

class ComputeForm extends React.Component {
  handleSubmit() {

  }
  
  render() {
    return (
        <div className="App">
            <header className="App-header">
            <div class="row">
              <div class="column">
                <div>
                  <label>Competition: </label>
                  <input type='text' id='team'></input>
                  <label>Team: </label>
                  <input type='text' id='team'></input>
                </div>
                <div>
                  <button type='submit'>Compute!</button>
                </div>
              </div>
              <div class="column"></div>
                <div>
                  <label>Manual Entry: </label>
                  <textarea id='manual-entry'></textarea>
                </div>
                <div>
                  <button type='submit'>Compute!</button>
                </div>
              </div>
            </header>
        </div>
    );
  }
}

export default ComputeForm;
