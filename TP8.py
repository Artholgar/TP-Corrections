from subprocess import *
from os import listdir

if __name__ == "__main__":

    #On stoque la liste des noms des programmes dans lst_eleves
    lst_eleves = listdir('./Rendus_eleves/eleves_bis')

    #Fichier dans lequelle on va écrire les notes
    fich = open("resultats.csv", "w")

    for eleve in lst_eleves:
        compilation = 0
        warning = 0
        tests = 0
        qualite = 0

        #On test si le programme compile
        compil = Popen(["gcc", "-ansi", "-Wall", "-o", eleve[:-2], "./Rendus_eleves/eleves_bis/" + eleve], stdout = PIPE, stderr = PIPE, encoding = "utf8")
        compil.wait()

        #On compte le nombre de warnings
        if compil.returncode == 0:
            compilation = 1
        for ligne in compil.stderr:
            if 'warning' in ligne:
                warning += 1

        #Si le programme compile, on test les resultats
        if compilation == 1:
            out = Popen(["./" + eleve[:-2], "0", "0"], stdout = PIPE, encoding = "utf8")
            out.wait()

            for sortie in out.stdout:
                if(sortie == "La somme de 0 et 0 vaut 0\n"):
                    tests += 1
            

            out = Popen(["./" + eleve[:-2], "1", "0"], stdout = PIPE, encoding = "utf8")
            out.wait()

            for sortie in out.stdout:
                if(sortie == "La somme de 1 et 0 vaut 1\n"):
                    tests += 1


            out = Popen(["./" + eleve[:-2], "0", "1"], stdout = PIPE, encoding = "utf8")
            out.wait()

            for sortie in out.stdout:
                if(sortie == "La somme de 0 et 1 vaut 1\n"):
                    tests += 1
            

            out = Popen(["./" + eleve[:-2], "1", "1"], stdout = PIPE, encoding = "utf8")
            out.wait()

            for sortie in out.stdout:
                if(sortie == "La somme de 1 et 1 vaut 2\n"):
                    tests += 1
            

            out = Popen(["./" + eleve[:-2], "12", "12"], stdout = PIPE, encoding = "utf8")
            out.wait()

            for sortie in out.stdout:
                if(sortie == "La somme de 12 et 12 vaut 24\n"):
                    tests += 1


            out = Popen(["./" + eleve[:-2], "12", "-43"], stdout = PIPE, encoding = "utf8")
            out.wait()

            for sortie in out.stdout:
                if(sortie == "La somme de 12 et -43 vaut -31\n"):
                    tests += 1
            

            out = Popen(["./" + eleve[:-2], "-1", "-52"], stdout = PIPE, encoding = "utf8")
            out.wait()

            for sortie in out.stdout:
                if(sortie == "La somme de -1 et -52 vaut -53\n"):
                    tests += 1

        #On compte le nombre de commentaires
        quali = Popen(["cat", "./Rendus_eleves/eleves_bis/" + eleve], stdout = PIPE, encoding = "utf8")
        quali.wait()

        tmp = 0
        for ligne in quali.stdout:
            if "/*" in ligne:
                tmp = 1
            if "*/" in ligne:
                qualite += tmp
                tmp = 0

            if tmp != 0:
                tmp += 1

         #On ecris les resultats dan le fichier csv
        ligne = str(eleve[:-2]) + "," + str(compilation) + "," + str(warning) + "," + str(tests) + "," + str(qualite)

        fich.write(ligne + '\n')

        #On supprime l'executable
        if(compilation == 1):
            call(["rm", eleve[:-2]])
    fich.close()