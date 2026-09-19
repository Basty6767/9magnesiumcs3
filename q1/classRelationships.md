# Class Relationships: Association and Multiplicity

## Previous Work
[Part I - Classes and Objects](classObjectUML.md)
[Part II - Class Attributes and Methods](classAttributesMethods.md)

## Existing Class
Class: VNL Teams

Description: The international Volleyball teams of 18 different countries that compete in annual indoor Volleyball matches.

## New Related Class
Class: Coaches

Description: The people that strategize and call different kinds of plays during matches. Each team is only allowed to have 3 coaches on the bench during matches.

## Association
Relationship: HAS-A Relationship (Coaches manage VNL Teams)

Explanation: A VNL Team HAS-A Coaching staff that manages its strategies play calls during matches. This connects individual Coach objects to a specific VNL Team object so they can interact as a connected system.

## Multiplicity
Multiplicity: Coaches 1..* ───────── 1 VNL Team (Many-to-One)

Explanation: I think this relationship is appropriate for my system because in general, a VNL coach can only be on one team at a time. However, VNL Teams can have up to 3 coaches on the bench for each match.

## UML Class Relationship Diagram
![Class Relationship Diagram](Images/classRelationshipDiagram.png)

## Python Implementation
[View Python Source](classRelationships.py)

## Test Run
![Relationship Test Run](Images/relationshipTestRun.png)

## Object Relationship Diagram
![Object Relationship Diagram](Images/objectRelationshipDiagram.png)

## Analysis

### 1. What is the association between your two classes?

### 2. What multiplicity did you choose and why?

### 3. How did you implement the relationship in Python?

### 4. Why did you store an object reference instead of copying its data?

### 5. If your relationship uses many, why is a list appropriate?
