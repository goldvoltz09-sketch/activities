def perimeterofrectangle(length, breadth):
    perimeter= 2 * (length + breadth)
    print('the perimeter of the rectangle is', perimeter)
def perimeterofsquare(side):
    perimeter= 4 * side
    print('the perimeter of the square is', perimeter)
    print('select the shape to calculate perimeter -\n')
    print('a. Rectangle\n',
       'b. Square\n')
choice=input('Enter choice(a/b): ')
if choice=='a':
     length=int(input('Enter the length of the rectangle: '))
     breadth=int(input('Enter the breadth of the rectangle: '))
     perimeterofrectangle(length, breadth)
elif choice=='b':
     side=int(input('Enter the side of the square: '))
     perimeterofsquare(side)
else:
     print('Invalid input')