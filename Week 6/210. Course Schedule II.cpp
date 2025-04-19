class Solution {
    public:
        struct Node {
            int val;
            vector<Node*> children;
        };
    
        Node* findNode(Node* subj, int val){
            if (subj == nullptr || subj->val != val){
                return nullptr;
            }
    
            Node* currentResult = nullptr;
            for (size_t i = 0; i < subj->children.size(); i += 1){
                currentResult = findNode(subj->children[i], val);
                if (currentResult != nullptr){
                    return currentResult;
                }
            }
    
            return nullptr;
        }
    
        vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
            Node* headNode;
    
            headNode->val = 0;
    
            for (size_t i = 0; i < prerequisites.size(); i++){
                Node* prereq = findNode(headNode, prerequisites[i][1]);
    
                if (prereq == nullptr){
                    cout << "HMMMM";
                } else {
                    prereq->children.push_back(new Node {prerequisites[i][0]});
                }
            }
    
            // now perform bfs on this tree
            vector<Node*> vec {headNode};
    
            int frontIndex = 0;
    
            vector<int> finishedOrder;
            while (vec.size() > 0){
                finishedOrder.push_back(vec[frontIndex]->val);
                
                for (size_t i = 0; i < vec[frontIndex]->children.size(); i++){
                    vec.push_back(vec[frontIndex]->children[i]);
                }
    
                frontIndex += 1;
            }
    
            return finishedOrder;
        }
    };