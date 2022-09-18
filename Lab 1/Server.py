import socket
import threading
import constants
import os
import datetime
import time
import wsgiref.handlers


server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = constants.IP_SERVER


def main():
    print("***********************************")
    print("Server is running...")
    print("Dir IP:",server_address )
    print("Port:", constants.PORT)
    server_execution()


def handler_client_connection(client_connection,client_address):
    print(f'\nNew incomming connection is coming from: {client_address[0]}:{client_address[1]}')
    data_recevived = client_connection.recv(constants.RECV_BUFFER_SIZE)
    remote_string = str(data_recevived.decode(constants.ENCONDING_FORMAT))
    remote_string = remote_string.replace("\r", "")
    remote_command = remote_string.split('\n')
    while('' in remote_command) :
        remote_command.remove('')
    method, myfile, httpv = remote_command[0].split(' ')
    print('Method:', method)
    print('URI:', myfile)
    print('HTTP version:', httpv)
    myfile = myfile.lstrip('/')
    myfile = constants.DOCUMENT_ROOT + myfile
    if myfile == constants.DOCUMENT_ROOT:
        myfile = constants.DOCUMENT_ROOT + 'index.html'
    del remote_command[0]
    decode_headers_request(remote_command)

    date_header = str(wsgiref.handlers.format_date_time(time.mktime(datetime.datetime.now().timetuple())))
    server_header = constants.ELASTIC_IP + '/' + str(constants.PORT)

    if method == 'GET':
        exists = os.path.exists(myfile)       
        if (exists):
            header = 'HTTP/0.9 200 OK\r\n'
            header += 'Date: ' + date_header + '\r\n'
            header += 'Server:' + server_header + '\r\n'
            f_type = file_type(myfile)
            header += 'Content-Type: ' + f_type + '\r\n'
            header += '\r\n'
            header = header.encode(constants.ENCONDING_FORMAT)
            client_connection.sendall(header)

            f = open(myfile, 'rb')
            l = f.read(constants.RECV_BUFFER_SIZE)
            while (l):
                client_connection.send(l)
                l = f.read(constants.RECV_BUFFER_SIZE)
            f.close()
            
            decode_headers_response(date_header, server_header, f_type)
        else:
            header = 'HTTP/0.9 404 Not Found\r\n'
            header += 'Date: ' + date_header + '\r\n'
            header += 'Server:' + server_header + '\r\n'
            header += '\r\n'
            header = header.encode(constants.ENCONDING_FORMAT)
            client_connection.sendall(header)
            decode_headers_response(date_header, server_header)
    else:
        header = 'HTTP/0.9 405 Method Not Allowed\r\n'
        header += 'Date: ' + date_header + '\r\n'
        header += 'Server:' + server_header + '\r\n'
        header += '\r\n'
        header = header.encode(constants.ENCONDING_FORMAT)
        client_connection.sendall(header)
        decode_headers_response(date_header, server_header)
    print(f'Now, client {client_address[0]}:{client_address[1]} is disconnected...')
    client_connection.close()


def server_execution():
    tuple_connection = (server_address,constants.PORT)
    server_socket.bind(tuple_connection)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print ('Socket is bind to address and port...')
    server_socket.listen(5)
    print('Socket is listening...')
    while True:
        client_connection, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handler_client_connection, args=(client_connection,client_address))
        client_thread.start()
    print('Socket is closed...')
    server_socket.close()

    
def decode_headers_response(date_header, server_header, filetype_header = 0):
    print('DECODED HEADERS - RESPONSE:')
    print('The date of the response is', date_header)
    print('The server of the response is', server_header)
    if filetype_header != 0:
        print('The MIME type of the file of the response is', filetype_header)


def decode_headers_request(headers):
    unknown =[]
    for i in range(len(headers)):
        headers[i] = headers[i].split(': ')
    print('DECODED HEADERS - REQUEST:')
    for i in range(len(headers)):
        if headers[i][0] == 'User-Agent':
            print("The user agent is", headers[i][1])
        elif headers[i][0] == 'Keep-Alive':
            print("Keep alive the connection:", headers[i][1])
        elif headers[i][0] == 'Host':
            print("The host is", headers[i][1])
        elif headers[i][0] == 'Date':
            print('The date of the request is', headers[i][1])
        else:
            unknown.append(headers[i][0])
    print('Headers desconocidos:', ', '.join(unknown))


def file_type (myfile):
    if(myfile.endswith('.jpg')):
        return 'image/jpeg'
    elif(myfile.endswith('.jpeg')):
        return 'image/jpeg'
    elif(myfile.endswith('.png')):
        return 'image/png'
    elif(myfile.endswith('.css')):
        return 'text/css'
    elif(myfile.endswith('.csv')):
        return 'text/csv'
    elif(myfile.endswith('.pdf')):
        return 'application/pdf'
    elif(myfile.endswith('.doc')):
        return 'application/msword'
    elif(myfile.endswith('.html')):
        return 'text/html'
    elif(myfile.endswith('.htm')):
        return 'text/html'
    elif(myfile.endswith('.json')):
        return 'application/json'
    elif(myfile.endswith('.txt')):
        return 'text/plain'
    else:
        return 'application/octet-stream'


if __name__ == "__main__":
    main()
