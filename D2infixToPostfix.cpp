 #include<iostream>                        //  (a-b/c)(a/k-l)   -> abc/-ak/l-
#include<stack>
using namespace std;

int power(char c){
    if(c=='^')   return 3;
    if(c=='/'  ||  c=='*')   return 2;
    if(c=='+'  ||  c=='-')   return 1;
    else return -1;
}

void prefix_to_postfix(string s){
    stack < char > st;
    string res;
    for(int i=0;i<s.length();i++){
        if(s[i]>='a'  &&  s[i]<='z'  ||  s[i]>='A'  &&  s[i]<='Z'){
            res+=s[i];
        }
        else if(s[i]=='(')  st.push(s[i]);
        else if(s[i]==')'){
            while(!st.empty()  &&  st.top()!='('){
                res+=st.top();
                st.pop();
            }
            st.pop();
        }
        else{
            while(!st.empty()   &&    power(s[i])<power(st.top())){
                res+=st.top();
                st.pop();
            }
            st.push(s[i]);
        }
    }
    while(!st.empty()){    res+=st.top();    st.pop();  }
    cout<<res<<endl;
}

int main(){
    string s9;
    cout<<"enter expression";
    cin>>s9;
    prefix_to_postfix(s9);
    return 0;
}