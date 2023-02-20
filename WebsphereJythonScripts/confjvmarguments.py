# Importa as bibliotecas necessárias
import sys
import java
import os
import subprocess

print ("Iniciando configuração dos argumentos das jvms, Aguarde... \n") 

# Define as jvms que terão os argumentos configurados.
stopManager = "/opt/IBM/WebSphere/Dmgr/bin/stopManager.sh"
startManager = "/opt/IBM/WebSphere/Dmgr/bin/startManager.sh"
nodename = ['webspherelabNode01','webspherelab2Node01']
jvmsname = ['server1','server2','server3'] 	

for node in nodename:
 # Loop através da lista de nodes
 for jvm in jvmsname:
	# Loop através da lista de jvms
    print ("Configurando argumentos da jvm "  + jvm + " no node " + node + "\n")

    servers = AdminTask.setJVMProperties('[-serverName ' +  jvm + ' -nodeName  ' + node + '  -verboseModeClass false -verboseModeGarbageCollection false -verboseModeJNI false -initialHeapSize 1024 -maximumHeapSize 1024 -runHProf false -hprofArguments  -debugMode false -debugArgs "-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=7777" -genericJvmArguments "-Dcom.sun.jndi.ldap.connect.pool.timeout=300000 -Xgcpolicy:gencon -Xmn1024m -javaagent:/usr/WebSphere/AppServer/wily/AgentNoRedefNoRetrans.jar -Dcom.wily.introscope.agentProfile=/usr/WebSphere/AppServer/wily/core/config/IntroscopeAgent.websphere.NoRedef.profile -Dcom.wily.autoprobe.logSizeInKB=10000 -Xshareclasses:none" -executableJarFileName  -disableJIT false]')

    print ("Argumentos da jvm "  + jvm + " no node " + node + "configurados! \n")

# Salva as mudanças
AdminConfig.save()
#Sincroniza nodes ativos
print("--- Sincronizando os nodes ativos --- \n")
try:
 AdminNodeManagement.syncActiveNodes()
 print("Nodes ativos sincronizados... \n")
except syncActivenodes:
    print("O sincronismo dos nodes ativos falhou! \n")

#Desconecta do wsadmin.sh
quit

# Reinicia o DMGR
print("--- Reinicializando a DMGR --- \n")
try:
    print("--- Parando o DMGR --- \n")
    subprocess.call(['bash', stopManager,'-quiet'])
except stopDmgr:
    print("Não foi possível parar a Dmgr! ")

try:
    print("--- Iniciando o DMGR --- \n")
    subprocess.call(['bash', startManager,'-quiet'])
    print("--- DMGR reiniciado com sucesso! --- \n")
except startDmgr:
    print("Inicializacao da Dmgr falhou!")

print ("--- Processo de configuração dos argumentos das Jvms finalizado! ---")