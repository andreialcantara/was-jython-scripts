# Importa as bibliotecas necessárias
import sys
import java
import os
import subprocess

print ("--- Adicionando membros aos Clusters --- \n")

# Define o nome dos clusters, nós e membros a serem criados
stopManager = "/opt/IBM/WebSphere/Dmgr/bin/stopManager.sh"
startManager = "/opt/IBM/WebSphere/Dmgr/bin/startManager.sh"
clustername = "ClusterName2"
nodenames = ['webspherelabNode01','webspherelab2Node01']
membernames = ['server1','server2','server3'] #nome das jvms 

# Loop através da lista de nós
for nodename in nodenames:
 # Loop através da lista de membros
 for membername in membernames:
  print ("Adicionando o membro(jvm) "  + membername + " ao node " + nodename + " no cluster " + clustername + "\n")
  cluster = AdminClusterManagement.createClusterMember(clustername, nodename, membername)
  print ("Membro " + membername + " inserido no cluster " + clustername + " no node " + nodename + " com sucesso! \n")
            

# Salva as mudanças
AdminConfig.save()
#Sincroniza nodes ativos
print("--- Sincronizando os nodes ativos --- \n")
try:
 AdminNodeManagement.syncActiveNodes()
 print("--- Nodes ativos sincronizados --- \n")
except syncActivenodes:
    print("--- O sincronismo dos nodes ativos falhou! --- \n")

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

print ("--- Processo de adicao de membros aos Clusters do ambiente finalizado! ---")
