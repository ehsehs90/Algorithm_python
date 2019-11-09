
def solution(s):
    

    ans = len(s)
    # print(ans)
    for size in range(1, ans+2//2):
        ans = min(ans, compress(size))

    return ans

def compress(size):
        ret = 0
        before, count ='', 1
        for i in range(0, len(s),size):
            word=s[i:i+size]
            if word == before:
                count+=1
                # print(9)
            else:
                if count >1:
                    ret += len(str(count))
                ret += len(before)
                before, count = word, 1
        if count >1:
            ret += len(str(count))
        ret += len(before)
        return ret 




s="aabbaccc"
print(solution(s))
