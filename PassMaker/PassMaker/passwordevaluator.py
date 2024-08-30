#!/usr/bin/env Python3
from zxcvbn import zxcvbn



class PasswordEvaluator:
    """ Password Evaluator se encarga de evaluar las contraseñas """
    @staticmethod
    def evaluate(password:str):
        """
        Este metodo evalua si la contraseña  es segura o no
        """
        scores = {
            "0" : "Contraseña muy debil",
            "1" : "Contraseña debil",
            "2" : "Contraseña intermedia",
            "3" : "Contraseña fuerte",
            "4" : "Contraseña muy fuerte"
        }

        results = zxcvbn(password)
        score_password = str(results['score'])
        if score_password in scores.keys():
            return scores[score_password]
        else:
            raise(f"\n[!] Error")
    @staticmethod
    def spc(password:str)->dict:
        """
        Este metodo muestra en formato diccionario datos importantes de zxcvbn 
            args:
                password(str): Contraseña 
            return:
                retorna un diccionario que muestra la fortaleza,feedback y el tiempo de decifrarla por fuerza bruta
        """
        resutls = zxcvbn(password)
        strengths = resutls['score']
        feedback = resutls['feedback']['suggestions']
        cracked_time_display = resutls['crack_times_display']['offline_fast_hashing_1e10_per_second']
        
        #si no hay feedback
        if feedback == []:
            feedback = ['No hay feedback']

        return {
            "Fortaleza":f"{strengths}",
            "Feedback": f"{feedback}",
            "cracked" : f"{cracked_time_display}"
        }
    
