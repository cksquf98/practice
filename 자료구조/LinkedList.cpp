#include<iostream>
using namespace std;

// �ָ� �̼�!
// ��ũ�帮��Ʈ ����
// C++ : NULL�� 0�� ����

class Node
{
    public:
        Node* next = nullptr;
        int data;
};

class LinkedList
{
    private:
        int LinkedListSize = 0;
    public:
        Node* head = nullptr;
        Node* tail = nullptr;
    void printAllNode()
    {   
        Node* currentNode = head;
        while (currentNode != tail->next)
        {
            cout << currentNode->data << '\n';
            currentNode = currentNode->next;
        }
    }
    
    void insertFirst(Node* newNode)   //�� �տ� newNode �߰�
    {
        if(head == nullptr)    //empty
        {
            head = newNode;
            newNode->next = nullptr;
            tail = newNode;

            LinkedListSize++;
        }
        else
        {   
            newNode->next = head;
            head = newNode;

            LinkedListSize++;
        }
    }

    void insertLast(Node* newNode)
    {
        if(head == nullptr)
        {
            head = newNode;
            newNode->next = nullptr;
            tail = newNode;

            LinkedListSize++;
        }
        else
        {
            tail->next = newNode;
            tail = newNode;

            LinkedListSize++;
        }
    }

    void insertIndex(Node* newNode, int index)
    {
        Node* target = head;

        if(index == 1)  // �� �Ǿջ���
            insertFirst(newNode);
        else if(index == LinkedListSize+1) // �� �ǵڻ���
            insertLast(newNode);
        else
        {
            while (--index -1 > 0)
            {
                target = target->next;
            }

            newNode->next = target->next;
            target->next = newNode;

            LinkedListSize++;
        }
    }

    void deleteNode(int data)   // Ư�� �����͸� ������ ��� ����
    {
        Node* currentNode = head;
        if(currentNode->data == data)   // �� �� ��� �����ʿ�
        {
            head = head->next;
            delete currentNode;
            return;
        }

        while(currentNode != tail->next)
        {
            if(currentNode->next->data == data)
            {
                if(currentNode->next == tail)
                {
                    tail = currentNode;
                    delete currentNode->next;
                }
                Node* target = currentNode->next;
                currentNode->next = target->next;
                delete target;
                return;
            }
            currentNode = currentNode->next;
        }       
    }

    int SearchData(int data)
    {
        Node* currentNode = head;
        for (int i = 0; i < LinkedListSize-1; i++)  // �̵� Ƚ�� = ��� ����-1
        {
            if(currentNode->data == data)
            {
                return i;
            }   
            currentNode = currentNode->next;
        }
        return -1;
    }
};

int main(int argc, char const *argv[])
{
    Node newNode;
    LinkedList linkedList;


    // ����
    newNode.data = 1;
    linkedList.insertFirst(&newNode); // *** newNode�� *** �ּ� ��ġ�� �Ѱ���!!!!!! 
    // linkedList.printAllNode();


    Node newNode2;
    newNode2.data = 2;
    linkedList.insertFirst(&newNode2);  // 2 1
    // linkedList.printAllNode();


    Node newNode3;
    newNode3.data = 3;
    linkedList.insertLast(&newNode3);   // 2 1 3
    // linkedList.printAllNode();

    
    Node newNode4;
    newNode4.data = 4;
    linkedList.insertIndex(&newNode4, 2);   // 2 4 1 3
    // linkedList.printAllNode();


    // Ư�� ���� ������ ��� ����
    linkedList.deleteNode(1);   // 2 4 3
    linkedList.printAllNode();


    // ��ȸ
    int index = linkedList.SearchData(2);
    if(index >= 0)   printf("�ش� �����ʹ� %i��° ��忡 �ֽ��ϴ�.\n", index+1);
    else        cout << "�ش� �����ʹ� ����Ʈ�� �����ϴ�.\n";


    return 0;
}
