# 10.

# =========================================
# EMAIL DOMAIN COUNTER
# ====================

# emails = [
# "[ajay@gmail.com](mailto:ajay@gmail.com)",
# "[ravi@yahoo.com](mailto:ravi@yahoo.com)",
# "[neha@gmail.com](mailto:neha@gmail.com)",
# "[aman@outlook.com](mailto:aman@outlook.com)",
# "[abc@gmail.com](mailto:abc@gmail.com)"
# ]

# Write a program to:

# * Count users belonging to each email domain.

# Sample Output:
# {
# 'gmail.com':3,
# 'yahoo.com':1,
# 'outlook.com':1
# }

emails = [
"[ajay@gmail.com](mailto:ajay@gmail.com)",
"[ravi@yahoo.com](mailto:ravi@yahoo.com)",
"[neha@gmail.com](mailto:neha@gmail.com)",
"[aman@outlook.com](mailto:aman@outlook.com)",
"[abc@gmail.com](mailto:abc@gmail.com)"
]

for x in emails:
    for y in x:
        if y=="@":
            # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


e={}
for x in emails:
    e[x]=e.get(x,0)+1

for k,v in e.items():
    print(k," ",v)

