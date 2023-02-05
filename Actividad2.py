from flask import Flask, render_template
from flask import request

app=Flask(__name__)

@app.route("/")
def multiplicar():
    return render_template("Cinepolis.html")

@app.route("/validar",methods=["POST"])
def validar():
    name=request.form.get("txtName")
    compradores=request.form.get("txtCompradores")
    tarjeta=request.form.get("tarjeta")
    boletos=request.form.get("txtBoletos")
    tarjeta=int(request.form.get("tarjeta"))
    boletos=int(request.form.get("txtBoletos"))
    precioBoleto=int(12)
    desc=0
    pago=0
    pagoTotal=0
    vComprador= boletos/int(compradores) 
    if(vComprador > 7):
        return render_template("CinepolisNegacion.html",mensaje="Solamente se puede comprar 7 boletos por persona",name=name)
        #return "<h1></h1>"
    else:
        if(boletos > 5 ):
            des = 15
        elif(boletos >=3):
            if(boletos <=5):
                 des = 10
        else:
            des = 0
    pago = (int(boletos)*precioBoleto)-((int(boletos)*precioBoleto)*(des/100))    
    if(tarjeta == 1):
        pagoTotal= pago - (pago * 0.10)
        #return pagoTotal
        return render_template("CinepolisAceptacion.html",pago=pagoTotal,boletos=boletos,des=des,name=name,tarjeta="10")
    else:
        pagoTotal= pago
        return render_template("CinepolisAceptacion.html",pago=pagoTotal,name=name,des=des,boletos=boletos,tarjeta="No aplica")
    
    #return render_template("resultado.html",n1=n1,n2=n2,res=res)


if __name__=="__main__":
    app.run(debug=True)