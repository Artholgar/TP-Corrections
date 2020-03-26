from subprocess import *
from os import listdir

if __name__ == "__main__":

    lst_eleves = listdir('./Rendus_eleves/eleves_bis')

    for eleve in lst_eleves:
        erreur = 0
        warning = 0
        tests = 0
        qualite = 0

        print(eleve)
        compil = Popen(["gcc", "-ansi", "-Wall", "-o", eleve[:-2], "./Rendus_eleves/eleves_bis/" + eleve], stdout = PIPE, stderr = PIPE, encoding = "utf8")
        compil.wait()
        if compil.returncode != 0:
            erreur = 1
        for ligne in compil.stderr:
            if 'warning' in ligne:
                warning += 1

        print("erreur :", erreur, "\nwarning :", warning)

        if erreur == 0:
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

        print("tests : ", tests)

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

        print("qualite : " + str(qualite)) 

        print('\n')
        if(erreur == 0):
            call(["rm", eleve[:-2]])