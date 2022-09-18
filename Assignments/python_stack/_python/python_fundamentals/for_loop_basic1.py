
def basic():
    for i in range(0, 151):
        print(i)



def multiples_of_five():
    for i in range(1,200):
        print(i*5)



def counting_the_dojo_way():
    for i in range(1,100):
        if((i % 5 == 0)):
            print("Coding")
        if((i % 10 == 0)):
            print("Coding Dojo")



# Whoa. That Sucker's Huge
def sumofoddints ():
    sum = 0
    for num in range (0, 500000):
        if num % 2 == 1:
            sum += num
    print(sum)
    return sum

# Print positive numbers starting at 2018, counting down by fours.
def countdown_by_fours():
    for num in range(2018,0,-4):
        print(num)

def flexible_counter(lowNum,highNum,mult):
    for num in range(lowNum,highNum):
        if(num % mult == 0):
            print(num)


# multiples_of_five()
# counting_the_dojo_way()
# sumofoddints ()
# countdown_by_fours()
# flexible_counter(0,100,9)