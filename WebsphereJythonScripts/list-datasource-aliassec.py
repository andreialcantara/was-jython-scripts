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
