# Importar as bibliotecas necessárias
import sys
import java

# Definir as propriedades desejadas
heapdump_dir = "/caminho/para/heapdump"
javacore_dir = "/caminho/para/javacore"

# Obter a lista de servidores dos perfis de Application Server
servers = AdminTask.listServers('[-serverType APPLICATION_SERVER]').splitlines()

# Iterar sobre os servidores e configurar as propriedades nas JVMs
for server in servers:
    # Obter a lista de variaveis de ambiente das jvms do servidor atual
    jvms = AdminConfig.list("JavaProcessDef", server).splitlines()

    # Iterar sobre as JVMs e configurar as propriedades
    for jvm in jvms:
        print("Configurando variaveis de ambiente IBM_HEAPDUMPDIR e IBM_JAVACOREDIR para a JVM: " + jvm)

        # Configurar a propriedade IBM_HEAPDUMPDIR
        heapdump_prop = "[[name IBM_HEAPDUMPDIR] [value " + heapdump_dir + "] [description '']]"
        AdminConfig.create("Property", jvm, heapdump_prop)

        # Configurar a propriedade IBM_JAVACOREDIR
        javacore_prop = "[[name IBM_JAVACOREDIR] [value " + javacore_dir + "] [description '']]"
        AdminConfig.create("Property", jvm, javacore_prop)

# Salvar as mudanças na configuração
AdminConfig.save()
print("As propriedades foram configuradas com sucesso para todas as JVMs.")
AdminNodeManagement.syncActiveNodes()
print("Sincronizado os nodes ativos com sucesso!")
