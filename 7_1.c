#include <stdio.h>
#include <time.h>
#include <stdlib.h>
int main()
{
	srand(time(NULL));
	float y;
	
	FILE *fptr;
	fptr=fopen("uni.dat","w");
	
	int i;
	for(i=0;i<1000000;i++)
	{
		y=rand();
		y=y/RAND_MAX;            
		fprintf(fptr,"%f\n",y);
	}
	fclose(fptr);
}