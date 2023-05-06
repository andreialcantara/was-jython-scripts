# Define as variáveis de ambiente a serem adicionadas
variables = [
    {"name": "$ORACLE_DRIVER_PATH", "value": "/WebSphere/jdbcdriver/oracle"},
    {"name": "$DB2_DRIVER_PATH", "value": "/WebSphere/jdbcdriver/db2"},
    {"name": "$POSTGRES_DRIVER_PATH", "value": "/WebSphere/jdbcdriver/postgres"}
]

# Obtém a referência para o objeto "VariableMap" do escopo da Cell
cell_name = AdminControl.getCell()
cell_scope = AdminConfig.getid('/Cell:' + cell_name + '/')
variable_maps = AdminConfig.list('VariableMap', cell_scope)
variable_map_id = None

# Verifica se o VariableMap já existe, caso não exista, cria um novo
if len(variable_maps) == 0:
    print "VariableMap não encontrado, criando um novo..."
    variable_map_id = AdminConfig.create('VariableMap', cell_scope, [])
else:
    # Seleciona o primeiro objeto com apenas uma barra antes do caractere "|"
    for variable_map in variable_maps.splitlines():
        if variable_map.count("/") == 1:
            variable_map_id = variable_map
            break

    # Caso não encontre um objeto com apenas uma barra, seleciona o primeiro objeto
    if not variable_map_id:
        variable_map_id = variable_maps[0]

# Adiciona as entradas das variáveis de ambiente ao objeto "VariableMap"
for variable in variables:
    variable_entry = '[[symbolicName "%s"] [description ""] [value "%s"]]' % (variable["name"], variable["value"])
    AdminConfig.create('VariableSubstitutionEntry', variable_map_id, variable_entry)

# Salva as alterações na configuração da célula
AdminConfig.save()

# Imprime uma mensagem de confirmação
print "Variáveis de ambiente criadas com sucesso!"