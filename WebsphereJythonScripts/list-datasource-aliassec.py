#!/usr/bin/python
# -*- coding: utf-8 -*-
# Lista todos os datasources configurados no nivel da celula do cluster websphere e exibe o alias de segurança que armazena as credencias de conexcão do datasource.
import re

cells = AdminConfig.list('Cell').split()
output = ""
for cell in cells:
    cellName = AdminConfig.showAttribute(cell, 'name')
    output += "Cell: {}\n".format(cellName)
    datasources = AdminConfig.list('DataSource', cell).splitlines()
    for ds in datasources:
        dsName = AdminConfig.showAttribute(ds, 'name')
        securityAlias = AdminConfig.showAttribute(ds, 'authDataAlias')
        if securityAlias is None or securityAlias.strip() == "":
            securityAlias = "Nenhum alias de seguranca especificado"
        
        output += "  DataSource: {}\n".format(dsName)
        output += "  Alias de seguranca: {}\n\n".format(securityAlias)  # Adiciona uma quebra de linha aqui
    output += "\n"

# Tratar a saída final após o loop
output = re.sub(r'[^\x00-\x7F]', '', output)
print(output)
##################################################################################################################################
# Lista todos os datasources configurados no nivel da celula do cluster websphere e exibe o alias de segurança que armazena as credencias de conexcão do datasource.
# Gera a saida em formato csv
#!/usr/bin/python
# -*- coding: utf-8 -*-
#import re

# Lista todos os datasources configurados no nivel da celula do cluster websphere e exibe o alias de segurança que armazena as credencias de conexcão do datasource.

#cells = AdminConfig.list('Cell').split()
#output = []

#for cell in cells:
#    cellName = AdminConfig.showAttribute(cell, 'name')
#    datasources = AdminConfig.list('DataSource', cell).splitlines()
#    for ds in datasources:
#        dsName = AdminConfig.showAttribute(ds, 'name')
#        securityAlias = AdminConfig.showAttribute(ds, 'authDataAlias')
#        if securityAlias is None or securityAlias.strip() == "":
#            securityAlias = "Nenhum alias de seguranca especificado"
#        
#        output.append([cellName, dsName, securityAlias])
#
# Imprimir os dados no formato CSV
#print("Cell,Datasource,Alias de Seguranca")
#for row in output:
#    print(','.join(row))
