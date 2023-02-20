# Importa as bibliotecas necessárias
import sys
import java
import os
import subprocess

print ("Criacao dos Clusters do ambiente iniciou...\n")

# Define o nome dos clusters a serem criados
stopManager = "/opt/IBM/WebSphere/Dmgr/bin/stopManager.sh"
startManager = "/opt/IBM/WebSphere/Dmgr/bin/startManager.sh"
createclusterNames = ['ClusterName1','ClusterName2','ClusterName3']


# Loop atravéz da lista de clusters para criação de um novo cluster

for createclusterName in createclusterNames:
    print ("Criando o cluster"  + createclusterName + "\n")
    cluster = AdminClusterManagement.createClusterWithoutMember(createclusterName)
    print ("Cluster " + createclusterName + " criado com sucesso. \n")
    
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

print ("--- Processo de criacao dos Clusters do ambiente finalizado! ---")