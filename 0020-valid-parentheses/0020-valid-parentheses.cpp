#include <stack>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> si;
        
        for (char ch : s) {
            if (ch == '(' || ch == '{' || ch == '[') {
                si.push(ch);  // Push opening brackets onto the stack
            } else {
                if (si.empty()) return false;  // Closing bracket with no opening pair
                
                char top = si.top();
                if ((ch == ')' && top == '(') || 
                    (ch == '}' && top == '{') || 
                    (ch == ']' && top == '[')) {
                    si.pop();  // Proper match found, pop from stack
                } else {
                    return false;  // Mismatched closing bracket
                }
            }
        }
        
        return si.empty();  // Stack should be empty if all pairs matched
    }
};
