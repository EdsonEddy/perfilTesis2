#include <bits/stdc++.h>

using namespace std;
int n,d,h,s;
vector<int>v;
int solve(){
    int cc,hc,mini=-1;
    for(int i=0;i<h;i++){
        cin>>hc;
        bool si=false;
        for(int j=0;j<s;j++){
            cin>>cc;
            if(cc>=n)si=true;
        }
        if(si&&n*hc<=d){
            if(mini==-1)mini=n*hc;
            else mini=min(mini,n*hc);
        }
    }
    return mini;
}
int main()
{
    ios::sync_with_stdio(false);
    while(cin>>n>>d>>h>>s){
        int ans=solve();
        if(ans!=-1)cout<<ans<<"\n";
        else cout<<"quedarse en casa\n";
    }
    return 0;
}
