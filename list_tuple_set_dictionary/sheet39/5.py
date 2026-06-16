# 5.

# =========================================
# WORD LENGTH GROUPING
# ====================

# A content management system stores article tags.

# tags = ["python","java","api","react","html","css"]

# Write a program to:

# * Group words according to their length.
# * Store result in dictionary.

# Sample Output:
# {
# 3:['api','css'],
# 4:['java','html'],
# 5:['react'],
# 6:['python']
# }

tags = ["python","java","api","react","html","css"]

t={}
for x in tags:
    if len(x) not in t:
        t[len(x)]=[]
    t[len(x)].append(x)


t=sorted(t.items())
for k,v in t:
    print(k,v)



