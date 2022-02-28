# Diff type for-iterators:-
# =========================
# forward iterator:-
# ------------------
# read-only access on the collection
# fastest 

numlst = [10,20,30,40,50]

for elem in numlst:
   res = elem * elem

# Output:
# 2500



# reverse iteartor:-
# ------------------
# read-only access on the collection
# fastest 

numlst = [10,20,30,40,50]

for elem in reversed(numlst):
   res = elem * elem
print(res)
   
# Output:
# 2500



# index based iterator :-
# -----------------------
# special-class - range(start,stop,step)
#                  - range(start,stop)
#                  - range(start,stop)
# read-write acess on collection - LIST
# bit slow

numlst = [10,20,30,40,50]

for index in range(len(numlst)):
   numlst[index] = numlst[index] * numlst[index]
 
print(numlst)

# Output:
# [100, 400, 900, 1600, 2500]


# enumerate iterator:-
# --------------------
# special function - enumerate
# bit-slow
# suitable ONLY FOR  list


numlst = [10,20,30,40,50]

for index,value  in  enumerate(numlst):
   print(index,value)

# Output:
# 0 10
# 1 20
# 2 30
# 3 40
# 4 50


# parallel iterator:-
# --------------------
# Special function - zip(iter1,iter2)
# truncates to the smallest list


alst = ["indore", "bhopal", "pune", "banglore", "gurugram"]
blst = [10,20,30,40,50]

for loc,val in zip(alst,blst):
    print(loc,val)

# Output:
# indore 10
# bhopal 20
# pune 30
# banglore 40
# gurugram 50



# When to use which itertor?

# forward/reverse/index-based/enumerate/parallel

# traverse on a tuple   - forward
# when doing inplace operation on list - index-based
# traverse on 4 lists   - enumerate, parallel
# traverse on a set     - forward
# traverse a dict       - forward
# read the file         - forward