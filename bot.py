import paramiko

def start_connection():
    u_name = 'root'
    pswd = '@Tharuka10300a'
    port = 22
    r_ip = '128.199.134.79'
    

    myconn = paramiko.SSHClient()
    myconn.set_missing_host_key_policy(paramiko.AutoAddPolicy())


    session = myconn.connect(r_ip, username =u_name, password=pswd, port=port)

    remote_cmd = 'ls'
    (stdin, stdout, stderr) = myconn.exec_command(remote_cmd)
    print("{}".format(stdout.read()))
    print("{}".format(type(myconn)))
    print("Options available to deal with the connectios are many like\n{}".format(dir(myconn)))
    myconn.close()


if name == 'main':
    start_connection()
