import './App.css';
import React from 'react';
import { SingleEliminationBracket, Match } from '@g-loot/react-tournament-brackets';

function coalitionsToID(targetCoalitions, allCoalitions) {
	let res = []
	for (let coalition of targetCoalitions) {
		res.push(parseInt(Object.keys(allCoalitions).find(key => allCoalitions[key].join('-') === coalition.join('-'))))
	}
	return res
}

function computeMatch(round, coalitions, winners) {
	let qfWinners = coalitionsToID(winners['qf'], coalitions)
	let sfWinners = coalitionsToID(winners['sf'], coalitions)
	let finaleWinner = coalitionsToID([winners['f']], coalitions)[0]

	let firstRound = [[1, 8], [2, 7], [3, 6], [4, 5]]
	let secondRound = firstRound.map((k, i) => {
		for (let j of qfWinners) {
			if (k.includes(j)) {
				return j
			}
		}
		return NaN
	})	
	secondRound = [[secondRound[0], secondRound[1]], [secondRound[2], secondRound[3]]]
	let thirdRound = secondRound.map((k, i) => {
		for (let j of sfWinners) {
			if (k.includes(j)) {
				return j
			}
		}
	})	
	thirdRound = [thirdRound]


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
              "isWinner": (round > 2) && finaleWinner === k[0],
              "name": coalitions[k[0]].join(', ')
            },
            {
              "id": k[1],
              "isWinner": (round > 2) && finaleWinner === k[1],
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
            round: 0,
            winners: null
        }
    }

    nextRound() {
        this.setState({ round: (this.state.round + 1) % 4 })
    }

    componentDidMount() {
		let url = `http://localhost/won_lost/event/${this.props.competition}`
		fetch(url, {
			method: 'POST',
			headers: {
			'Content-Type': 'application/json',
			'Alliances': JSON.stringify(this.props.coalitions)
			}
		})
		.then(res => res.json())
		.then(winners => {
			this.setState({winners})
		})
		.catch(error => {
			console.log(error)
		})
    }

    render() {
		if (this.state.winners === null) {
			return (<></>)
		}
		console.log(this.state.winners)
		let qfMatches = this.state.winners['qf'].map(m => <p>{m.join(', ')}</p>)
		let qfProbs = this.state.winners['qf_probs'].map(m => <p>{Math.max(...m)}</p>)
		let sfMatches = this.state.winners['sf'].map(m => <p>{m.join(', ')}</p>)
		let sfProbs = this.state.winners['sf_probs'].map(m => <p>{Math.max(...m)}</p>)
		let fMatch =  <p>{this.state.winners['f'].join(', ')}</p>
		let fProbs = <p>{Math.max(...this.state.winners['f_probs'])}</p>
        return (
            <>
				<h1>Optimization and winner prediction for event {this.props.competition}</h1>

                <SingleEliminationBracket
                  matches={ computeMatch(this.state.round, this.props.coalitions, this.state.winners) }
                  matchComponent={Match}
                />
				<button onClick={this.nextRound.bind(this)}>Next Round</button>
				<h4>Raw model outputs</h4>
				<table>
					<tbody>
						<tr>
							<td>QF Matches Winners</td>
							<td>SF Matches Winners</td>
							<td>Final Match Winners</td>
							<td>QF Matches Win Confidence</td>
							<td>SF Matches Win Confidence</td>
							<td>Final Matches Win Confidence</td>
						</tr>
						<tr>
							<td>{qfMatches}</td>
							<td>{sfMatches}</td>
							<td>{fMatch}</td>
							<td>{qfProbs}</td>
							<td>{sfProbs}</td>
							<td>{fProbs}</td>
						</tr>
					</tbody>
				</table>
            </>
        );
  }
}

export default ComputeForm;