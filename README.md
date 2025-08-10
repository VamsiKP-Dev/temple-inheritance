# Temple Inheritance in Python
This project demonstrates how object-oriented programming (OOP) works in Python using the concept of temple structures. 
It uses **class inheritance**, **method overriding**, and **real-world modeling** to simulate the properties of a famous temple and a village temple.

## 1. Understanding Inheritance and Method Overriding in Python

### Inheritance

Inheritance is a feature in Python where a class (called a child or subclass) can inherit attributes and methods from another class (called a parent or superclass). 
This promotes code reuse and makes it easier to build complex systems based on simpler components.

#### Example from the code:

class FamousTemple:
    temple = "Tirumala"

* The VillageTemple class inherits from FamousTemple:

class VillageTemple(FamousTemple):
    temple = "LakshmiTirumala"
* Now VillageTemple has access to all the attributes and methods defined in FamousTemple, unless overridden.

## Method Overriding
Method overriding occurs when a subclass defines a method with the same name as one in its superclass, replacing the original behavior.

Example:
In the FamousTemple class:

def Laddu(self):
    self.quanty = 200
    self.taste = "Excelent"
    self.ingredeants = ("Sugar", "Ghee", "Badam")
    print(self.taste)

* In the VillageTemple class (override):

def Laddu(self):
    self.quanty = 100
    self.taste = "Ok"
    self.ingredeants = ("Sugar", "Rawa")
    print(self.taste)
* When Laddu() is called on a VillageTemple object, it uses the overridden version.

## 2. Real-World Modeling with Classes
* The code represents two types of temples:

# FamousTemple :
Class variable: temple = "Tirumala"

# Instance variables:
  * height = 9.9
  * energy = "High Possitive"
  * gods = ("Vishnu", "Varahaswamy")
# Method:
 * Laddu() – prints laddu taste and ingredients

# VillageTemple
Class variable: temple = "LakshmiTirumala"
Inherits from FamousTemple
Additional attributes:
  * vheight = 9.7
  * venergy = "Possitive"
  * vgods = ["Vishnu", "Lakshmi"]

# Method:
 * display() – prints inherited and new values
 * Laddu() – overridden method with a different laddu recipe

## 3. How the Program Works
* When the program is run:

venkatesh = VillageTemple()
venkatesh.display()
venkatesh.Laddu()























