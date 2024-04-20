#include<iostream>
using namespace std;

// 주말 미션!
// 링크드리스트 구현
// C++ : NULL은 0과 같다

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
    
    void insertFirst(Node* newNode)   //맨 앞에 newNode 추가
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

        if(index == 1)  // 즉 맨앞삽입
            insertFirst(newNode);
        else if(index == LinkedListSize+1) // 즉 맨뒤삽입
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

    void deleteNode(int data)   // 특정 데이터를 가지는 노드 삭제
    {
        Node* currentNode = head;
        if(currentNode->data == data)   // 맨 앞 헤드 삭제필요
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
        for (int i = 0; i < LinkedListSize-1; i++)  // 이동 횟수 = 노드 개수-1
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


    // 삽입
    newNode.data = 1;
    linkedList.insertFirst(&newNode); // *** newNode의 *** 주소 위치를 넘겨줘!!!!!! 
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


    // 특정 값을 가지는 노드 삭제
    linkedList.deleteNode(1);   // 2 4 3
    linkedList.printAllNode();


    // 조회
    int index = linkedList.SearchData(2);
    if(index >= 0)   printf("해당 데이터는 %i번째 노드에 있습니다.\n", index+1);
    else        cout << "해당 데이터는 리스트에 없습니다.\n";


    return 0;
}
