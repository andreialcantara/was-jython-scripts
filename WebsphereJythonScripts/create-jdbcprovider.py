import os

# obtém o nome da Cell atual
cell_name = AdminControl.getCell()
print("Cell name: " + cell_name)

# define uma lista de dicionários com as informações sobre os JDBC Providers
jdbc_providers = [
    {
        'database_type': 'Oracle',
        'provider_type': 'Oracle JDBC Driver',
        'implementation_type': 'Connection pool data source',
        'provider_name': 'Oracle JDBC Driver',
        'provider_desc': 'Oracle JDBC Driver',
        'classpath': '${ORACLE_JDBC_DRIVER_PATH}/ojdbc8.jar'
    },
    {
        'database_type': 'Oracle',
        'provider_type': 'Oracle JDBC Driver',
        'implementation_type': 'XA data source',
        'provider_name': 'Oracle JDBC Driver (XA)',
        'provider_desc': 'Oracle JDBC Driver (XA)',
        'classpath': '${ORACLE_JDBC_DRIVER_PATH}/ojdbc8.jar'
    }
]

# percorre a lista de dicionários e cria um JDBC Provider para cada item
for provider_info in jdbc_providers:
    provider_id = '[-scope Cell=' + cell_name + ' -databaseType ' + provider_info['database_type'] + ' -providerType "' + provider_info['provider_type'] + '" -implementationType "' + provider_info['implementation_type'] + '" -name "' + provider_info['provider_name'] + '" -description "' + provider_info['provider_desc'] + '" -classpath [' + provider_info['classpath'] + '] -nativePath "" ]'
    AdminTask.createJDBCProvider(provider_id)
    print("JDBC Provider " + provider_info['provider_name'] + " created successfully.")

# Salva as alterações na configuração da célula
AdminConfig.save()

print("All JDBC Providers created successfully.")
