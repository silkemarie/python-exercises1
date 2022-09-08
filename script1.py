import sys

def main(a):

    if a[1] == 'Claus':
        print('Hello ' + a[1])
    else:
        print('Hello ' + str(a))

main(sys.argv)