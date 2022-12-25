#include<iostream>
#include<stack>
using namespace std;

void expression(string s){
    stack < char >st;                                          
    for(int i=0;i<s.length();i++){
        if(s[i]=='('  ||  s[i]=='['  ||  s[i]=='{'){
            st.push(s[i]);
        }
        if(s[i]==')'){
            if(!st.empty()  &&  st.top()=='('){
                st.pop();
            }
            else   st.push(s[i]);
        }
        if(s[i]==']'){
            if(!st.empty()  &&  st.top()=='['){
                st.pop();
            }
            else   st.push(s[i]);
        }
        if(s[i]=='}'){
            if(!st.empty()  &&  st.top()=='{'){
                st.pop();
            }
            else   st.push(s[i]);
        }
        else   continue;
    }
    if(st.empty())    cout<<"Well Paranthesise"<<endl;
    else  cout<<"NOT PARENTHESISE PROPERLY"<<endl;
    //while(!st.empty()){
    //    cout<<st.top();
    //    st.pop();
    //}
}

int main(){
    string s1;
    cout<<"enter the string";
    cin>>s1;

    expression(s1);
}

//((8)(*--$$9))
//8)*(9)
