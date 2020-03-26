from subprocess import *
from os import listdir

if __name__ == "__main__":

    lst_eleves = listdir('./Rendus_eleves/eleves_bis')

    for eleve in lst_eleves:
        erreur = 0
        warning = 0
        tests = 0
        print(eleve)
        s = Popen(["gcc", "-ansi", "-Wall", "-o", eleve[:-2], "./Rendus_eleves/eleves_bis/" + eleve], stdout = PIPE, stderr = PIPE, encoding = "utf8")
        s.wait()
        if s.returncode != 0:
            erreur = 1
        for ligne in s.stderr:
            if 'warning' in ligne:
                warning += 1

        print("erreur :", erreur, "\nwarning :", warning)

        if erreur == 0:
            out = call(["./" + eleve[:-2], "0", "0"], stdout = sortie, encoding = "utf8")
            if(sortie == "La somme de 0 et 0 vaut 0\n"):
                tests += 1

            out = call(["./" + eleve[:-2], "1", "0"], encoding = "utf8")
            if(out == "La somme de 1 et 0 vaut 1\n"):
                tests += 1

        print("test : ", tests)
        if(erreur == 0):
            call(["rm", eleve[:-2]])