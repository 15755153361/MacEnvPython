#include <stdlib.h>
#include <stdio.h>

typedef struct  BinaryTreeNode
{
	struct BinaryTreeNode *pLeft;
	struct BinaryTreeNode *pRight;
	int mValue;
}BINARYTREENODE;

void CreateBinaryTree(BINARYTREENODE **pRoot)
{
	int value = 0;
	printf("Please Input a None Zero Value : ");
	scanf("%d",&value);
	printf("Value = %d\n",value);
	if(value == 0)
	{
		*pRoot = NULL;
		return;
	}
	else
	{
		*pRoot = (BINARYTREENODE *)malloc(sizeof(BINARYTREENODE));
		printf("*pRoot = %p\n",*pRoot);
		printf("*pRoot = %p\n",pRoot);
		(*pRoot)->mValue = value;
		CreateBinaryTree(&((*pRoot)->pLeft));
		CreateBinaryTree(&((*pRoot)->pRight));
	}
}

void DeleteBinaryTree(BINARYTREENODE ** pRoot)
{
	if ((*pRoot)->pLeft == NULL && (*pRoot)->pRight == NULL)
	{	
		printf("Delete Node is %d\n",(*pRoot)->mValue);
		*pRoot = NULL;
		free(*pRoot);		
		return;
	}
	else
	{
		DeleteBinaryTree(&((*pRoot)->pLeft));
		DeleteBinaryTree(&((*pRoot)->pRight));
	}
}
void ShowBinaryTree(BINARYTREENODE * pRoot)
{
	if (NULL!=pRoot)
	{
		printf("%d ",pRoot->mValue);
	}
}

void PerOrder(BINARYTREENODE * pRoot)
{
	if (NULL!=pRoot)
	{
		ShowBinaryTree(pRoot);
		PerOrder(pRoot->pLeft);
		PerOrder(pRoot->pRight);
	}
}

void InOrder(BINARYTREENODE * pRoot)
{
	if (NULL!=pRoot)
	{
		InOrder(pRoot->pLeft);
		ShowBinaryTree(pRoot);		
		InOrder(pRoot->pRight);
	}
}

void PostOrder(BINARYTREENODE * pRoot)
{
	if (NULL!=pRoot)
	{
		PostOrder(pRoot->pLeft);	
		PostOrder(pRoot->pRight);
		ShowBinaryTree(pRoot);	
	}
}

int main()
{
	BINARYTREENODE * pRoot = NULL;

	CreateBinaryTree(&pRoot);
	printf("%p\n",pRoot);	
	printf("Find All Pre Order of Binary Tree : ");
	PerOrder(pRoot);
	printf("\n");

	printf("Find All In Order of Binary Tree : ");
	InOrder(pRoot);
	printf("\n");

	printf("Find All Post Order of Binary Tree : ");
	PostOrder(pRoot);
	printf("\n");

	printf("Before Delete %p\n",pRoot);
	while (pRoot!=NULL)
	{
		DeleteBinaryTree(&pRoot);
	}
	
	printf("After Delete %p\n",pRoot);
}


