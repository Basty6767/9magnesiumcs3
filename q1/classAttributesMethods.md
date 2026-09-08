# Class Attributes and Methods

## Previous Design
Link to my previous activity:
[classObjectUML.md](classObjectUML.md)

## Design Revision
No major changes were needed from my original design.

## Visibility Decisions
| Attribute | Data Type | Visibility | Reason |
|---|---|---|---|
| Players | Integer | Private | Protects data so nobody accidentally changes the number of players in a team |
| Country | String | Public | Anyone can view what country each team represents |
| Ranking | Integer | Public | Anyone can view each team's current rank |
| NumofWins | Integer | Private | Protects the data so external code cannot cheat and fake the win count |

## Updated UML Class Diagram
![Class Diagram](images/classDiagramSG5.png)

## Python Implementation
[View Python Source](classImplementation.py)

## Test Run
![Test Run](images/classTestRun.png)

## Object Diagram
![Object Diagram](images/objectDiagram.png)

## Analysis

### Why did you make your chosen attribute private?
    I made the players and numofwins attributes private to protect their values from being changed directly. Instead, I used methods like subPlayer() and addwin() to safely change them. This helps control how the values are updated in the program.
### Which method changes the state of your object?
    The subPlayer() method changes the state of my object by decreasing the number of players by 1. For example, team1 started with 12 players, and after using subPlayer(), it had 11 players. The addwin() method also changes the state by increasing team1's wins from 8 to 9.
### How did your two objects demonstrate that instances are independent?
    My 2 objects, team1 and team2, were created from the same class but had different values. I only performed actions on team1, so its players changed from 12 to 11 and its wins changed from 8 to 9. team2 stayed at 12 players and 20 wins showing that the objects are independent.
### What is the difference between your class diagram and your object diagram?
    The class diagram shows the blueprint of the VNLTeams class, including its attributes and methods. The object diagram shows the actual objects created from the class and their current values. In my object diagram, team1 and team 2 show their specific values after the actions were performed.