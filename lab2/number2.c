#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <sys/wait.h>

int main(int argc, char **argv){
	int pid; //process ID

	switch (pid=fork()){
	case 0: //fork returns 0 to the child
		printf("I am the child process: pid = %d\n",getpid());
		break;

	default: //fork returns a pid to the parent
		wait(NULL);
		printf("I am the parent process: pid = %d\n", getpid());
		break;

	case -1: //something went wrong
		perror("fork");
		exit(1);
	}
	exit(0);
}
