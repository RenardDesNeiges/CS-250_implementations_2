#include <iostream>
#include <string>
#include<vector>
#include <algorithm> 

using namespace std;

struct edge {
    long n1;
    long n2;
    long weight;
};

struct search_node {
    long n;
    long val;
};

std::vector<long> splitStringByChar(std::string str, char split)
{
    std::string nb = "";
    std::vector<long> out;

    for (auto x : str) 
    {
        if (x == split)
        {
            out.push_back(std::stol(nb));
            nb = "";
        }
        else {
            nb = nb + x;
        }
    }
    out.push_back(std::stol(nb));
    return out;
}

bool compare_nodes(search_node n1, search_node n2){
    return n1.val < n2.val;
}

vector<search_node> succ(vector<long> nodes, vector<edge> edges, search_node current){
    vector<search_node> s;
    vector<vector<edge>::iterator> delList;

    for (auto edge = edges.begin(); edge != edges.end(); edge++) {
        search_node step;
        step.n = edge->n2;
        step.val = max(edge->weight,current.val);
        if(edge->n1 == current.n && binary_search(s.begin(),s.end(),step) ){
            s.push_back(step);
            delList.push_back(edge);
        }
        else{
            step.n = edge->n1;
            if(edge->n2 == current.n && binary_search(s.begin(),s.end(),step) ){
                s.push_back(step);
                delList.push_back(edge);
            }
        }
    }

    for(auto it: delList){
        edges.erase(it);
    }
    
    return s;
}

long thresh(vector<long> nodes, vector<edge> edges){
    // initializing the root and goal nodes
    long root = 1;
    long goal = nodes.size()+1;

    // initializing the queue
    vector<search_node> Q;
    search_node root_node;
    root_node.n = root;
    root_node.val = 0;
    Q.push_back(root_node);


    sort(Q.begin(),Q.end(),compare_nodes);

    while (Q.size()>0){
        search_node current = Q.at(0);
        Q.erase(Q.begin());
        cout << current.n << ";" << current.val << endl;


    }

    // for(auto el:Q){
    //     cout << "(" <<el.n << "," << el.val << ")" << endl;
    // }

    return goal;
}

int main(){
    
    //getting the parameters from the first line
    string line;
    getline(std::cin, line);
    vector<long> splitLine = splitStringByChar(line,' ');
    long nNodes = splitLine.at(0);
    long nEdges = splitLine.at(1);

    vector<edge> edges;
    vector<long> nodes;

    for( int i = 0; i<nEdges; i++){
        // reanding edges from the buffer and instanciating a vector of edges
        string line;
        getline(std::cin, line);
        vector<long> splitLine = splitStringByChar(line,' ');
        edge nEdge;
        nEdge.n1 = splitLine.at(0);
        nEdge.n2 = splitLine.at(1);
        nEdge.weight = splitLine.at(2);
        edges.push_back(nEdge);
        nodes.push_back(i+1);
    }

    // for(auto el:edges){
    //     cout << "(" <<el.n1 << "," << el.n2 << ")" << " => " << el.weight << endl;
    // }
    cout << thresh(nodes,edges) << endl;

}