import './App.css';
import React from 'react';
import { SingleEliminationBracket, Match } from '@g-loot/react-tournament-brackets';

let coalitions = {
    "1": [
      "frc364", 
      "frc6443", 
      "frc1339"
    ], 
    "2": [
      "frc4911", 
      "frc1678", 
      "frc1785"
    ], 
    "3": [
      "frc2990", 
      "frc330", 
      "frc4561"
    ], 
    "4": [
      "frc118", 
      "frc3309", 
      "frc7419"
    ], 
    "5": [
      "frc7108", 
      "frc3132", 
      "frc7426"
    ], 
    "6": [
      "frc386", 
      "frc7179", 
      "frc4534"
    ], 
    "7": [
      "frc5892", 
      "frc2881", 
      "frc3931"
    ], 
    "8": [
      "frc2147", 
      "frc368", 
      "frc1261"
    ]
}

function computeMatch(round) {
    let firstRound = [[1, 8], [2, 7], [3, 6], [4, 5]]
    let secondRound = [[1, 7], [3, 4]]
    let thirdRound = [[1, 3]]
    let finaleWinner = 3
    let res = []
    firstRound.forEach((k, i) => {
        let nextMatch = secondRound[parseInt(i/2)]
        res.push({
            "id": `${k.join('')}-firstRound`,
            "tournamentRoundText": "1", // Text for Round Header
            "nextMatchId": nextMatch.join('') + '-secondRound', // Id for the nextMatch in the bracket, if it's final match it must be null OR undefined
            "participants": [
              {
                "id": k[0], // Unique identifier of any kind
                "isWinner": (round > 0) && (nextMatch.includes(k[0])),
                "name": coalitions[k[0]].join(', ')
              },
              {
                "id": k[1],
                "isWinner": (round > 0) && (nextMatch.includes(k[1])),
                "name": coalitions[k[1]].join(', ')
              }
            ]
        })
    })
    secondRound.forEach(k => {
        let participants = [
            {
              "id": k[0], // Unique identifier of any kind
              "isWinner": (round > 1) && (thirdRound[0].includes(k[0])),
              "name": coalitions[k[0]].join(', ')
            },
            {
              "id": k[1],
              "isWinner": (round > 1) && (thirdRound[0].includes(k[1])),
              "name": coalitions[k[1]].join(', ')
            }
        ]
        res.push({
            "id": k.join('') + '-secondRound',
            "nextMatchId": `${thirdRound[0].join('')}-thirdRound`, // Id for the nextMatch in the bracket, if it's final match it must be null OR undefined
            "participants": (round > 0) ? participants : []
        })
    })
    thirdRound.forEach(k => {
        let participants = [
            {
              "id": k[0], // Unique identifier of any kind
              "isWinner": (round > 2) && finaleWinner == k[0],
              "name": coalitions[k[0]].join(', ')
            },
            {
              "id": k[1],
              "isWinner": (round > 2) && finaleWinner == k[1],
              "name": coalitions[k[1]].join(', ')
            }
        ]
        res.push({
            "id": k.join('') + '-thirdRound',
            "participants": (round > 1) ? participants : []
        })
    })
    return res
}

class ComputeForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            data: null,
            error: null,
            round: 0
        }
    }

    componentDidMount() {
        // let url = 'https://raw.githubusercontent.com/Drarig29/brackets-viewer.js/master/demo/db.json'
        let url = 'http://localhost/compute/team/3538/competition/2019carv'
        fetch(url)
        .then(res => res.json())
        .then(coalitions => {
            console.log(coalitions)
            this.setState({ coalitions, error: null })
        })
        .catch(error => {
            this.setState({ error })
        })
    }

    nextRound() {
        this.setState({ round: (this.state.round + 1) % 4 })
    }

    render() {
        if (this.state.error !== null) return (<>{this.state.error.message}</>)
        if (this.state.coalitions === null) return (<>Loading...</>)
        return (
            <>
                <SingleEliminationBracket
                  matches={ computeMatch(this.state.round) }
                  matchComponent={Match}
                />
                <button onClick={this.nextRound.bind(this)}>Next Round</button>
            </>
        );
  }
}

export default ComputeForm;