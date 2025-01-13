#include <bits/stdc++.h>

using namespace std;

struct compare {
    bool operator()(pair<int, Node*> const &a, pair<int, Node*> const &b) {
        return a.first >= b.first;
    }
}

struct Node {
    int val;
    Node* prev;
    Node* next;

    Node(int x) : val(x), prev(nullptr), next(nullptr) {}

    Node(int x, Node* prev, Node* next) : val(x), prev(prev), next(next) {}
};


class MaxStack{

public:
    Node* head;
    Node* tail;
    priority_queue<pair<int, Node*>, vector<pair<int, Node*>>, compare> pq;
    MaxStack(){
        head = new Node(0);
        tail = new Node(0);
        head->next = tail;
        tail->prev = head;
    }

    void push(int x){
        
    }

    int pop(){
        return 0;
    }

    int top(){
        
    }

    int peakMax(){
        
    }

    int popMax(){
        
    }
};

