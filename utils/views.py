from django.shortcuts import render

def group_queryset(n,queryset,fill=True):
    result = []
    temp = []

    for q in queryset:
        temp.append(q)
        if len(temp) == n:
            result.append(temp)
            temp = []
    # if fill:
    #     result.append(temp)

    return result
    


