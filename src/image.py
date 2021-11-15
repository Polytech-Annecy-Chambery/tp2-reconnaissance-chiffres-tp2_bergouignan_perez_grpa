from skimage import io
from skimage.transform import resize
import matplotlib.pyplot as plt
import numpy as np

class Image:
    def __init__(self):
        """Initialisation d'une image composee d'un tableau numpy 2D vide
        (pixels) et de 2 dimensions (H = height et W = width) mises a 0
        """
        self.pixels = None
        self.H = 0
        self.W = 0
    

    def set_pixels(self, tab_pixels):
        """ Remplissage du tableau pixels de l'image self avec un tableau 2D (tab_pixels)
        et affectation des dimensions de l'image self avec les dimensions 
        du tableau 2D (tab_pixels) 
        """
        self.pixels = tab_pixels
        self.H, self.W = self.pixels.shape


    def load(self, file_name):
        """ Lecture d'un image a partir d'un fichier de nom "file_name"""
        self.pixels = io.imread(file_name)
        self.H,self.W = self.pixels.shape 
        print("lecture image : " + file_name + " (" + str(self.H) + "x" + str(self.W) + ")")


    def display(self, window_name):
        """Affichage a l'ecran d'une image"""
        fig = plt.figure(window_name)
        if (not (self.pixels is None)):
            io.imshow(self.pixels)
            io.show()
        else:
            print("L'image est vide. Rien à afficher")


    #==============================================================================
    # Methode de binarisation
    # 2 parametres :
    #   self : l'image a binariser
    #   S : le seuil de binarisation
    #   on retourne une nouvelle image binarisee
    #==============================================================================
    def binarisation(self, S):
        
        im_binar = Image()
        im_binar.set_pixels(np.zeros((self.H,self.W), dtype=np.uint8))
                                                
        # boucle imbriquées
        for l in range(self.H):
            for c in range(self.W):
                # modif des pixels d'intensite <= à S
                if self.pixels[l][c] <= S:
                    im_binar.pixels[l][c] = 0 #le pixel devient noir
                else :
                    im_binar.pixels[l][c] = 255 #le pixel devient blanc
        return im_binar

    #==============================================================================
    # Dans une image binaire contenant une forme noire sur un fond blanc
    # la methode 'localisation' permet de limiter l'image au rectangle englobant
    # la forme noire
    # 1 parametre :
    #   self : l'image binaire que l'on veut recadrer
    #   on retourne une nouvelle image recadree
    #==============================================================================
    def localisation(self):
        # preparaton du resultat : creation d'une image vide 
        im_modif = image()
        
        #création des variables qui sont les bornes de l'image recadrée
        Li,Lf,Ci,Cf=self.H,0,self.W,0
                                                              
        # boucle imbriquees pour parcourir tous les pixels de l'image
        for l in range(self.H):
            for c in range(self.W):
                if self.pixels[l][c] == 0:
                    if Li>l:
                        Li=l
                    if Lf<l:
                        Lf=l
                    if Ci>c:
                        Ci=c
                    if Cf<c:
                        Cf=c
        im_modif.set_pixels(self.pixels[Li:Lf+1,Ci:Cf+1])
        return im_modif 

    #==============================================================================
    # Methode de redimensionnement d'image
    #==============================================================================
    def resize(self, new_H, new_W):
        # preparaton du resultat : creation d'une image vide 
        im_modif = image()
        #utilisation de la fonction resize
        im_modif.pixels = resize(self.pixels, (new_H,new_W), 0)
        #modifiaction pour adaptation au format
        im_modif.pixels = np.uint8(im_modif.pixels*255)
        return im_modif


    #==============================================================================
    # Methode de mesure de similitude entre l'image self et un modele im
    #==============================================================================
    def similitude(self, im):
        # création d'un compteur
        compteur=0
        # boucle imbriquees pour parcourir tous les pixels de l'image
        for l in range(self.H):
            for c in range(self.W):
                if self.pixels[l][c]==im.pixels[l][c]:
                    compteur=compteur+1
        return compteur/(self.H*self.W)
   
# fin class image

