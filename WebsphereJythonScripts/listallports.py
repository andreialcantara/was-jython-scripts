###########################################################
## Description: lista todas as portas:
## dmgr,ihs.nodeagent,jvms do cluster was
## autor: desconhecido da internet  
###########################################################
#           /^\/^\
#         _|__|  O|
#\/     /~     \_/ \
# \____|__________/  \
#        \_______      \
#                `\     \                 \
#                  |     |                  \
#                 /      /                    \
#                /     /                       \
#              /      /                         \ \
#             /     /                            \  \
#           /     /             _----_            \   \
#          /     /           _-~      ~-_         |   |
#         (      (        _-~    _--_    ~-_     _/   | -jython-
#          \      ~-____-~    _-~    ~-_    ~-_-~    /
#            ~-_           _-~          ~-_       _-~   
#               ~--______-~                ~-___-~
###########################################################
## Version: 1.0.1
###########################################################

import java
lineSeparator = java.lang.System.getProperty('line.separator')
def ListPort():
        servers = AdminConfig.list( 'ServerEntry' ).splitlines()
        for server in servers :
            ServerName = server.split( '(', 1 )[ 0 ]
            print "System information: Server Name : " +  ServerName

            NamedEndPoints = AdminConfig.list( "NamedEndPoint" , server).split(lineSeparator)
            for namedEndPoint in NamedEndPoints:
                endPointName = AdminConfig.showAttribute(namedEndPoint, "endPointName" )
                endPoint = AdminConfig.showAttribute(namedEndPoint, "endPoint" )
                host = AdminConfig.showAttribute(endPoint, "host" )
                port = AdminConfig.showAttribute(endPoint, "port" )
                print "System information: Endpoint Name  : " +  endPointName + " Host : " + host + " port : " + port 

ListPort()
