def distance(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

def type(left, right):

    total = 0

    for s in string:
        total+=1
        
        if keyboard[s][0]=="l":
            total += distance(keyboard[s][1], keyboard[s][2], keyboard[left][1], keyboard[left][2])
            left = s
        
        elif keyboard[s][0]=="r":
            total += distance(keyboard[s][1], keyboard[s][2], keyboard[right][1], keyboard[right][2])
            right = s
        else:
            continue
    return total


keyboard = {
  'q':('l',0,0),
  'w':('l',0,1),
  'e':('l',0,2),
  'r':('l',0,3),
  't':('l',0,4),
  'a':('l',1,0),
  's':('l',1,1),
  'd':('l',1,2),
  'f':('l',1,3),
  'g':('l',1,4),
  'z':('l',2,0),
  'x':('l',2,1),
  'c':('l',2,2),
  'v':('l',2,3),
  'y':('r',0,5),
  'u':('r',0,6),
  'i':('r',0,7),
  'o':('r',0,8),
  'p':('r',0,9),
  'h':('r',1,5),
  'j':('r',1,6),
  'k':('r',1,7),
  'l':('r',1,8),
  'b':('r',2,4),
  'n':('r',2,5),
  'm':('r',2,6),
}

left, right = input().split()
string = input()

print(type(left, right))