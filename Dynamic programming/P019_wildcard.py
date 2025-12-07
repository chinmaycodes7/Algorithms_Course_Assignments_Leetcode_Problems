
"""P019 - Wildcard matching: '?' matches one char, '*' matches zero or more chars"""
def is_match(s, p):
    n=len(s); m=len(p)
    dp=[[False]*(m+1) for _ in range(n+1)]
    dp[0][0]=True
    # handle leading *
    for j in range(1,m+1):
        if p[j-1]=='*':
            dp[0][j]=dp[0][j-1]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if p[j-1]=='?' or p[j-1]==s[i-1]:
                dp[i][j]=dp[i-1][j-1]
            elif p[j-1]=='*':
                # * matches zero (dp[i][j-1]) or one/more (dp[i-1][j])
                dp[i][j]=dp[i][j-1] or dp[i-1][j]
            else:
                dp[i][j]=False
    return dp[n][m]

if __name__=="__main__":
    assert is_match("abcd","a*d")
    assert is_match("acdcb","a*c?b")==False
    assert is_match("aa","*")==True
    print("P019 OK")
