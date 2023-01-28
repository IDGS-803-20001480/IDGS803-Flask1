from flask import Flask
from flask import request

app=Flask(__name__)

@app.route("/operasBas",methods=["GET","POST"])
def operasBas():

    if request.method=="POST":
        num1=request.form.get("num1")
        num2=request.form.get("num2")
        opc = request.form.get("fav_language")

        if(opc =="suma"):
            return "La suma es: {}".format(str(int(num1)+int(num2)))
        elif(opc =="resta"):
            return "La resta es: {}".format(str(int(num1)-int(num2)))
        elif(opc =="multi"):
            return "La multiplicacion es: {}".format(str(int(num1)*int(num2))) 
        elif(opc =="division"):
            return "La division es: {}".format(str(int(num1)/int(num2)))  
        #return "La suma es: {}".format(str(int(num1)+int(num2)))
    else:
        return """"
            <form action="/operasBas" method="POST">
            <label>Selecciona la opracion a realizar </label>
            <input type="radio" id="s" name="fav_language" value="suma">
            <label for="html">suma</label><br>
            <input type="radio" id="r" name="fav_language" value="resta">
            <label for="html">resta</label><br>
            <input type="radio" id="m" name="fav_language" value="multi">
            <label for="html">multiplicacion</label><br>
            <input type="radio" id="d" name="fav_language" value="division">
            <label for="html">division</label><br>
            </br>
            <label>N1: </label>
            <input type="text" name="num1"/></br></br>
            <label>N2: </label>
            <input type="text" name="num2"/></br></br>
            <input type="submit" value="calcular"/>
            </form>
        
        """
    return "!!!Hola mundo!!!--cambio"


if __name__=="__main__":
    app.run(debug=True)