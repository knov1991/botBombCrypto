#pip install pymysql
import pymysql

def conexaoBanco():
    HOST='localhost'
    DB='bomb_crypto'
    USER='root'
    PASSWORD='root'
    try:
        con = pymysql.connect(host=HOST, database=DB, user=USER, password=PASSWORD)
    except:
        return -1
    return con

def verificaLogin(email,password):
    try:
        con = conexaoBanco()
        cursor = con.cursor()
        sql = "select * from usuarios where email = '"+email+"' and password = '"+password+"';"
        cursor.execute(sql)
        resultado = cursor.fetchone()
        if(resultado):
            idUsuario = resultado[0] # idUsuario
            qtdContas = resultado[3] # numero de contas
            hwid = resultado[4] #hwid // MAC-ADDRESS
            if(resultado[3] > 0): #Verifica o numero de contas permitidas // se for maior que 0 permite conexão
                return [idUsuario, int(qtdContas), hwid]
            else:
                print('Acesso Negado')
                return -1
        else:
            print('Acesso Negado')
            return -1
    except:
        print('erro')
        return -1

def novoPC(hwid,idUsuario):
    try:
        con = conexaoBanco()
        cursor = con.cursor()
        print('aqui')
        sql = "update usuarios set hwid = '"+hwid+"' where idUsuario = '"+str(idUsuario)+"';"
        print('aqui 2')
        cursor.execute(sql)
        con.commit()
    except:
        print('Erro ao acessar o banco de dados')
