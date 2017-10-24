#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void my_memcpy(char *dest,const char * sour,int len)
{
	char * dst = NULL;
	const char * src = NULL;
	if (dest>sour+len || dest<sour)
	{
		printf("内存不重叠情况.....\n");
		dst = dest;
		src = sour;
		while (len)
		{
			*dst = *src;
			dst++;
			src++;
			len--;
		}
	}
	else
	{
		printf("内存重叠情况.....\n");
		dst = dest + len-1;
		src = sour + len-1;
		while (len)
		{
			*dst = *src;
			dst--;
			src--;
			len--;
		}
	}
	return;
}


int main()
{
	/* 内存不重叠情况*/
	char *source = "didi_Test";
	int len = strlen(source);
	printf("len = %d\n",len);
	char *dest = NULL;
	dest = (char *)malloc(sizeof(char)*(len+1));
	printf("source = %p , dest = %p\n",source,dest);
	memset(dest,0,len+1);
	my_memcpy(dest,source,len+1);
	printf("%s\n",dest);

	printf("-----------------------------------------------------------\n");
	/* 内存重叠情况*/
	char comm_src[50] = "This is memcpy test";
	char *comm_dst = comm_src+10;
	printf("comm_str = %p , comm_dst = %p\n",comm_src,comm_dst);
	printf("comm_dst - comm_str = %ld\n",comm_dst - comm_src);
	int comm_len = strlen(comm_src);
	printf("len = %d\n",comm_len);
	my_memcpy(comm_dst,comm_src,comm_len+1);
	printf("%s\n",comm_dst);
	printf("%s\n",comm_src);
}

