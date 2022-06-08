#include <bits/stdc++.h>
#define PB(a) push_back(a)
#define MP(a,b) make_pair(a,b)
#define PBP(a,b) PB(MP(a,b))
using namespace std;
int main(){
    int n,p,h,s;
    while(cin>>n>>p>>h>>s){
        int hot,lel;
        vector<pair<int,int> > vec;
        for(int i=0;i<h;i++){
            cin>>hot;
            int aux = -1;
            for(int j=0;j<s;j++){
                cin>>lel;
                aux = max(aux,lel);
            }
            vec.PBP(hot,aux);
        }
        int sol = -1;
        for(int i=0;i<vec.size();i++){
            if(vec[i].first * n <=p && vec[i].second >=n)sol = vec[i].first * n;
        }
        if(sol==-1)cout<<"quedarse en casa"<<endl;
        else cout<<sol<<endl;
    }
    return 0;
}
