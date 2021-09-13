#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/un.h>
#include <unistd.h>
#include <errno.h>


typedef struct sockaddr_un socket_address;
#define SOCK_PATH "/tmp/drkp.socket"
#define BUFF_SIZE 1024 * 4

int main(int argc, char** argv) {
    char* path = NULL;
    socket_address addr;
    socket_address client_address;
    char buff[BUFF_SIZE];
    
    int fd = socket(AF_UNIX, SOCK_SEQPACKET, 0);
    if (fd == -1) {
        printf("%s\n", "Error creating socket");
        return 1;
    }
    printf("%s\n", "Socket successfully created");

    memset(&addr, 0, sizeof(socket_address));
    memset(&client_address, 0, sizeof(socket_address));
    memset(&buff, 0, BUFF_SIZE);
    addr.sun_family = AF_UNIX;
    strcpy(addr.sun_path, SOCK_PATH);
    unsigned int len = sizeof(addr);
    int status = unlink(SOCK_PATH);
    if (status != 0) {
        printf("%s [%s]\n", "Uanble to delete ", SOCK_PATH);
    }
    status = bind(fd, (struct sockaddr *) &addr, len);
    if (status != 0) {
        printf("%s [%s]", "Could not bind socket to path", SOCK_PATH);
        close(fd);
        exit(1);
    }

    status = listen(fd, 10);

    if (status != 0) {
        printf("%s", "Could not start listening on socket");
        close(fd);
        exit(1);
    }

    int client_socket = accept(fd, (struct sockaddr *) &client_address, &len);
    if (client_socket < 0) {
        printf("%s", "Could not accept connections");
        close(fd);
        close(client_socket);
        exit(1);
    }

    int bytes_recived = recvfrom(fd, buff, BUFF_SIZE, 0, (struct sockaddr *) &addr, &len);
    if (bytes_recived < 0) {
        printf("%s", "Data did not recived");
        printf("%s%d\n", "RECVFROM ERROR = ", errno);
        close(fd);
        exit(1);
    }

    for (int i = 0; i < bytes_recived; i++) {
        if (i % 8 == 0) {
            printf("\n%02x ", i);
        }
        printf("%02x ", buff[i]);
    }
    return 0;
}