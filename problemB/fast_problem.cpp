#include <iostream>
#include <string>
#include <vector>
#include <deque>
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

bool compare_edges(edge e1, edge e2){
    return e1.weight < e2.weight;
}

bool node_in_dq(deque<search_node> s, search_node node){
    for(auto cn : s){
        if(cn.val == node.val && cn.n == node.n){
            return true;
        }
    }
    return false;
}


bool edge_deletable(edge e){
    return ( e.n1 == -1 && e.n2 == -1 ); // not a multigraph so we dont check for weights
}

void printQueue(deque<search_node> q){
    cout << "queue : ";
    for(auto el : q){
        cout << "(" << el.n << "," << el.val << ");";
    }
    cout << endl;
}

deque<search_node> succ(vector<long>  & nodes, vector<edge> & edges, search_node current){
    
    deque<search_node> s;
    edge delVal;
    delVal.n1 = -1;
    delVal.n2 = -1;
    delVal.weight = -1;

    for (auto edge = edges.begin(); edge != edges.end(); edge++) {
        search_node step;
        step.n = edge->n2;
        step.val = max(edge->weight,current.val);
        if(edge->n1 == current.n && !node_in_dq(s,step) ){
            s.push_back(step);
          
            *edge = delVal;
        }
        else{
            step.n = edge->n1;
            if(edge->n2 == current.n &&  !node_in_dq(s,step)){
                s.push_back(step);
                *edge = delVal;
            }
        }
    }

    // delete explored edges to gain time
    edges.erase(remove_if(edges.begin(),edges.end(),edge_deletable),edges.end());

    // for(auto e: edges){
    //     cout << "(" << e.n1 << ";" << e.n2 << ")";
    // }
    // cout << endl;

    // cout << "succ for node " << current.n << " ; " ;
    // printQueue(s);
    
    return s;
}

long thresh(long goal, vector<long> nodes, vector<edge> edges){
    // initializing the root and goal nodes
    long root = 1;
    // cout << "goal" << goal << endl;

    // initializing the queue
    deque<search_node> q;
    search_node root_node;
    root_node.n = root;
    root_node.val = 0;
    q.push_back(root_node);


    sort(q.begin(),q.end(),compare_nodes);

    while (q.size()>0){

        search_node current = q.at(0);
        q.erase(q.begin()   );

        // computing queue value
        deque<search_node> s = succ(nodes,edges,current);

        // appending a sorted successor queue to the queue
        // sort(s.begin(),s.end(),compare_nodes);
        for(auto succ : s){
            if(!node_in_dq(q,succ)){
                q.push_back(succ);
            }
        }

        // sorting the queue
        sort(q.begin(),q.end(),compare_nodes);

        // cout << current.n << endl;  

        // printQueue(q);

        if(current.n == goal){
            return current.val;
        }



    }

    // for(auto el:Q){
    //     cout << "(" <<el.n << "," << el.val << ")" << endl;
    // }

    return -1;
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
    cout << thresh(nNodes,nodes,edges) << endl;

}