import string

# Definir as variáveis
default_host = AdminConfig.getid('/VirtualHost:default_host/')
new_ports = ["5000","6000","7000","8000"]

# Criar novo HostAlias com um hostname * e as portas especificadas
host_alias_attrs = []
for port in new_ports:
    host_alias_attrs.append(['port', port])
    host_alias_attrs.append(['hostname', '*'])
    new_host_alias = AdminConfig.create('HostAlias', default_host, host_alias_attrs)

# Salvar as mudanças na configuração
AdminConfig.save()

print("New HostAlias created for default_host with ports", new_ports)
