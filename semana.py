import datetime
from datetime import date
import calendar


#4  é igual a abril
diasemana = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado','Domingo']
def dia_da_semana(mes, dia_da_semana):
    l = []
    dia = 1
    hj = date.today()
    quantos_dias_tem_um_mes = calendar.mdays[mes]
    for x in range(quantos_dias_tem_um_mes):
           
        data1 = datetime.date(day=dia, month=mes, year=hj.year)
        if diasemana[data1.weekday()]==dia_da_semana:
            #print('Mês: ',mes, dia, diasemana[data1.weekday()])
            res = datetime.date(year=hj.year, month=mes,day=dia)
            l.append(res)
        dia+=1
    return l         
print(dia_da_semana(1,'Domingo'))


hj = date.today()
mes_atual =hj.month
''' gera datas do mês atual até o mês 12 de acordo com a semana indicada '''
for i in range(mes_atual,13): #percorre todos os meses de 1 a 12 sendo janeiro 1             
    for i in dia_da_semana(i,diasemana[0]):#mes e dia da semana no caso 0 será segunda-feira
        print("Agenda(nome=nome_atual, data= ",i, "eletronico=tecnologia)")
print('dados.save()')

