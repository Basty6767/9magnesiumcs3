# OOP Concept
**Name:** Sebastian Felix G. Ibasco

**Section:** 9 - Magnesium

**Last Name:** Ibasco

**Date:** August 20, 2026

# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

### 1. Encapsulation
    Encapsulation means grouping a products's data, like price and quantity, inside a single Product object. In Python, we can prefix variables with underscores to show they are private and should not be changed directly. Instead, we use methods like reduce_stock() to update the numbers safely, which stops bugs like inventory dropping below zero

### 2. Abstraction
    Abstraction hides the complicated background code so the store owner only sees what they need. For example, the owner just calls a simple Python method named sell_item(). They do not need to see the complex math or file-saving code running behind the scenes to update the shop's total sales.

### 3. Inheritance
    Inheritance lets us create a main Product class for basic items, and the reuse its code for special items. A Python subclass like PerishableItem(Product) automatically gets name and price from the main class, but lets us add a new expiry_date attribute. This saves time because we do not have to copy paste the same code for every new item type.

### 4. Polymorphism
    Polymorphism lets us use one single command to handle different types of items differently. We can create a method called get_final_price(). A regular item will return the normal price, but a bulk item can automatically apply a discount using that exact same method name, removing the need for messy if-else rules when looping through our inventory.

## Reflection
    Encapsulation is the most useful pillar for a sari-sari store system. In a small shop, keeping track of exact stock numbers and prices is the most important task. If any part of the program could change the inventory variables without rules, it would be easy to accidentally get negative stock or wrong pieces. Encapsulation locks this data up and keeps the store records safe and accurate.

