#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <sys/wait.h>
#include <sys/types.h>

char names[5][40]; 
int i; 

void askName(){
  for( i = 1 ; i < 5; i++ ) { 
    printf( "Enter name : " ); 
    fgets( names[i], 40, stdin ); 
  }
}

void displayName(){
      printf( "\nList of names:\n" ); 
  for( i = 1; i < 5; i++ ) 
    printf( "%s", names[i] ); 
}

int main(void){
            pid_t pid = fork();
                if(pid == 0){
                    askName();
                    displayName();
                    exit(0);
                }

                else{
                    printf("Enter 4 names:\n");
                    printf("Waiting for child processes to finish...\n");
                    wait(NULL);
                    printf("\nJob is Done.\n");
                }
        return EXIT_SUCCESS;
}
