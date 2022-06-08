#include <iostream>
#define MAX 100001
using namespace std;
int main(){
    int N, P, H, S, x, y;
    while(cin>>N>>P>>H>>S){
        int min=MAX;
        while(H--){
            cin>>x;
            bool sw=true;
            for(int i=0; i<S; i++){
                cin>>y;
                if(y<N)
                    sw=false;
            }
            if(sw){
                if(x*N<min && x*N<=P)
                    min=x*N;
            }

            }
        if(min==MAX)
            cout<<"quedarse en casa"<<endl;
        else
            cout<<min<<endl;

    }
    return 0;
}
