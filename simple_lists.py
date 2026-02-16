a = []
a = [1,2,3,4,5,6]
print(a)
a = [True, [1,"Bob", -8.2], False, "Jamaica", 99.99]
print(a)
print(len(a)) #amount of items in the list

print(a[2])
a[2] = "No longer FALSE" #list is mutable
print(a)

print(a[::-1])
print(a[2::2])
print([ 1, 2, 3]+["Bob","Bob", "BOBOBOBOB"])
print([1, 2, 9]*4)
a = ["Bob", "James", "Jane"]
for item in a: #iterate over a list
    print(item)