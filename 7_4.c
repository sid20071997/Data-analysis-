#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main()
{
	
	int b;
	float r;

	srand(time(NULL));

	//printf("%d",RAND_MAX);

	for (b=11;b>=0;b--){

		r=rand();

		printf("%f\n", r/RAND_MAX);

	}
	return 0;
}