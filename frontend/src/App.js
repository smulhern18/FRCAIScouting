import './App.css';
import React from 'react';
import {
  BrowserRouter,
  Route,
  Switch,
} from "react-router-dom";
import ComputeForm from './compute-form'
import Bracket from './bracket'

class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      coalitions: []
    }
  }

  handleSubmit(coalitions, team, competition) {
    this.setState({coalitions, team, competition})
  }

  render() {
    return (
      <BrowserRouter>
        <Switch>
          <Route exact path="/">
            {(Object.keys(this.state.coalitions).length > 0) ?
            <Bracket coalitions={this.state.coalitions} team={this.state.team} competition={this.state.competition}/> :
            <ComputeForm handleSubmit={this.handleSubmit.bind(this)}/>}
          </Route>
        </Switch>
      </BrowserRouter>
    );
  }
}

export default App;
