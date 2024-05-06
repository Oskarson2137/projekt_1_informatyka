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

   def Npu(self,fi):
    """
     Funkcja liczy parametr N dla podanej szerokosci geodezyjnej na danej elipsoidzie.

        Parameters
        ----------
        fi : [float] szerokosć geodezyjna punktu dla którego chcemy obliczyć N
             Jednostka: [rad]
                    

        Returns
        -------
        N : [float] promień przekroju krzywizny elipsoidy w 1-szym wertykale
            jedn: [m]

        """
    N = self.a / np.sqrt(1 - self.e2 * np.sin(fi)**2)
         return N

    def hirvonen(self,X,Y,Z):
       """
        Funkcja przelicza współrzędne geocentryczne XYZ na współrzędne geodezyjne krzywoliniowe,
        realizując algorytm Hirvonena.

        Parameters
        ----------
        X : [float] współrzędna geocentryzna X danego punktu
            jedn: [m]
        Y : [float] współrzędna geocentryczna Y danego punktu
            jednostka: [m]
        Z : [float] współrzędna geocentryczna Z danego punktu
            jednostka: [m]

        Returns
        -------
        wyniki : [list] lista współrzędnych geodezyjnych danego punktu, w kolejnosci: phi, lambda, h.
                 jednostka: phi, lambda [st_dziesiętne], h [m]

        """
        wyniki = []
        for X, Y, Z in zip(X, Y, Z):
            p = np.sqrt(X**2+Y**2)
            fi = np.arctan(Z/(p*(1-self.e2)))
            while True:
                N = self.Npu(fi)
                h = (p/np.cos(fi)) - N
                fi_poprzednia = fi
                fi = np.arctan((Z/p)/(1-((N*self.e2)/(N+h))))
                if abs(fi_poprzednia-fi)<(0.000001/206265):
                    break
            N = self.Npu(fi)
            h = p/np.cos(fi) - N
            lam = np.arctan(Y/X)
            wyniki.append([np.rad2deg(fi), np.rad2deg(lam), h])
            
        return wyniki

    def hirvonen_odw(self,fi,lam,h):
       """
        Funkcja przelicza współrzędne geodezyjne krzywoliniowe danego punktu na 
        współrzędne geocentryczne X, Y, Z.

        Parameters
        ----------
        fi : [float] szerokosć geodezyjna danego punktu
             jednostka: [rad]
        lam : [float] długosć geodezyjna danego punktu
              jednostka: [rad]
        h : [float] wysokosć danego punktu nad przyjętą elipsoidą
            jednostka: [m]

        Returns
        -------
        wyniki : [list] lista współrzędnych geocentrycznych danego punktu
                 w kolejnosci: X, Y, Z.
                 jednostka: [m]

        """
        wyniki = []
        #fi = radians(fi)
        #lam = radians(lam)
        for fi, lam, h in zip(fi, lam, h):
            N = self.Npu(fi)
            Xk = (N+h)*np.cos(fi)*np.cos(lam)
            Yk = (N+h)*np.cos(fi)*np.sin(lam)
            Zk = (N*(1-self.e2)+h)*np.sin(fi)   
            wyniki.append([Xk,Yk,Zk])
            
        return wyniki

    def pl1992(self,fi,lama,m=0.9993):
       """
       Funkcja przelicza podane współrzędne geodezyjne krzywoliniowe na współrzędne X, Y na 
        płaszczyźnie Gaussa-Kruggera, a następnie na współrzędne w układzie 
        PL 1992.

        Parameters
        ----------
        fi : [float] szerokosć geodezyjna danego punktu
             jednostka: [rad]
        lama : [float] długosć geodezyjna danego punktu
              jednostka: [rad]
        m : [float] skala zniekształceń układu PL 1992
            jednostka: brak

        Returns
        -------
        wyniki : [list] lista współrzędnych w układzie PL 1992, w kolejnosci: X92, Y92
                 jednostka: [m]

        """
        lama0 = np.deg2rad(19)
        wyniki = []
        for fi, lama in zip (fi,lama):   
            b2 = self.a**2*(1-self.e2)
            ep2 = (self.a**2-b2)/b2
            dellama = lama - lama0
            t = np.tan(fi)
            ni2 = ep2*(np.cos(fi)**2)
            N = self.Npu(fi)
         
            A0 = 1- (self.e2/4)-(3*self.e2**2/64)-(5*self.e2**3/256)
            A2 = (3/8)*(self.e2+(self.e2**2/4)+(15*self.e2**3/128))
            A4 = (15/256)*(self.e2**2+((3*self.e2**3)/4))
            A6 = (35*self.e2**3)/3072
            sigma = self.a *(A0*fi-A2*np.sin(2*fi)+A4*np.sin(4*fi)-A6*np.sin(6*fi))
        
            xgk =  sigma    +    ( ((dellama**2/2)*N*np.sin(fi)*np.cos(fi))    *    (1   +   ((dellama**2/12)*(np.cos(fi)**2)*(5 - t**2 + 9*ni2 + 4*ni2**2))      +         ((dellama**4/360)*(np.cos(fi)**4)*(61 - 58*t**2 + t**4 + 270*ni2 - 330*ni2*t**2))))
            ygk =  (dellama* N * np.cos(fi))  *   ( 1 +  ((dellama**2/6)   *   (np.cos(fi)**2)   *  (1 - t**2 + ni2))     +     (((dellama**4/120)*(np.cos(fi)**4)) * (5 - (18*t**2) + t**4 + (14 * ni2) - (58*ni2*t**2))))
        
            x92 = xgk * m - 5300000
            y92 = ygk*m + 500000
            wyniki.append([x92,y92])

    def pl2000(self,fi,lama,m=0.999923):
        wyniki = []
        for fi, lama in zip (fi,lama):
            lama0 = 0
            strefa = 0
            if lama >np.deg2rad(13.5) and lama < np.deg2rad(16.5):
                strefa = 5
                lama0 = np.deg2rad(15)
            elif lama >np.deg2rad(16.5) and lama < np.deg2rad(19.5):
                strefa = 6
                lama0 = np.deg2rad(18)
            elif lama >np.deg2rad(19.5) and lama < np.deg2rad(22.5):
                strefa =7
                lama0 = np.deg2rad(21)
            elif lama >np.deg2rad(22.5) and lama < np.deg2rad(25.5):
                strefa = 8
                lama0 = np.deg2rad(24)
            
            b2 = self.a**2*(1-self.e2)    
            ep2 = (self.a**2-b2)/b2
            dellama = lama - lama0
            t = np.tan(fi)
            ni2 = ep2*(np.cos(fi)**2)
            N = self.Npu(fi)
             
            A0 = 1- (self.e2/4)-(3*self.e2**2/64)-(5*self.e2**3/256)
            A2 = (3/8)*(self.e2+(self.e2**2/4)+(15*self.e2**3/128))
            A4 = (15/256)*(self.e2**2+((3*self.e2**3)/4))
            A6 = (35*self.e2**3)/3072
            
            sigma = self.a *(A0*fi-A2*np.sin(2*fi)+A4*np.sin(4*fi)-A6*np.sin(6*fi))
            
            xgk =  sigma    +    ( ((dellama**2/2)*N*np.sin(fi)*np.cos(fi))    *    (1   +   ((dellama**2/12)*(np.cos(fi)**2)*(5 - t**2 + 9*ni2 + 4*ni2**2))      +         ((dellama**4/360)*(np.cos(fi)**4)*(61 - 58*t**2 + t**4 + 270*ni2 - 330*ni2*t**2))))
            ygk =  (dellama* N * np.cos(fi))  *   ( 1 +  ((dellama**2/6)   *   (np.cos(fi)**2)   *  (1 - t**2 + ni2))     +     (((dellama**4/120)*(np.cos(fi)**4)) * (5 - (18*t**2) + t**4 + (14 * ni2) - (58*ni2*t**2))))
            
            x2000 = xgk * m 
            y2000 = ygk*m + (strefa *1000000) +500000
            wyniki.append([x2000,y2000])
            
        return  wyniki

     def Rneu(self, phi, lam):
           Rneu = np.array([[-np.sin(phi)*np.cos(lam), -np.sin(lam), np.cos(phi)*np.cos(lam)],
                         [-np.sin(phi)*np.sin(lam), np.cos(lam), np.cos(phi)*np.sin(lam)],
                         [np.cos(phi), 0, np.sin(phi)]])
        
        return Rneu

      def xyz2neup(self, X, Y, Z, X0, Y0, Z0):
         wyniki = []
        p = np.sqrt(X0**2+Y0**2)
        fi = np.arctan(Z0/(p*(1-self.e2)))
        while True:
            N = self.Npu(fi)
            h = (p/np.cos(fi)) - N
            fi_poprzednia = fi
            fi = np.arctan((Z0/p)/(1-((N*self.e2)/(N+h))))
            if abs(fi_poprzednia-fi)<(0.000001/206265):
                break 
        N = self.Npu(fi)
        h = p/np.cos(fi) - N
        lam = np.arctan(Y0/X0)
        
        R_neu = self.Rneu(fi, lam)
        for X, Y, Z in zip(X, Y, Z):
            X_sr = [X-X0, Y-Y0, Z-Z0] 
            X_rneu = R_neu.T@X_sr
            wyniki.append(X_rneu.T)
            
        return wyniki

   
       


         


        
       
   
       


     
     
     
    
     
  



