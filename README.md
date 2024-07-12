# **Montecarlo Simulation- ds5100-finalproject-ehe5bn :**
:game_die:	
Montecarlo is a Python Module for simulating dice being rolled along with being able to see descriptive statistics. Montecarlo contains three classes, *Die* (to create the Die objects), *Game* (to roll Die objects), and *Analyzer* (to view statistics of each game). :game_die:

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install montecarlo.

```bash
pip install montecarlo
```
Import the three classes
```bash
from montecarlo.montecarlo import Die, Game, Analyzer
```
<u>Required packages</u>:
+ pandas
+ numpy

## Die Class Demo
```python
#Create a die object with an array of distinct values
Die1 = np.array([1,2,3,4,5,6])

Die_example = Die(array)

#Change weights of a die
Die_example.change_weight(2, 6)
```
## Game Class Demo
```python
#Create game object using list of Die Classes
dice_list = [Die1, Die2]
Die_game = Game(dice_list)

#Play game three times (rolls two dice, three times)
Die_game.play_game(3)

#Show results of the game in a dataframe
Die_game.show_results()
```

## Analyzer Class Demo
```python
#instantiate an Analyzer object with a Game object
Die_Analyze = Analyze(Die_game)

#View different statistics such as permutations
Die_Analyze.permutation()
```

## Code help (API)

```python
class Die():
    '''Purpose: The purpose of the Die class is to create a "die" object with N number of sides and W weights.
    Weights can be changed but default to 1 for each face and are a positive number (a float or an integer). 
    Each side contains a unique symbol. This die object is created to be rolled one or more times.
    '''
    
    def __init__(self, array):
        '''To initialize Die class, input required is a numpy array of strings or numbers. 
        Values in array must be distinct. This will save die attributes in a dataframe with weights defaulting to 1.
        '''
        
    def change_weight(self, face, new_weight):
        '''Purpose: change weight of any face of the die object
        
        Parameters: change_weight(face, new_weight)
        face: input existing face to change weight of
        new_weight: adjust weight of face by inputing integer or float
        '''
    
    def roll_die(self, num_rolls = 1):
        '''Purpose: To roll created die object N number of times
        
        Parameters: roll_die(num_rolls=1) **defaults to one
        num_rolls (optional): can specify number of rolls for the die to make
        
        Returns: a list of results of the outcome(s)
        '''
    
    def current_state(self):
        '''Purpose: return an updated dataframe of the faces of the die object and the corresponding weights
        
        Parameters: current_state()
        No parameters, however, requires existing die object to have been created
        
        Returns: a dataframe of the updated die object
        '''
        
class Game():
    '''Purpose: Roll one or more similar dice (die objects) of same number of sides and associated faces.
    
    Parameters: Game(list of dice)
    Requires a list of die objects to be rolled'''
    
    def __init__(self, dice_list):
        '''Purpose: inializes die objects to be rolled
        
        Parameters: Game(dice_list)
        dice_list represents a list of previously created die objects from the Die Class.'''
    
    def play_game(self, num_rolls):
        '''Purpose: Specify number of times the dice should be rolled
        
        Parameters: play_game(num_rolls):
        num_rolls: Requires a positive integer input
        
        Saves die to a private dataframe, use show_result() to return results.'''

    def show_results(self, choice='wide'):
        '''Purpose: Show results of rolled dice in a dataframe
        
        Parameters: show_result(choice='wide'), default to wide
        Option: choose 'narrow' to recieve dataframe in narrow form
        
        Returns: specified dataframe of results of game played (dice rolled)
        '''
            
class Analyzer():
    '''Purpose: This class contains multiple function to compute descriptive statistics of games played.
    
    Requirement: Requires game object to be initiated.
    '''
    def __init__(self, play): #initializes game to analyze
        '''Purpose: initialize Analyzer class with Game object
        
        Parameters: Analyzer(play)
        play: a Game object created
        '''

    def jackpot(self):
        '''Purpose: Computes how many times Game resulted in jackpot (all of the same faces rolled)
        
        Parameters: None
        
        Returns: Integer number of jackkpots
        '''

    def face_counts(self):
        '''Purpose: Computes how many times a face was rolled in each event.
        
        Parameters: None
        
        Returns: A wide dataframe of results with index as roll number, 
        face values as column headers, count of face values in the cells.
        '''

    def combos(self):
        '''Purpose: Compute distinct combinations of faces rolled along with the counts, order independdent.
        
        Parameters: None
        
        Returns: Dataframe in wide format of with multiindex of distinct combinations and a column of
        associated counts.
        '''
       
    def permutation(self):
        '''Purpose: Computes the distinct permutations of faces rolled, along with their counts, order
        dependent.
        
        Parameters: None
        
        Returns: Dataframe in wide format of with multiindex of distinct permutations and a column of
        associated counts.
        '''
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
