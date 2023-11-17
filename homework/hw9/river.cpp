#include <iostream>
#include <vector>
using namespace std;

vector <int> start(4,0);
vector <int> goal(4,1);
vector <string> role;
vector < vector <int> > VisitedMap;

void P_path(vector < vector <int> > path){
    for(int i=0;i<path.size();i++){
        for (int j=0;j<path.at(i).size();j++){
            if(j+1 == path.at(i).size())cout<<role.at(j)<<path.at(i).at(j);
            else cout<<role.at(j)<<path.at(i).at(j)<<" : ";
        }
        cout<<"\n";
    }
}

vector < vector <int> > neighbours(vector <int> state){
    int p_site = state.at(0);
    vector < vector <int> > nb_list;
    vector <int> nb;
    int next_p_site;

    if(p_site)next_p_site=0;
    else next_p_site=1;
    //人物自己移動
    nb.push_back(next_p_site);
    for(int i=1;i<state.size();i++){
        nb.push_back(state[i]);
    }
    nb_list.push_back(nb);
    /*cout<<"NB1\n";
    P_path(nb_list);*/
    nb.clear();
    //一起移動
    for(int i=1;i<state.size();i++){
        if(state.at(i)==p_site){
            for(int j=0;j<state.size();j++){
                nb.push_back(state.at(j));
            }
            nb.at(0)=next_p_site;
            nb.at(i)=next_p_site;
            nb_list.push_back(nb);
            /*cout <<"NB2\n";
            P_path(nb_list);*/
            nb.clear();
        }
    }
    return nb_list;
}

int Is_Dead(vector <int> state){
    if(state.at(1) == state.at(2) && state.at(0) != state.at(1))return 1;
    if(state.at(2) == state.at(3) && state.at(0) != state.at(2))return 1;
    return 0;
}

void dfs(vector <int> state, vector < vector <int> > path){
    //P_path(path);
    /*for (int j=0;j<state.size();j++){
        cout<<state.at(j);
    }
    cout<<"\n";*/
    if(Is_Dead(state))return;
    for(int i=0;i<VisitedMap.size();i++){if(state==VisitedMap.at(i))return;}
    VisitedMap.push_back(state);
    path.push_back(state);
    if(state == goal){cout<<"PATH\n";P_path(path);return;}
    vector < vector <int> > nb_list = neighbours(state);
    for(int i=0;i<nb_list.size();i++){
        dfs(nb_list.at(i),path);
    }
    path.pop_back();
}

int main(void){
    vector < vector <int>  > path;
    role.push_back("人");
    role.push_back("狼");
    role.push_back("羊");
    role.push_back("菜");
    dfs(start,path);
}

/*    
    vector <int> s1(4,1);
    vector <int> s2;
    vector <int> s3;
    s2.push_back(1);
    s2.push_back(0);
    s2.push_back(1);
    s2.push_back(0);
    s3.push_back(0);
    s3.push_back(0);
    s3.push_back(0);
    s3.push_back(0);
    VisitedMap.push_back(s1);
    VisitedMap.push_back(s2);
    VisitedMap.push_back(s3);
    for(int i=0;i<VisitedMap.size();i++){
        for (int j=0;j<VisitedMap.at(i).size();j++){
            cout<<VisitedMap.at(i).at(j);
        }
        cout<<"\n";
    }
    int count = dfs(start);
    cout<<count<<"\n";
    */