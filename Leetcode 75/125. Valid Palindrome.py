# The Code

``` Python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        ans=""
        for i in s:
            if i.isalnum()==True:
                ans+=i
        # print(ans," ","".join(reversed(ans)))
        if ans == "".join(reversed(ans)):
            return True
        return False
```
#   What i have learned is 

# isalpha - Just to check the alphabets
# isdigit -> just checks only numbers 
# isalnum -> Checks alphanumeric

# reversed -> Gives us the iteratable object containg the series of objects that can be traversed 
# join -> used to join it's like concatnating the elements to the empty string

# so, "".join(reversed(container)) will give us the container values converted to the string.
