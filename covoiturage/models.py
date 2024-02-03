# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class clientspec(models.Model):
#     _name = 'clientspec.clientspec'

#     name = fields.Char()

class Trajet(models.Model):
    _name = 'covoiturage.trajet'
    _description = "Les trajets"
    name = fields.Char(string="Nom_trajet", required=True)
    date = fields.Date()
    vehicule = fields.Char(string="Nom_vehicule")
    point_depart = fields.Char(string="Point_depart") 
    point_arrivee = fields.Char(string="Point_arrivee")
    etat = fields.Selection([
         ('Proposer', 'Proposer'),
         ('Conferme', 'Conferme'),
         ('Terminé', 'Terminé'),
         ('Annulé', 'Annulé')],
         default='Proposer', string='etet')
    note = fields.Selection([
         ('1', '1'),
         ('2', '2'),
         ('3', '3')],
         string='note')
    
    def act_conferme(self):
        self.etat = "conferme"
    def act_annuler(self):
        self.etat = "Annulé"
    def act_terminer(self):
        self.etat = "Terminé"
 

class  Signalement(models.Model):
    _name = 'covoiturage.signalement'
    _description = "Les signalement"

    name = fields.Char(string="Nom_signamelent", required=True)
    cause = fields.Selection([  
         ('retard', 'retard'),
         ('changement de trajet', 'changement de trajet'),
         ('problème dans le véhicule', 'problème dans le véhicule')],
         string='cause')
    trajet = fields.Many2one("covoiturage.trajet", 
        ondelete="cascade", string="trajet", required = True)

    


   