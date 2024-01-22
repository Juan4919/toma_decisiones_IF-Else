llamadas = int(input("Indica el número de minutos que has habllado este mes > "))
print
mensajes = int(input("¿Cuanto sms has enviado este mes? "))
print 
if llamadas > 50 and mensajes > 50:
    coste_llamadas=(llamadas - 50)*0.25
    coste_sms=(mensajes-50)*0.15
    print(f"El coste total de la factura será de {(15.00+coste_llamadas+coste_sms+0.44)*1.05}€")
    print(f"en base a los {llamadas} minutos de llamadas realizadas y a los {mensajes} mensajes enviados,") 
    print(f"junto con los 0.44€ correspondientes a números 911 y el 5% de impuestos por ventas")
elif llamadas <= 50 and mensajes > 50:
    coste_sms=(mensajes-50)*0.15
    print(f"El coste total de la factura será de {(15.00+coste_sms+0.44)*1.05}€")
    print(f"en base a los {llamadas} minutos de llamadas realizadas y a los {mensajes} mensajes enviados,") 
    print(f"junto con los 0.44€ correspondientes a números 911 y el 5% de impuestos por ventas")
elif llamadas > 50 and mensajes <= 50:
    coste_llamadas=(llamadas - 50)*0.25
    print(f"El coste total de la factura será de {(15.00+coste_llamadas+0.44)*1.05}€")
    print(f"en base a los {llamadas} minutos de llamadas realizadas y a los {mensajes} mensajes enviados,") 
    print(f"junto con los 0.44€ correspondientes a números 911 y el 5% de impuestos por ventas")
else: 
    print(f"El coste total de la factura será de {(15.00+0.44)*1.05}€")
    print(f"en base a los {llamadas} minutos de llamadas realizadas y a los {mensajes} mensajes enviados,") 
    print(f"junto con los 0.44€ correspondientes a números 911 y el 5% de impuestos por ventas")
    
    