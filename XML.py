from xml.dom.minidom import parse


def save_xml (nomfichier):
    dom = parse (nomfichier)
    root = dom.getElementsByTagName ("Individue")[0]
    reponse = "Non"
    while reponse != "Oui":
        x = dom.createElement ("Person")
        root.appendChild (x)
        tags = dom.getElementsByTagName ("Person")[0]
        nom = str (input ("Saisir un nom : "))
        x = dom.createElement ("Nom")
        txt_nom = dom.createTextNode (nom)
        x.appendChild (txt_nom)
        tags.appendChild (x)
        prenom = str (input ("Saisir un prenom : "))
        x = dom.createElement ("Prenom")
        txt_prenom = dom.createTextNode (prenom)
        x.appendChild (txt_prenom)
        tags.appendChild (x)
        adresse = str (input ("Saisir une adresse : "))
        x = dom.createElement ("Adresse")
        txt_adresse = dom.createTextNode (adresse)
        x.appendChild (txt_adresse)
        tags.appendChild (x)
        code = str (input ("Saisir un code postal : "))
        x = dom.createElement ("CodePostal")
        txt_code = dom.createTextNode (code)
        x.appendChild (txt_code)
        tags.appendChild (x)
        numero = str (input ("Saisir une numero de telephone : "))
        x = dom.createElement ("Numero")
        txt_numero = dom.createTextNode (numero)
        x.appendChild (txt_numero)
        tags.appendChild (x)
        reponse = str (input ("Arreter? Oui/ Non : "))
    dom.writexml (open ("personnes.xml", "w"))


def ajouter_xml (nomfichier):
    dom = parse (nomfichier)
    for node in dom.getElementsByTagName ("Numero"):
        date = str (input ("Saisir un date de naissance: "))
        x = dom.createElement ("DateDeNaissance")
        txt_date = dom.createTextNode (date)
        x.appendChild (txt_date)
        node.appendChild (x)
        sexe = str (input ("Saisir un sexe : "))
        x = dom.createElement ("Sexe")
        txt_sexe = dom.createTextNode (sexe)
        x.appendChild (txt_sexe)
        node.appendChild (x)
    dom.writexml (open ("personnes.xml", "w"))


def chercher_xml(codepostal, nomfichier):
    dom = parse(nomfichier)
    for node in dom.getElementsByTagName ("Person"):
        node_code = dom.getElementsByTagName ("CodePostal")[0]
        if codepostal == node_code.childNodes[0].nodeValue:
            for node in dom.getElementsByTagName("Person"):
                node_nom = dom.getElementsByTagName("Nom")[0]
                print(node_nom.childNodes[0].nodeValue)
                node_prenom = dom.getElementsByTagName("Prenom")[0]
                print(node_prenom.childNodes[0].nodeValue)
                node_code = dom.getElementsByTagName("CodePostal")[0]
                print(node_code.childNodes[0].nodeValue)
                node_address = dom.getElementsByTagName("Adresse")[0]
                print(node_address.childNodes[0].nodeValue)
                node_numero = dom.getElementsByTagName ("Numero")[0]
                print(node_numero.childNodes[0].nodeValue)
                node_sexe = dom.getElementsByTagName ("Sexe")[0]
                print (node_sexe.childNodes[0].nodeValue)
        else:
            print("Il y n'a pas de code postal dans le fichier .xml")

def chercher_xml_lettres(nomfichier):
        dom = parse(nomfichier)
        for node in dom.getElementsByTagName ("Person"):
            node_prenom = dom.getElementsByTagName("Prenom")[0]
            if node_prenom.childNodes[0].nodeValue >="F" or "f" <= node_prenom.childNodes[0].nodeValue <= "M" or \
                    node_prenom.childNodes[0].nodeValue <= "m":
                for node in dom.getElementsByTagName ("Person"):
                    node_nom = dom.getElementsByTagName ("Nom")[0]
                    print (node_nom.childNodes[0].nodeValue)
                    node_prenom = dom.getElementsByTagName ("Prenom")[0]
                    print (node_prenom.childNodes[0].nodeValue)
                    node_code = dom.getElementsByTagName ("CodePostal")[0]
                    print (node_code.childNodes[0].nodeValue)
                    node_address = dom.getElementsByTagName ("Adresse")[0]
                    print (node_address.childNodes[0].nodeValue)
                    node_numero = dom.getElementsByTagName ("Numero")[0]
                    print (node_numero.childNodes[0].nodeValue)
                    node_sexe = dom.getElementsByTagName ("Sexe")[0]
                    print (node_sexe.childNodes[0].nodeValue)
            else:
                print ("Il y n'a pas des prenoms avec les letters entre F(f) et M(m) dans le fichier .xml")

# save_xml("personnes.xml")
#ajouter_xml("personnes.xml")
#chercher_xml ("tttyyy", "personnes.xml")
#chercher_xml ("tttyyyff", "personnes.xml")
#chercher_xml_lettres("personnes.xml")
