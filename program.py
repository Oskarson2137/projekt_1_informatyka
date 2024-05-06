import numpy as np
from argparse import ArgumentParser

class Transformation:
   def __init__(self,elip):
     """
     Funkcja definiuje parametry elipsoidy obrotowej.

        Parameters
        ----------
       
        elip : [list] lista parametrów elipsoidy obrotowej, w kolejnosci: a, e^2
               jednostka: [m] 

        Returns
        -------
        None.

        """
      self.a = elip[0]
     self.e2 = elip[1]


     
     
     
    
     
  



