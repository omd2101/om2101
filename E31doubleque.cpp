#include<iostream>
using namespace std;
#define n 5

class dequeue{
    private:
    int a[n];
    int rear,front;
    public:
    dequeue(){
        rear=-1;
        front=-1;
    }
    void push_front(int);
    void push_back(int);
    void pop_front();
    void pop_back();
    bool empty();
    bool full();
    void display();
};

void dequeue :: push_front(int z){
    if(rear==-1  &&  front==-1){
        front++;rear++;
        a[front]=z;
        return;
    }
    else if(front<=0  &&  rear>=n-1){
        cout<<"Queue is overflow"<<endl;
        return;
    }
    else if(front>0 &&  front<=rear){
        front--;
        a[front]=z;
        return;
    }
    else if(front==0 && rear<n-1){
        for(int i=rear+1;i>front;i--){
            a[i]=a[i-1];
        }
        rear++;
        a[front]=z;
        return;
    }
    else{
        cout<<"Condition not valid"<<endl;
    }
}

void dequeue :: push_back(int z){
    if(front==-1  &&  rear==-1){
        front++; rear++;  a[rear]=z;
        return;
    }
    else if(front<=0  &&  rear>=n-1){
        cout<<"Queue is overflow"<<endl;
        return;
    }
    else if(rear<n-1  &&  rear>=front){
        rear++;  a[rear]=z;
        return;
    }
    else if(rear==n-1  &&  front>0){
        for(int i=front-1;i<rear;i++){
            a[i]=a[i+1];
        }
        front--;
        a[rear]=z;
        return;
    }
    else{
        cout<<"Condition not valid"<<endl;
    }

}

void dequeue :: pop_front(){
    if(front==-1  &&  rear==-1  ||  front>rear){   cout<<"Queue is empty"<<endl;  return;}
    else {
        front++;
    }
}

void dequeue :: pop_back(){
    if(front==-1  &&  rear==-1  ||  front>rear){   cout<<"Queue is empty"<<endl;  return;}
    else {
        rear--;
    }
}

bool dequeue :: empty(){
    if(front==-1  &&  rear==-1  ||  front>rear){
        return true;
    }
    return false;
}

bool dequeue :: full(){
    if(front<=0  &&  rear >=n-1){
        return true;
    }
    return false;
}

void dequeue :: display(){
    if(front==-1  &&  rear==-1  ||  front>rear){   cout<<"Queue is empty"<<endl;  return;}
    for(int i=front;i<=rear;i++){  
        cout<<a[i]<<" ";  
    }
    cout<<endl;
    return;
}

int main(){
    int x;
    dequeue q;
    int ch=-1;
    while(ch!=8){
        cout<<" push  push        pop  pop        empty  full         display         exit"<<endl;
        cout<<"  1     2           3    4            5    6               7             8 "<<endl;
        cout<<"Enter the choice : "; 
        cin>>ch;
        switch(ch){
            case 1:
                cout<<"Enter for push front : ";cin>>x;
                q.push_front(x);
                break;
            case 2:
                cout<<"Enter for push back : "; cin>>x;
                q.push_back(x);
                break;
            case 3:
                q.pop_front();
                break;
            case 4:
                q.pop_back();
                break;
            case 5:
                (q.empty()) ? cout<<"Queue is empty"<<endl : cout<<"Not empty"<<endl;
                break;
            case 6:
                (q.full()) ? cout<<"Queue is full"<<endl : cout<<"Not full"<<endl;
                break;
            case 7:
                q.display();
                break;
            case 8:
                exit(0);
        }
    }
}