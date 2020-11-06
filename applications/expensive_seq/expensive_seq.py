# Your code here
my_dict = {}

def expensive_seq(x, y, z):
    # Your code here
    my_dict.update({(0,0,0) : 0})
    if x <=0:
        return y+z
    if x > 0:
        if (x,y,z) in my_dict:
            return my_dict[(x,y,z)]
        
        my_dict[(x,y,z)] = expensive_seq(x-1, y+1, z) + expensive_seq(x-2, y+2, z*2) + expensive_seq(x-3, y+3, z*3)
        return my_dict[(x, y, z)]

if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
