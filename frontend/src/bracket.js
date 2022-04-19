import './App.css';
import React from 'react';

class ComputeForm extends React.Component {
    render() {
        let url = 'https://raw.githubusercontent.com/Drarig29/brackets-viewer.js/master/demo/db.json'
        // url = 'http://localhost/compute/team/3538/competition/2019carv'
        const data = fetch(url).then(res => res.json());

        window.bracketsViewer.render({
            stages: data.stage,
            matches: data.match,
            matchGames: data.match_game,
            participants: data.participant,
        });
    
        return (
            <div className="App">
                <div className="brackets-viewer"></div>
            </div>
        );
  }
}

export default ComputeForm;
