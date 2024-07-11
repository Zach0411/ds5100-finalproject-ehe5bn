import unittest
import pandas as pd
import numpy as np
from montecarlo.montecarlo import Die, Game, Analyzer

class montecarloTest(unittest.TestCase):
    
    def test_dataframe(self):
        a = np.array([1,2,3])
        object1 = Die(a)
        self.assertIsInstance(object1.df_die, pd.DataFrame)
        
    def test_weight(self):
        a = np.array([1,2,3])
        object1 = Die(a)
        object1.change_weight(1,90)
        x = object1.current_state()
        z = x.reset_index()
        c = z.values[0,0]
        self.assertEqual(90, c)
        
    def test_roll_die(self):
        a = np.array([1,2,3])
        object1 = Die(a)
        x = len(object1.roll_die(2))
        y = 2
        self.assertEqual(x,y)
        
    def test_current_state(self):
        a = np.array([1,2,3])
        object1 = Die(a)
        object1.change_weight(1,90)
        x = object1.current_state()
        df3 = pd.DataFrame(
            columns=[0], 
            index=[90,1.0,1.0], 
            data=[[1],[2],[3]])
        self.assertTrue(x.equals(df3))
        
    def test_game_in(self):
        a = np.array([1,2,3,4,5,6])
        b = np.array([1,2,3,4,5,6])
        object4 = Die(a)
        object5 = Die(b)
        dice_list = [object4, object5]
        game1 = Game(dice_list)
        self.assertEqual(type(game1.dice_list), list)
        
    def test_playinggame(self):
        a = np.array([1,2,3,4,5,6])
        b = np.array([1,2,3,4,5,6])
        object4 = Die(a)
        object5 = Die(b)
        dice_list = [object4, object5]
        game1 = dice_list
        game1 = Game(dice_list)
        game1.play_game(3)
        game1.show_results()
        x = len(game1.show_results())
        self.assertTrue(x == 3)
        
        
    def test_showresults(self):
        a = np.array([1,2,3,4,5,6])
        b = np.array([1,2,3,4,5,6])
        object4 = Die(a)
        object5 = Die(b)
        dice_list = [object4, object5]
        game2 = Game(dice_list)
        game2.play_game(3)
        x = game2.show_results()
        row_count = len(x)
        y = 3
        self.assertEqual(row_count, y)
        
    def test_init_analyzer(self):
        a = np.array([1,2,3])
        Die1 = Die(a)
        dice_list = [Die1,Die1]
        Jgame = Game(dice_list)
        Jgame.play_game(3)
        Janalyzer = Analyzer(Jgame)
        self.assertIsInstance(Jgame, Game)
        
    
    def test_jackpot(self):
        a = np.array([1,2,3])
        Die1 = Die(a)
        Die1.change_weight(1,90)
        Die1.change_weight(2,0)
        Die1.change_weight(3,0)
        dice_list = [Die1,Die1]
        Jgame = Game(dice_list)
        Jgame.play_game(3)
        Janalyzer = Analyzer(Jgame)
        Janalyzer.jackpot()
        b = print('Jackpots:', int(3))
        self.assertEqual(b, Janalyzer.jackpot())
        
    def test_face_counts(self):
        a = np.array([1,2,3])
        Die1 = Die(a)
        Die1.change_weight(1,90)
        Die1.change_weight(2,0)
        Die1.change_weight(3,0)
        dice_list = [Die1,Die1]
        Jgame = Game(dice_list)
        Jgame.play_game(3)
        Janalyzer = Analyzer(Jgame)
        Janalyzer.face_counts()
        y = 3
        self.assertEqual(y, len(Janalyzer.face_counts()))
        
    def test_combos(self):
        a = np.array([1,2])
        Die1 = Die(a)
        Die2 = Die(a)
        dice_list = [Die1,Die2]
        Jgame = Game(dice_list)
        Jgame.play_game(40)
        Janalyzer = Analyzer(Jgame)
        x2 = Janalyzer.combos().copy()
        y = 3
        self.assertTrue(len(x2) <= y)
        
        
    def test_permutations(self):
        a = np.array([1,2])
        Die1 = Die(a)
        Die2 = Die(a)
        dice_list = [Die1,Die2]
        Jgame = Game(dice_list)
        Jgame.play_game(40)
        Janalyzer = Analyzer(Jgame)
        x2 = Janalyzer.permutation().copy()
        y = 4
        self.assertTrue(len(x2) <= y)
        
if __name__ == '__main__':
    
    unittest.main(verbosity=3)