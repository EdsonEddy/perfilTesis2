#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;
int main(){
	int n,p,h,s,costo,libre;
	while(cin>>n>>p>>h>>s){
		bool sw=false;
		int minimo=999999999;
		for(int i=0;i<h;i++){
			cin>>costo;

			for(int j=0;j<s;j++){
				cin>>libre;
				if(libre>=n)sw=true;
			}
			if(sw)minimo=min(minimo,n*costo);
		}
		if(minimo!=999999999 and minimo<=p)cout<<minimo<<endl;
		else cout<<"quedarse en casa"<<endl;
			
		
	}
	return 0;
}