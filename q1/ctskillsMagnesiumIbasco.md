## Smart School Canteen Queue Annex A

**Name:** Sebastian Felix G. Ibasco

**Section:** 9 - Magnesium

**Last Name:** Ibasco

**Date:** August 18, 2026

## Step 1: Identify the Big Problem

### Main Problem

The school's canteen procedure is inefficient which causes long, slow moving lines that takes up a large portion of the canteen.

## Step 2: Identify the Sub-Problems

1. The cashier takes too long calculating the amount of change needed for each order.
2. The students take too long deciding what to order because there is no menu that displays what foods are available.
3. The cashiers have to manually check if the food that the students order is still available.
4. The employees serving the orders sometimes still have to ask what flavour of a certain drink or snack.

## Step 3: Define Computational Thinking Approaches
| Sub-Problem | CT Skill | Example Solution |
|---|---|---|
| Calculating Amount of change | Algorithms | Install computers with programs that will automatically calculate the change for the ordered items |
| Menu problem | Abstraction | Install a menu at the counter that students can easily read |
| Food Availability | Algorithm | Along with the program that calculates change, there will also be a program that tracks the stock of each item in the canteen |
| Flavour of drinks/snacks | Abstraction | Require the student to specify what flavour of that snack/drink before they can proceed with their order |

## Step 4: Algorithmic Solution

### Selected Sub Problem

Sub-Problem 1 - The cashier takes too long calculating the amount of change needed for each order.

### Pseudocode

START
    
    Show food menu with prices
    Take students order
    Calculate total price
    Show total price
    Collect students payment

    IF Students payment is less than total price
        Display Not enough money
    Else
        return change to student
        
END
