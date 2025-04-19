class Solution {
    public:
    
        // void printVector(const vector<vector<int>>& grid){
        //     cout << "[";
        //     for (size_t i = 0; i < grid.size(); i++){
        //         cout << "[";
        //         for (size_t j = 0; j < grid[i].size(); j++){
        //             cout << grid[i][j];
        //         }
        //         cout << "]" << endl;
        //     }
        //     cout << "]" << endl;
        // }
    
        void resetZero(vector<vector<int>>& grid){
            for (size_t i = 0; i < grid.size(); i++){
                for (size_t j = 0; j < grid[i].size(); j++){
                    grid[i][j] = 0;
                }
            }
        }
    
        int orangesRotting(vector<vector<int>>& grid) {
            
            // count the number of fresh oranges to begin with
            int numFresh = 0;
    
            for (size_t i = 0; i < grid.size(); i++){
                for (size_t j = 0; j < grid[i].size(); j++){
                    if (grid[i][j] == 1){
                        numFresh += 1;
                    }
                }
            }
    
            int iteration = 0;
    
    
            vector<vector<int>> reserveGrid(grid.size(), vector<int>(grid[0].size()));
    
            // cout << reserveGrid.size() << reserveGrid[0].size();
    
    
    
            while (numFresh > 0 && iteration < 100) {
                iteration += 1;
                for (size_t i = 0; i < grid.size(); i++){
                    for (size_t j = 0; j < grid[i].size(); j++){
                        if ((grid[i][j] == 0 || grid[i][j] == 1) &&
                            reserveGrid[i][j] != 2){
                            reserveGrid[i][j] = grid[i][j];
                        } else if (reserveGrid[i][j] != 2){
                            reserveGrid[i][j] = grid[i][j];
    
                            if (i >= 1 && grid[i-1][j] == 1 && reserveGrid[i-1][j] != 2){
                                reserveGrid[i-1][j] = 2;
                                numFresh -= 1;
                                // cout << "upper changed" << endl;
                            }
                            if (i+1 < grid.size() && grid[i+1][j] == 1 && reserveGrid[i+1][j] != 2){
                                reserveGrid[i+1][j] = 2;
                                numFresh -= 1; 
                                // cout << "lower changed" << endl;
                            }
                            if (j >= 1 && grid[i][j-1] == 1 && reserveGrid[i][j-1] != 2){
                                reserveGrid[i][j-1] = 2; 
                                numFresh -= 1;
                                // cout << "left changed" << endl;
                            }
                            if (j+1 < grid[0].size() && grid[i][j+1] == 1 && reserveGrid[i][j+1] != 2){
                                reserveGrid[i][j+1] = 2; 
                                numFresh -= 1;
                                // cout << "right changed" << endl;
                            }
                        }
                    }
                }
    
                grid = reserveGrid;
    
                // printVector(grid);
    
                // cout << numFresh;
    
                resetZero(reserveGrid);
            }
            
            if (iteration < 100){
                return iteration;
            } else {
                return -1;
            }
        }
    };