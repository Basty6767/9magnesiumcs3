# SG4 - Understanding Classes and Objects
## Class Name: VNL Teams

## Class Description: The international Volleyball teams of 18 different countries that compete in annual indoor Volleyball matches.

## Properties
| Property | Data Type | Description |
|---|---|---|
| Players | Integer | Number of players in a team |
| Country | String | The country that team represents |
| Ranking | Integer | Current ranking in the league |
| NumofWins | Integer | Current of number of wins |
## Methods
| Method | Description |
|---|---|
| serve | The team does a serve to start a rally |
| block(opponentSpike: string) | The team tries to block the spike of the opposing team |
| subPlayer(Name: string) | Swaps a player on the court with a player on the bench |

## Class Diagram

+------------------------------------------+

| VNL Teams |

+------------------------------------------+

| Players : Integer |
| Country : String |
| Ranking : Integer |
| Wins : Integer |

+------------------------------------------+

| serve() |
| block(opponentSpike : String) |
| subPlayer(Name: string) |

+------------------------------------------+

## Design Explanation

### Why did you choose this class?
     - I chose VNL Teams because I am a big fan of the sport volleyball and I play it nearly everyday on the court near dorm 1. I also enjoy watching matches of the international level players because of the long, intense rallies they have.

### Which property is the most important? Why?
    - For me, I think the ranking is the most important because it reflects on the teams performance in the league. It also determines whether the team is qualified for the quarterfinals and finals.

### Which method is the most useful? Why?
    - I think the subPlayer method is the most important because if used correctly, coaches can create several different strategies based on the players that they put onto the court. It is also essential for players to be subbed out during matches in order for them to rest and not be exhausted after just 1 set.
