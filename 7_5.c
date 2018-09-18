#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
	srand(time(NULL));
	float y,temp;
	
	FILE *fptr;   
	fptr=fopen("s.dat","w");
	
	for(int i=0;i<1000000;i++)
	{
		temp=0;
		for(int j=0;j<12;j++)
		{
			y=rand();
			y=y/RAND_MAX;    
			temp=y+temp;
		}
		
		fprintf(fptr,"%f\n",temp-6);
	}
	
	fclose(fptr); 
return 0;	
}