##################################################
## Description:Instala WebSphere Enterprise Application
##################################################
## Version: 1.0.0
##################################################

# Carrega a biblioteca wsadmninlib
import sys
sys.path.append("/opt/IBM/WebSphere/Dmgr/bin/wsadminlib")
from wsadminlib import *

# Lista das variáveis servers
servers = [
    {"nodename": "webspherelabNode01", "servername": "IHS"},
    {"nodename": "webspherelab2Node01", "servername": "IHS"},
]

# Lista das variáveis dos clusters
clusternames = ["ClusterName1"]

# Lista das variáveis dos pacotes de aplicação
pacotes = [
    {"appname": "SampleWebApp.war", "filepath": "/tmp/SampleWebApp_war.ear"},
]

# Instala a app SampleWebApp.war
for pacote in pacotes:
    try:
        installApplication(pacote["filepath"], servers, clusternames, None)
        print("Realizado o deploy da app " + pacote["appname"] + " com sucesso!")
    except:
        print("Algo deu errado no deploy!")
#Salva as configurações

AdminConfig.save()

#Sincronizando configuração com os Nodes
syncRetorno = AdminNodeManagement.syncActiveNodes()
if syncRetorno == 1:
    print("Sincronização dos nodes ativos concluída com sucesso!")
else:
    print("Ocorreu um erro durante a sincronização dos nodes ativos.")

# Mensagem de finalização do script
print ("Execução do script finalizada!")