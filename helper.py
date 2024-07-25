def getEntityByField(array, field, value):
    for row in array:
        if str(row.get(field)) == str(value):
            return row
    return None

def handleParams(params):
    l = list(params.keys())
    if l:
        field = l[0]
        value = params[field]
        return [field, value]

    return [None, None]