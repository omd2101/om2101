#include<iostream>
using namespace std;
# define n 20

class queue{
    private:
    int arr[n];
    int front,back;
    public:
    queue(){
        front = -1;
        back = -1;
    }
    void push(int);
    void pop();
    int peek();
    bool empty();
    bool full();
    void display();
};

void queue :: push(int x){
    if( back>=n-1){
        cout<<"Overflow."<<endl;
        return;
    }
    if(front==-1)  front++;
    back++;
    arr[back]=x;
}

void queue :: pop(){
    if(front==-1  ||  front>back){
        cout<<"Queue is Empty."<<endl;
        return;
    }
    front++;
}

int queue :: peek(){
    if(front==-1  ||  front>back){
        cout<<"Queue is Empty."<<endl;
        return -1;
    }
    return arr[front];
}

bool queue :: empty(){
    if(front==-1  ||  front>back)   return true;
    return false;
}

bool queue :: full(){
    if(front<back  ||  back==n-1)  return true;
    return false;
}

void queue :: display(){
    if(front==-1  ||  front>back){
        cout<<"Queue is Empty."<<endl;
        return;
    }
    for(int i=front;i<=back;i++)   cout<<arr[i]<<" ";  cout<<endl;
}


int main(){
    int ch;
    int val;
    queue q;
    while(true){
        cout<<"1. Insert \n2. Delete \n3. Display \n4. Check empty \n5. Check full \n6. Exit \nEnter choice : ";
        cin>>ch;
        switch(ch){
            case 1:
                cout<<"Enter the value : ";  cin>>val;  q.push(val);  break;
            case 2:
                q.pop();    break;
            case 3:
                q.display();     break;
            case 4:
                if(q.empty())   cout<<"Queue is empty"<<endl;
                else  cout<<"Queue is not empty"<<endl;       break;
            case 5:
                if(q.full())   cout<<"Queue is full"<<endl;
                else    cout<<"Queue is not full"<<endl;       break;
            case 6:
                exit(0);
            

        }
    }

    return 0;
}