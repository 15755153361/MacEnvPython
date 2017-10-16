#include <stdio.h>
#include <stdlib.h>

typedef struct BinaryTreeNode{
    struct BinaryTreeNode * pLeft;
    struct BinaryTreeNode * pRight;
    int  m_Value;
}BINARYTREENODE;

void CreateBinaryTree(BINARYTREENODE **pRoot)
{
    int m = 0;
    printf("Please Input a None Zero Value : ");
    scanf("%d",&m);
    if(0 == m)
    {
	pRoot = NULL;
    	return;
    }
    else
    {
	*pRoot = (BINARYTREENODE *)malloc(sizeof(BINARYTREENODE));
	(*pRoot)->m_Value = m;
	CreateBinaryTree(&((*pRoot)->pLeft));
	CreateBinaryTree(&((*pRoot)->pRight));
    }
}

void ShowBinary(BINARYTREENODE * pRoot)
{
    if(NULL!=pRoot)
    {
    	printf("%d\n",pRoot->m_Value);
    }
}

void PreOrder(BINARYTREENODE * pRoot)
{	
    if(NULL!=pRoot)
    {
	ShowBinary(pRoot);
    	PreOrder(pRoot->pLeft);
	PreOrder(pRoot->pRight);
    }
}

int main(int argc , char *argv[])
{
    int value = 0;
    BINARYTREENODE * pRoot = NULL;
    CreateBinaryTree(&pRoot); 
    printf("The Value is %d\n",pRoot->m_Value);
    printf("The Pre Order of Binary Tree : \n");
    PreOrder(pRoot);    
}
