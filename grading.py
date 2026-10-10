subjects=int(input())


for i in range(subjects):
    grad=int(input())
    if grad<38:
        print(grad)
    else:
        remai=5-(grad%5)
        if remai<3:
            print(remai+grad)
        else:
            print(grad)
    subjects-=1
