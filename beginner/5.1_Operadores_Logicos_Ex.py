# Disparo de alarme

porta = "open"
janela = "closed"

alarme = (porta == 'open') or (janela == 'open')

msg = 'Alarme Disparado? ' + str(alarme)

print(msg)