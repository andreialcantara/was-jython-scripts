#Lista portas do WC_defaulthost WC_defaulthost_secure e BOOTSTRAP_ADDRESS
import re
import sys

nodes = ['webspherelabNode01', 'webspherelab2Node01']
servers = ['server1', 'server2']

ports = {}
for node in nodes:
    for server in servers:
        result = AdminTask.listServerPorts(server, '[-nodeName {}]'.format(node)).splitlines()
        for line in result:
            match = re.search(r'\[\[(\w+)\s+\[\[\[host\s+([^]]+)\]\s+\[node\s+([^]]+)\]\s+\[server\s+([^]]+)\]\s+\[port\s+(\d+)', line)
            if match:
                category, host, node, server, port = match.groups()
                if category in ['WC_defaulthost', 'WC_defaulthost_secure', 'BOOTSTRAP_ADDRESS']:
                    key = '{}:{}:{}'.format(node, category, port)
                    ports[key] = '{}:{}:{}:{}'.format(server, node, category, port)

for key in sorted(ports.keys()):
    print(ports[key])