# Obtem o nome da célula atual
cell_name = AdminControl.getCell()

# Obtem o ID da célula usando o nome da célula
cell_id = AdminConfig.getid('/Cell:' + cell_name + '/')

# Define uma lista de bibliotecas compartilhadas a serem criadas
shared_libraries = [
    {'name': 'INFRALOG', 'path': '/WebSphere/was_shared_libraries'},
    {'name': 'MYLIB', 'path': '/WebSphere/my_shared_libraries'}
]

# Loop para criar cada biblioteca compartilhada
for lib in shared_libraries:
    # Define os detalhes da biblioteca compartilhada usando o formato de string para incluir o nome e o caminho da biblioteca
    shared_library = '[[nativePath ""] [name "{}"] [isolatedClassLoader false] [description ""] [classPath "{}"]]'.format(lib['name'], lib['path'])
    
    # Cria a biblioteca compartilhada no escopo da célula
    AdminConfig.create('Library', cell_id, shared_library)
    
    # Exibe uma mensagem de confirmação para cada biblioteca criada
    print('Biblioteca compartilhada {} criada com sucesso.'.format(lib['name']))

# Salva as alterações feitas na configuração do WebSphere
AdminConfig.save()
