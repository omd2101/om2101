#include<iostream>
using namespace std;

class node{
    public:
    char name[10];
    int prn;
    node * next;
};

class list{
    private:
    node * president;
    node * secretory;
    node * current;
    node * currentmin;
    int count;
    public:
    list(){
        count=0;
        president =new node;
        secretory =new node;
        current = new node;
        currentmin=new node;
    }
    void display();
    void gethead();
    void gettail();
    void addmember();
    void remove();
    void displaycount();
    void disp_rev(list*);
    friend void display_reverse(list,node *);
};

void list :: gethead(){
    count++;
    cout<<"Enter the name of precident : ";cin>>president->name;
    cout<<"Enter the roll number of president : "; cin>>president->prn;
    president->next=secretory;
}

void list :: gettail(){
    count++;
    cout<<"Enter the name of secretory : ";  cin>>secretory->name;
    cout<<"Enter the prn of secretory : ";  cin>>secretory->prn;
    secretory->next = NULL;
}

void list :: addmember(){
    count++;
    node * tmp =new node;
    cout<<"Enter the name of member : ";  cin>>tmp->name;
    cout<<"Enter the roll number of prn : ";cin>>tmp->prn;
    
    if( president->prn>tmp->prn ){
        tmp->next=president;
        president=tmp;
    }
    else if( secretory->prn<tmp->prn ){
        secretory->next=tmp;
        tmp->next=NULL;
        secretory = tmp;
    }
    else if( president ==NULL ){
        president = tmp;
    }
    else if( president->next==NULL ){
        if ( president->prn>tmp->prn ){
            tmp->next=president;
            president->next =NULL;
            president=tmp;
        }
        else{
            president->next = tmp;
            tmp->next = NULL;
        }
    }
    else{
        currentmin=president;
        current=president->next;
        while( current->prn<tmp->prn  &&  current!=secretory ){
            current=current->next;
            currentmin=currentmin->next;
        }
        currentmin->next=tmp;
        tmp->next=current;
    }
    current=NULL;
    currentmin=NULL;
    tmp=NULL;
}

void list :: displaycount(){
    cout<<"Total member : "<<count<<endl;
}

void list :: display(){
    current=president;
    while(current->next != NULL){
        cout<<"Name : "<<current->name<<endl;
        cout<<"Prn : "<<current->prn<<endl;
        current=current->next;
    }
    cout<<"Name : "<<current->name<<endl;
    cout<<"Prn : "<<current->prn<<endl;
    current = NULL;
}

void list :: remove(){
    count--;
    int pon=0;
    cout<<"Enter the prn for delete : ";cin>>pon;
    node * tmp;
    currentmin=president;
    current=president->next;
    if(pon==president->prn){
        tmp=currentmin;
        delete tmp;
        president=current;
        return;
    }
    else if(pon==secretory->prn){
        while( current->next !=NULL ){
            current=current->next;
            currentmin=currentmin->next;
        }
        tmp=current;                                    // error
        delete tmp;
        currentmin->next=NULL;
        secretory=currentmin;
        return;
    }
    else if( president == NULL ){
        cout<<"Error underflow "<<endl;
        count--;
        return;
    }
    else{
        while( current->prn <=pon  &&  pon<=secretory->prn ){
            if( current->prn == pon ){
                currentmin->next = current->next;
                delete current;
                return;
            }
            else{
                current=current->next;
                currentmin=currentmin->next;
            }
        }
    }
    count--;
    cout<<"member not present."<<endl;
}

//friend void display_reverse(iist *a ,node *head );

int main(){
    list a;
    a.gethead();
    a.gettail();
    int ch=-1;
    while(ch!=6){
        cout<<"1 2 3 4 6"<<endl;
        cout<<"Enter : ";cin>>ch;
        switch(ch){
            case 1:
                a.addmember();  break;
            case 2:
                a.remove();  break;
            case 3:
                a.displaycount();  break;
            case 4:
                a.display();   break;
            case 6:
                exit(0);
        }
    }
}