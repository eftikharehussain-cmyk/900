n, m = map(int, input().split())
ip_name = {}
for _ in range(n):
    name, ip = input().split()
    ip_name[ip] = name
for _ in range(m):
    command, ip = input().split()
    ip_del = ip[:-1]
    print(command,ip, "#"+ip_name[ip_del])
print(ip_name)