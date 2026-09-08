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

### Which method changes the state of your object?

### How did your two objects demonstrate that instances are independent?

### What is the difference between your class diagram and your object diagram?
