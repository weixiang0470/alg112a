#include <iostream>
#include <vector>
#define ROW 6
#define COL 8
using namespace std;

vector<vector <int> > v_map;

int map[ROW][COL]={{1,1,1,1,1,1,1,1},
               {1,1,0,1,0,1,1,1},
               {0,0,0,0,0,1,1,1},
               {1,0,1,1,1,1,1,1},
               {1,0,0,0,0,0,1,1},
               {1,1,1,1,1,0,1,1}};

void print_map(int maze[ROW][COL]){
    for(int i=0;i<sizeof(map)/sizeof(map[0]);i++){
        for(int j=0;j<sizeof(map[0])/sizeof(int);j++){
            cout<<maze[i][j];
        }
        cout<<"\n";
    }
}

void print_path(vector<vector<int> > path){
    for(int i=0;i<path.size();i++){
        cout<<"[";
        for(int j=0;j<path.at(i).size();j++){
            cout<<path.at(i).at(j);
        }
        cout<<"]";
    }
    cout<<"\n";
}

void find(int x, int y,vector<vector<int> > path){
    if(x>6 || x<0 || y>8 || y<0)return;
    vector<int> p;
    if(x==5 && y==5){
        p.push_back(x);
        p.push_back(y);
        path.push_back(p);
        print_path(path);
        return;
    }
    p.push_back(x);
    p.push_back(y);
    for(int i=0;i<v_map.size();i++){if(p==v_map[i])return;}
    v_map.push_back(p);
    path.push_back(p);
    if(map[x+1][y]==0)find(x+1,y,path);
    if(map[x-1][y]==0)find(x-1,y,path);
    if(map[x][y+1]==0)find(x,y+1,path);
    if(map[x][y-1]==0)find(x,y-1,path);
}

int main(void){
    vector<vector<int> > path;
    find(2,0,path);
}