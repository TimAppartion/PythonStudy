import paramiko
def serverConnect():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 第一次连接时会提示是否继续进行远程连接，选择yes

    # 连接远程主机
    ssh.connect(hostname='39.108.224.140', port=22, username='root', password='wh2234040')
    return ssh


ssh = serverConnect()
# 执行命令
stdin, stdout, stderr = ssh.exec_command('/root/testdb/test.json')
res_list = stdout.readlines()
print(res_list)
# 关闭连接
ssh.close()
