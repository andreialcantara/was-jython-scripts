##################################################
## Description: Criação das WebSphere Variables no Cell scope e no Node scope. 
##################################################
## Version: 1.0.1
##################################################

#Carrega a biblioteca wsadmninlib
execfile('/opt/IBM/WebSphere/Dmgr/bin/wsadminlib')
#Valor das variáveis de ambiente que serão inseridas no WebSphere variables
variables = [
    {"name": "$ORACLE_DRIVER_PATH", "value": "/WebSphere/jdbcdriver/oracle"},
    {"name": "$DB2_DRIVER_PATH", "value": "/WebSphere/jdbcdriver/db2"},
    {"name": "$POSTGRES_DRIVER_PATH", "value": "/WebSphere/jdbcdriver/postgres"}
]
# Adiciona variaveis de ambiente no escopo dos Nodes
nodes = listNodes()
for node in nodes:
    for variable in variables:
      try:
        setWebSphereVariable ( variable["name"], variable["value"], nodeName=node, serverName=None, clusterName=None )
        print ("Variável de ambiente " + variable["name"] + " inserida com sucesso no Node " + node) 
      except:
        print ("Algo deu errado, não foi possível adicionar as variáveis de ambiente no escopo dos Nodes!")
    
 
#Adiciona variaveis de ambiente no escopo da Cell
cell = getVariableMap()
for variable in variables:
      try:
        setWebSphereVariable ( variable["name"], variable["value"], nodeName=None, serverName=None, clusterName=None )
        cell_parts = cell.split("|")
        cell_name = cell_parts[0].split("/")[-1]
        print("Variável de ambiente " + variable["name"] + " inserida com sucesso na Cell " +  cell_name)
      except:
        print ("Algo deu errado, não foi possível adicionar as variáveis de ambiente no escopo da Cell!")
  
       
#Salva as configurações
AdminConfig.save()
# Imprime uma mensagem de confirmação
print ("Execução do script finalizada!")
