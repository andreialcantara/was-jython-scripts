##################################################
## Description: Efetua a criação dos webservers 
##################################################
## Version: 1.0.1
##################################################

# Carrega a biblioteca wsadmninlib
import sys
sys.path.append("/opt/IBM/WebSphere/Dmgr/bin/wsadminlib")
from wsadminlib import *

variables = [
    {"servername": "webserver1",
     "webPort": "10443",
     "webInstallRoot": "/opt/IBM/HTTPServer",
     "pluginInstallRoot": "/opt/IBM/Plugins",
     "configurationFile": "/opt/IBM/HTTPServer/conf/httpd.conf",
     "retryInterval": "3"}
]

# Adiciona os nodes do ambiente a variavel
nodes = listNodes()
for nodename in nodes:
    for variable in variables:
      try:
          creationString = '[-name %s -templateName IHS -serverConfig [-webPort %s -webInstallRoot %s -pluginInstallRoot %s -configurationFile %s]]' % (variable["servername"], variable["webPort"], variable["webInstallRoot"], variable["pluginInstallRoot"], variable["configurationFile"])
          AdminTask.createWebServer(nodename, creationString)
          print ("Criado o " + variable["servername"] + " com a porta " + variable["webPort"] + " no " + nodename)
      except:
          print ("Algo deu errado, não foi possível criar o " + variable["servername"] + " no " + nodename)

#Configura o valor do plugin Retry interval
for nodename in nodes:
    for variable in variables:
      try:
         webserver = getServerByNodeAndName(nodename, variable["servername"])
         plgClusterProps = AdminConfig.list('PluginServerClusterProperties', webserver)
         AdminConfig.modify(plgClusterProps, [['RetryInterval', variable["retryInterval"] ]])
         print ("Configurado no " + variable["servername"] + " no " + nodename + " o plugin Retry Interval de " + variable["retryInterval"])
      except:
         print ("Algo deu erro na configuração do Plugin Retry Interval no " + variable["servername"] + " no " + nodename )
    
#Salva as configurações
AdminConfig.save()
# Imprime uma mensagem de confirmação
print ("Execução do script finalizada!")        