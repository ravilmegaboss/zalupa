class Solution {
public:
    vector<int> sumZero(int n) {
        vector<int> result(n);
        if(n % 2 == 0)
        {
            for(int i = 0; i < n/2; i++)
            {
                result[i] = i + 1;
                result[n - i - 1] = (1 + i) * (-1);
            }
        }
        else
        {
           for(int i = 0; i < n/2; i++)
            {
                result[i] = i + 1;
                result[n - i - 1] = (i + 1)  * (-1);
            }
            result[n/2] = 0;
        }
        return result;
    }
};