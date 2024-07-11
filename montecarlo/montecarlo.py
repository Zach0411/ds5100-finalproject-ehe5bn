# Montecarlo Project
import pandas as pd
import numpy as np

class Die():
    '''Purpose: The purpose of the Die class is to create a "die" object with N number of sides and W weights.
    Weights can be changed but default to 1 for each face and are a positive number (a float or an integer). 
    Each side contains a unique symbol. This die object is created to be rolled one or more times.
    '''
    
    def __init__(self, array):
        '''To initialize Die class, input required is a numpy array of strings or numbers. 
        Values in array must be distinct. This will save die attributes in a dataframe with weights defaulting to 1.
        '''
        #make sure input was an array
        if not isinstance(array, np.ndarray):
            raise TypeError("Input must be a numpy array.")
            
        #make sure values are distinct
        if len(array) != len(set(array)):
            raise ValueError("Values in the array must be distinct.")
            
        #initialize faces
        self.faces = array
        
        #weights of one for each face
        self.weights = np.ones(len(array))
        
        #save to a dataframe
        self.df_die = pd.DataFrame(array, index = self.weights)
        
    def change_weight(self, face, new_weight):
        '''Purpose: change weight of any face of the die object
        
        Parameters: change_weight(face, new_weight)
        face: input existing face to change weight of
        new_weight: adjust weight of face by inputing integer or float
        '''
        if face not in self.faces:
            raise IndexError("Face value does not exist")
        if type(new_weight) != int and type(new_weight) != float:
            raise TypeError("New Weight must be numeric")
        else:
            self.weights[np.where(self.faces == face)] = new_weight #changes weight based on index
    
    def roll_die(self, num_rolls = 1):
        '''Purpose: To roll created die object N number of times
        
        Parameters: roll_die(num_rolls=1) **defaults to one
        num_rolls (optional): can specify number of rolls for the die to make
        
        Returns: a list of results of the outcome(s)
        '''
        self.num_rolls = num_rolls
        results = []
        #set probabilities based on weights
        self.my_probs = [i/sum(self.weights) for i in self.weights]
        #Roll die based on number of rolls and weights
        for i in range(self.num_rolls):
            result = self.df_die.sample(weights=self.weights).values[0]
            results_list = list(result)
            results.extend(results_list)
        return results
    
    def current_state(self):
        '''Purpose: return an updated dataframe of the faces of the die object and the corresponding weights
        
        Parameters: current_state()
        No parameters, however, requires existing die object to have been created
        
        Returns: a dataframe of the updated die object
        '''
        return self.df_die.copy()
        
class Game():
    '''Purpose: Roll one or more similar dice (die objects) of same number of sides and associated faces.
    
    Parameters: Game(list of dice)
    Requires a list of die objects to be rolled'''
    
    def __init__(self, dice_list):
        '''Purpose: inializes die objects to be rolled
        
        Parameters: Game(dice_list)
        dice_list represents a list of previously created die objects from the Die Class.'''
    
        self.dice_list = dice_list #must be a list of similar dice

    def play_game(self, num_rolls):
        '''Purpose: Specify number of times the dice should be rolled
        
        Parameters: play_game(num_rolls):
        num_rolls: Requires a positive integer input
        
        Saves die to a private dataframe, use show_result() to return results.'''
        if type(num_rolls) != int:
            raise ValueError('Must be an integer for number of rolls')
        else:
            self.rolls = num_rolls
        self.rolls_outcome = [die.roll_die(num_rolls) for die in self.dice_list]
        self.df_game = pd.DataFrame(self.rolls_outcome).T
        self.df_game.index.name = 'n'
        self.df_game.index += 1

    def show_results(self, choice='wide'):
        '''Purpose: Show results of rolled dice in a dataframe
        
        Parameters: show_result(choice='wide'), default to wide
        Option: choose 'narrow' to recieve dataframe in narrow form
        
        Returns: specified dataframe of results of game played (dice rolled)
        '''
        copy = self.df_game.copy()
        if choice == 'wide':
            return copy
        elif choice == 'narrow':
            narrow = copy.stack()
            narrow2 = copy.stack().to_frame()         
            return  narrow2 #change to narrow
        else:
            raise ValueError("Must choose between 'wide' or 'narrow'")

            
class Analyzer():
    '''Purpose: This class contains multiple function to compute descriptive statistics of games played.
    
    Requirement: Requires game object to be initiated.
    '''
    def __init__(self, play): #initializes game to analyze
        '''Purpose: initialize Analyzer class with Game object
        
        Parameters: Analyzer(play)
        play: a Game object created
        '''
        if not isinstance(play, Game):
            raise ValueError("Input must be a Game object")
        else:
            self.play = play

    def jackpot(self):
        '''Purpose: Computes how many times Game resulted in jackpot (all of the same faces rolled)
        
        Parameters: None
        
        Returns: Integer number of jackkpots
        '''
        counter = 0
        y = self.play.show_results().T
        for i in y:
            if y[i].nunique() == 1:
                counter += 1
        y = print('Jackpots:', int(counter))
        return y

    def face_counts(self):
        '''Purpose: Computes how many times a face was rolled in each event.
        
        Parameters: None
        
        Returns: A wide dataframe of results with index as roll number, 
        face values as column headers, count of face values in the cells.
        '''
        face_values = self.play.dice_list[0].faces.tolist()
        roll_counts = []
        for roll in self.play.show_results().values:
            roll_count = {face: roll.tolist().count(face) for face in face_values}
            roll_counts.append(roll_count)
        
        df_counts = pd.DataFrame(roll_counts)
        df_counts.index.name = 'Roll'
        df_counts.index += 1
        return df_counts

    def combos(self):
        '''Purpose: Compute distinct combinations of faces rolled along with the counts, order independdent.
        
        Parameters: None
        
        Returns: Dataframe in wide format of with multiindex of distinct combinations and a column of
        associated counts.
        '''
        z = self.play.show_results().copy() #brings dataframe of results
        t = pd.DataFrame(np.sort(z.values, axis=1), columns=z.columns).value_counts().reset_index(name='counts')
        t_newindex = t.set_index([c for c in t.columns if c != 'counts'])
        return t_newindex
    
    def permutation(self):
        '''Purpose: Computes the distinct permutations of faces rolled, along with their counts, order
        dependent.
        
        Parameters: None
        
        Returns: Dataframe in wide format of with multiindex of distinct permutations and a column of
        associated counts.
        '''
        c = self.play.show_results().copy()
        c_perms = c.value_counts().to_frame()
        return c_perms