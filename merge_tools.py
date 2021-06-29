'''
This is the python solution for the following hackerrank question:

    https://www.hackerrank.com/challenges/merge-the-tools/problem
    
'''

def merge_the_tools(string, k):
    substrs = list()
    substr = list()
    final_s = list()
    for i in range(0,len(string),k):
        substrs.append(string[i:i+k])

    for x in substrs:
        for y in x:
            if y not in substr:
                substr.append(y)
        final_s.append(''.join(substr))
        substr.clear()

    print(*final_s,sep='\n')


if __name__ == '__main__':
    string,k = input() , int(input())
    merge_the_tools(string,k)
