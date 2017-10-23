#include <stdio.h>
#include <stdlib.h>
int main()
{
	char str[] = "We Are Happy";
	char new_str[50] = "";
	int len = sizeof(str)-1;
	int count=0;
	int blank = 0;
	for(int i=0;i<len;i++)
	{
		if(str[i] != ' ')
		{
			new_str[count++] = str[i];
		}
		else
		{
			blank++;
			new_str[count++] = '%';
			new_str[count++]= '2';
			new_str[count++] = '0';
		}
	}
	for(int i=0;i<count;i++)
	{
		printf("%c",new_str[i]);
	}
	printf("\n");
	
	char *arr = new char[len+blank*2];
	int new_count = 0;
	for(int i=0;i<len;i++)
	{
		if(str[i] != ' ')
		{
			arr[new_count++] = str[i];
		}
		else
		{
			arr[new_count++] = '%';
			arr[new_count++]= '2';
			arr[new_count++] = '0';
		}
		
	}
	for(int i=0;i<len+blank*2;i++)
	{
		printf("%c",arr[i]);
	}
	printf("\n");
}
