/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {

        if (root == nullptr){
            return vector<int>();
        }
        
        int maxDepth = 0;
        int currentDepth = 0;

        TreeNode* currentNode = root;

        vector<int> rightview {root->val};

        vector<TreeNode*> pastNodes;

        int i = 0;

        while (i < 50){
            // general algorithm

            if (currentNode == nullptr){
                break;
            }

            while (true){
                pastNodes.push_back(currentNode);

                if (currentDepth > maxDepth){
                    rightview.push_back(currentNode->val);
                    maxDepth += 1;
                }

                if (currentNode->right == nullptr){
                    break;
                }

                currentNode = currentNode->right;
                currentDepth += 1;

                // cout << "current node currently0 " << currentNode->val << "level is" << currentDepth << endl;
            }

            // cout << "current node currently1 " << currentNode->val << "level is" << currentDepth << endl;


            // backtrack a bit
            TreeNode* previousNode = nullptr;
            while (currentNode->left == nullptr || currentNode->left == previousNode){

                if (pastNodes.size() != 0){
                    if (pastNodes.size() < 2){
                        return rightview;
                    } else {
                        previousNode = currentNode;
                        currentNode = pastNodes[pastNodes.size()-2];
                        currentDepth -= 1;
                        pastNodes.pop_back();
                    }
                } else {
                    break;
                }

                // cout << "current node currently2 " << currentNode->val << "level is" << currentDepth << endl;
            }

            currentNode = currentNode->left;
            currentDepth += 1;


            // cout << "now, current node is " << currentNode->val << endl;


            i += 1;
        }

        return rightview;

    }
};