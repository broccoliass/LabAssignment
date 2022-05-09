#include <stdio.h> 
#include <stdlib.h> 
#include <sys/types.h> 
#include <sys/wait.h> 
#include <unistd.h>
#include <errno.h>
#include <signal.h>
 
int number,i,m=0,flag=0; 

void sigint_handler (int sig);
char s[200];

int getPrime() {
// use PPID and PID as the seed 
srand(getpid() + getppid()); 
scanf("%d",&number);

if(fgets(s, 200, stdin) == NULL)
		perror("gets");

return number;
}

void sigint_handler(int sig){
	printf("\nYou should enter a number!\n");
}

int main(void) {

	
if(signal(SIGINT, sigint_handler) == SIG_ERR){
	perror("signal");
	exit(1);
}

int fd[2]; 
pipe(fd);
pid_t pid = fork();

if (pid > 0) { //parent
close(0); 
close(fd[1]); 
dup(fd[0]);

int secretNumber; 
size_t readBytes = read(fd[0], &secretNumber, sizeof(secretNumber));

printf ("Waiting for Number... \n"); 
wait(NULL); 

m=secretNumber/2;    
for(i=2;i<=m;i++)    
{    
if(secretNumber%i==0)    
{    
printf("%d is not prime\n", secretNumber);    
flag=1;    
break;    
}    
}
if(flag==0)    
printf("%d is prime\n", secretNumber);  


//printf("Bytes read: %d\n", readBytes);
//printf("PIN: %d\n", secretNumber);


}

else if (pid == 0) { //child

close(1); 
close(fd[0]); 
dup(fd[1]);

int number = getPrime(); 
write(fd[1], &number, sizeof(number)); 

exit(EXIT_SUCCESS);
}
return EXIT_SUCCESS;
}
