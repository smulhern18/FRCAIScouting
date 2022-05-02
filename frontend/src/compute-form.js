import './App.css';
import React from 'react';

class ComputeForm extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      team: '3538',
      competition: '2019carv',
      manualEntry: ''
    }
    console.log(props)
  }

  handleSubmitAuto() {
    console.log('Submitted!', this.state)
    let url = `http://localhost/compute/team/${this.state.team}/competition/${this.state.competition}`
    fetch(url)
    .then(res => res.json())
    .then(coalitions => {
        this.props.handleSubmit(coalitions)
    })
    .catch(error => {
        this.setState({ error })
    })           
  }

  handleSubmitManual() {
    this.props.handleSubmit(JSON.parse(this.state.manualEntry))
  }

  handleChangeCompetition(e) {
    this.setState({competition: e.target.value})
  }

  handleChangeTeam(e) {
    this.setState({team: e.target.value})
  }

  handleChangeManualEntry(e) {
    this.setState({manualEntry: e.target.value})
  }
  
  render() {
    console.log(this.state)
    return (
        <div className="App">
            <header className="App-header">
            <div className="row">
              <div className="column">
                <div>
                  <label>Competition: </label>
                  <input type='text' id='competition' value={this.state.competition} onChange={this.handleChangeCompetition.bind(this)}/>
                  <label>Team: </label>
                  <input type='text' id='team' value={this.state.team} onChange={this.handleChangeTeam.bind(this)}/>
                </div>
                <div>
                  <button type='submit' onClick={this.handleSubmitAuto.bind(this)}>Compute!</button>
                </div>
              </div>
              <div className="column"/>
                <div>
                  <label>Manual Entry: </label>
                  <textarea id='manual-entry' onChange={this.handleChangeManualEntry.bind(this)} value={this.state.manualEntry}/>
                </div>
                <div>
                <button type='submit' onClick={this.handleSubmitManual.bind(this)}>Compute!</button>
                </div>
              </div>
            </header>
        </div>
    );
  }
}

export default ComputeForm;
