#include<algorithm>
#include<iostream>
using namespace std;
int appe(int size,int a[],int k)
{
    sort(a,a+size);
    for(int i=0;i<size;i++)
        cout<<a[i];
    int i = 1, count =1;
    int element = a[0];
    int res = -1;
    while(i<size+1)
    {
        if(element==a[i])
        {
        count++;
     
        }
        
        else{
            
               if(count==k){
                res = element;
            }
            element = a[i];
            count=1;
    }
    i++;
}
cout<<count<<endl;
return res;

}


int main()
{
    int a[7] = {1,2,2,5,3,4,6};
    int size = 7;
    int k =2;
    int ans;
    ans = appe(size,a,k);
    cout<<ans<<endl;
}