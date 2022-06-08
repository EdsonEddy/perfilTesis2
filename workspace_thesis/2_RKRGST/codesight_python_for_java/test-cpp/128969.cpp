#include<bits/stdc++.h>
using namespace std;
int main() {
    int a,b,c,d,i,j,p,m;
    while(cin>>a>>b>>c>>d){
        m=1e6;
        while(c--){
            cin>>p;
            int v[d];
            int c=0,s=a;
            for(i=0;i<d;i++)cin>>v[i];
            sort(v,v+d);
            for(i=d-1;i>=0 && s>0;i--){
                s-=v[i];c++;
            }
            c=c*p*a;
            if(s<1 && c>0)m=c<m?c:m;
        }
        if(m<=b)cout<<m<<endl;
        else cout<<"quedarse en casa\n";
    }
}