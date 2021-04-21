"""
import pygame

pygame.init()
pygame.font.init()
#écriture
font = pygame.font.Font("BlackRose-2Onld.ttf",50)
img_jouer= font.render('JOUER', False, (125,255,30))
    
#Display
fenetre = pygame.display.set_mode((1000,700))

#bouton_class
class bouton():
    def __init__(self,txt,couleurtxt,positionx,positiony,longueur,largeur,couleur):
        self.rect = pygame.Rect(positionx,positiony,longueur,largeur)
        self.positionx = positionx
        self.positiony = positiony
        self.longueur= longueur
        self.largeur = largeur
        self.couleur = couleur
        self.couleurtxt = couleurtxt
        self.txt= txt
        self.rendertxt= font.render(txt, False, couleurtxt)
        self.txtrect = self.rendertxt.get_rect(center = self.rect.center)

    def draw(self,fenetre, *args):
        pygame.draw.rect(fenetre,self.couleur,self.rect)
        fenetre.blit(self.rendertxt, self.txtrect)
        for arg in args:
            touche = font.render(arg,False, self.couleurtxt)
            fenetre.blit(touche,(360,self.txtrect[1]))        
#commandes

dico_touches= {"avancer":pygame.K_z,"reculer":pygame.K_s,"droite":pygame.K_d,"gauche":pygame.K_q,"dash":pygame.K_LSHIFT,"pause":pygame.K_p,"abilité":pygame.K_SPACE}
boutons_touche = []
for i in range(len(dico_touches)):
    boutons_touche.append(bouton(list(dico_touches)[i],(139,109,156),30,50+90*i,250,60,(0,0,0)))

        
#boutons
bouton_jouer = bouton("Jouer",(139,109,156),400,255,200,50,(255,255,255))
bouton_options = bouton("Options",(139,109,156),400,325,200,50,(255,255,255))
bouton_commandes = bouton("Commandes",(139,109,156),375,320,250,60,(255,255,255))
bouton_langue = bouton("Langues",(139,109,156),375,245,250,60,(255,255,255))
bouton_volume = bouton("Volume",(139,109,156),400,400,200,50,(255,255,255))
bouton_volume_effets_sonores = bouton("Effets sonores",(139,109,156),200,450,600,50,(255,255,255))
bouton_volume_musique = bouton("Musique",(139,109,156),200,200,600,50,(255,255,255))
slider_es = bouton("",(139,109,156),200,300,600,50,(255,255,255))
slider_m = bouton("",(139,109,156),200,550,600,50,(255,255,255))
barre_es = bouton("",(139,109,156),250,324,500,2,(255,255,255))
barre_m = bouton("",(139,109,156),250,574,500,2,(255,255,255))
truc_es = bouton("",(139,109,156),720,310,20,30,(255,255,255))
truc_m = bouton("",(139,109,156),720,560,20,30,(255,255,255))
menu_actif = "jouer"

def boutons_couleur(bouton):
    if bouton.rect.collidepoint(pos_souris):
        bouton.couleur =(73,77,126)
    else :
        bouton.couleur =(0,0,0)
#varalbes
fenetrefill = False
    
continuer= True
frame = 0
maxframe= 0
boutonselect = -1
pos_souris_1 = (0,0)
pos_souris_2 = (0,0)

while continuer==True :
    fenetre.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if boutonselect > -1 :
                nouvelletouche = event.key
                dico_touches[boutons_touche[boutonselect].txt] = nouvelletouche
                boutonselect = -1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE :
                if menu_actif == "options" :
                    menu_actif = "jouer"
                    fenetrefill == False
                elif menu_actif == "commandes" :
                    menu_actif = "options"
                elif menu_actif == "volume" :
                    menu_actif = "options"
                elif menu_actif == "langue" :
                    menu_actif = "options"
    #if pygame.mouse.get_pressed()[0]and truc_es.rect.collidepoint(pos_souris)and menu_actif == "volume":
            
            
    #positionsouris
    pos_souris = pygame.mouse.get_pos()
    
    #menus
    if menu_actif == "jouer":
        boutons_couleur(bouton_jouer)
            
        boutons_couleur(bouton_options)

        if fenetrefill == False :
            bouton_jouer.draw(fenetre)
            bouton_options.draw(fenetre)
        
    elif menu_actif == "options":
        boutons_couleur(bouton_commandes)
            
        boutons_couleur(bouton_langue)
        boutons_couleur(bouton_volume)
            
        bouton_langue.draw(fenetre)
        bouton_commandes.draw(fenetre)
        bouton_volume.draw(fenetre)
    
    elif menu_actif == "commandes":
        for i in range(len(boutons_touche)) :
            keyname = list(dico_touches.values())[i]
            boutons_touche[i].draw(fenetre,pygame.key.name(keyname))
            boutons_couleur(boutons_touche[i])
            
            if pygame.mouse.get_pressed(num_buttons = 3)[0]and boutons_touche[i].rect.collidepoint(pos_souris)and menu_actif == "commandes":
                boutonselect = i
        if boutonselect > -1 :
            if (frame//100)%2 == 0 :
                boutons_touche[boutonselect].couleur = (73,77,126)
            else :
                boutons_touche[boutonselect].couleur = (0,0,0)
    elif menu_actif == "volume" :
        boutons_couleur(bouton_volume_effets_sonores)
        boutons_couleur(bouton_volume_musique)
        boutons_couleur(slider_es)
        boutons_couleur(slider_m)

        bouton_volume_effets_sonores.draw(fenetre)
        bouton_volume_musique.draw(fenetre)
        slider_es.draw(fenetre)
        slider_m.draw(fenetre)
        barre_es.draw(fenetre)
        barre_m.draw(fenetre)
        truc_es.draw(fenetre)
        truc_m.draw(fenetre)
    #elif menu_actif == "langue" :
        
        

    #clic
    if maxframe < frame :
        if pygame.mouse.get_pressed(num_buttons = 3)[0]and bouton_options.rect.collidepoint(pos_souris)and menu_actif == "jouer":
            fenetre.fill((0,0,0))
            menu_actif = "options"
            maxframe = frame +60
        elif pygame.mouse.get_pressed(num_buttons = 3)[0]and bouton_commandes.rect.collidepoint(pos_souris)and menu_actif == "options":
            fenetre.fill((0,0,0))
            menu_actif ="commandes"
            maxframe = frame +60
        elif pygame.mouse.get_pressed(num_buttons = 3)[0]and bouton_jouer.rect.collidepoint(pos_souris)and menu_actif == "jouer":
            fenetre.fill((0,0,0))
            fenetrefill= True
            maxframe = frame +60
        elif pygame.mouse.get_pressed(num_buttons = 3)[0]and bouton_volume.rect.collidepoint(pos_souris)and menu_actif == "options":
            fenetre.fill((0,0,0))
            menu_actif= "volume"
            maxframe = frame +60
        elif pygame.mouse.get_pressed(num_buttons = 3)[0]and bouton_langue.rect.collidepoint(pos_souris)and menu_actif == "options":
            fenetre.fill((0,0,0))
            menu_actif= "langue"
            maxframe = frame +60
    #slider
    pos_souris_1 = pygame.mouse.get_pos()
    delta_pos = [0,0]
    delta_pos[0] = pos_souris_1[0] - pos_souris_2[0]
    pos_souris_2 = pos_souris_1
    if pygame.mouse.get_pressed(num_buttons = 3)[0]and slider_es.rect.collidepoint(pos_souris)and menu_actif == "volume":
        truc_es.rect.update((pygame.mouse.get_pos()[0],truc_es.rect.topleft[1]), truc_es.rect.size)
    elif pygame.mouse.get_pressed(num_buttons = 3)[0]and slider_m.rect.collidepoint(pos_souris)and menu_actif == "volume":
        truc_m.rect.update((pygame.mouse.get_pos()[0],truc_m.rect.topleft[1]), truc_m.rect.size)
    
    
    frame +=1
    pygame.display.flip()
"""
