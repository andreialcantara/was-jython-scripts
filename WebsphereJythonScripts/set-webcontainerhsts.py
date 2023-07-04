##################################################
## Description: Seta hsts no webcontainer de todas
## as jvms do cluster 
##################################################
## Version: 1.0.1
##################################################

# Carrega a biblioteca wsadmninlib
import sys
sys.path.append("/opt/IBM/WebSphere/Dmgr/bin/wsadminlib")
from wsadminlib import *

# Nome e valores das propriedades que serão incluídas na custom properties do webcontainer
propname = "com.ibm.ws.webcontainer.addStrictTransportSecurityHeader"
propvalue = "max-age=31536000; includeSubDomains"

# Obtem todos os nodes do cluster
nodes = listNodes()

# Obtem todos os servidores de aplicações do cluster (jvms)
servers = listAllAppServers()
servernames = [server[1] for server in servers]

# Cria um conjunto para armazenar as combinações únicas de node e server
unique_combinations = set()

# Itera a lista de nodes e jvms, que irão receber a custom property no webcontainer
for nodename in nodes:
    for servername in servernames:
        unique_combinations.add((nodename, servername))

# Itera sobre as combinações únicas e configura a custom property
for nodename, servername in unique_combinations:
    try:
        setWebContainerCustomProperty(nodename, servername, propname, propvalue)
        print("Custom Property criada com sucesso no webcontainer da jvm " + servername + " no node " + nodename)
    except:
        print("Algo deu errado, não foi possível criar a custom property no webcontainer da jvm " + servername + " no node " + nodename)

# Salva as configurações
AdminConfig.save()

# Imprime uma mensagem de confirmação
print("Execução do script finalizada!")
