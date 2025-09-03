from datetime import date

class FuncionesPrograma:
    #Creo diccionarios para dia y mes
    NUMEROS_EN_TEXTO = {
        1: "uno", 2: "dos", 3: "tres", 4: "cuatro", 5: "cinco", 6: "seis", 7: "siete", 8: "ocho", 9: "nueve",
        10: "diez", 11: "once", 12: "doce", 13: "trece", 14: "catorce", 15: "quince", 16: "dieciséis", 17: "diecisiete",
        18: "dieciocho", 19: "diecinueve", 20: "veinte", 21: "veintiuno", 22: "veintidós", 23: "veintitrés", 24: "veinticuatro",
        25: "veinticinco", 26: "veintiséis", 27: "veintisiete", 28: "veintiocho", 29: "veintinueve", 30: "treinta", 31: "treinta y uno"
    }
    MESES_EN_TEXTO = {
        1: "enero", 2: "febrero", 3: "marzo", 4: "abril", 5: "mayo", 6: "junio", 7: "julio", 8: "agosto",
        9: "septiembre", 10: "octubre", 11: "noviembre", 12: "diciembre"
    }

    @staticmethod
    def añoConvertirString(n):
        unidades = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
        especiales = {
            10: "diez", 11: "once", 12: "doce", 13: "trece", 14: "catorce", 15: "quince",
            16: "dieciséis", 17: "diecisiete", 18: "dieciocho", 19: "diecinueve"
        }
        decenas = ["", "", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
        centenas = ["", "cien", "doscientos", "trescientos", "cuatrocientos", "quinientos",
                    "seiscientos", "setecientos", "ochocientos", "novecientos"]
        if not (1000 <= n <= 2099):
            raise ValueError("Solo se admiten años entre 1000 y 2099")

        mil = n // 1000
        resto = n % 1000
        texto = "mil" if mil == 1 else unidades[mil] + " mil"

        if resto == 0:
            return texto

        c = resto // 100
        decena_unidad = resto % 100
        d = decena_unidad // 10
        u = decena_unidad % 10

        if decena_unidad in especiales:
            texto += " " + centenas[c] + " " + especiales[decena_unidad]
        elif decena_unidad < 30:
            texto += " " + centenas[c] + " " + decenas[d] + (unidades[u] if u else "")
        else:
            texto += " " + centenas[c] + " " + decenas[d] + (" y " + unidades[u] if u else "")

        return texto.strip()

    # 🔹 Nuevo método: retorna un objeto date
    @staticmethod
    def getFechaDate(dia, mes, año):
        return date(año, mes, dia)

    @staticmethod
    def getFechaString(dia, mes, año):
        dia = FuncionesPrograma.NUMEROS_EN_TEXTO.get(dia, "día inválido")
        mes = FuncionesPrograma.MESES_EN_TEXTO.get(mes, "mes inválido")
        return dia + " de " + mes + " de " + FuncionesPrograma.añoConvertirString(año)


class Principal:
    def main(self):
        dia = int(input("Ingrese el dia: "))
        while dia <= 0 or dia > 31:
            print("INGRESE UN NUMERO VALIDO")
            dia = int(input("Ingrese el dia: "))
        mes = int(input("Ingrese un mes: "))
        while mes <= 0 or mes > 12:
            print("INGRESE UN NUMERO VALIDO")
            mes = int(input("Ingrese un mes: "))
        año = int(input("Ingrese un año entre 1000 y 2099: "))
        while año < 1000 or año > 2099:
            print("INGRESE UN NUMERO VALIDO")
            año = int(input("Ingrese un año entre 1000 y 2099: "))
    
        # Usamos ambos métodos
        print("Fecha en texto:", FuncionesPrograma.getFechaString(dia, mes, año))
        print("Fecha en objeto date:", FuncionesPrograma.getFechaDate(dia, mes, año))


Iniciar = Principal()
Iniciar.main()