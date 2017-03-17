# Metal Mine => metal_mine
def transform_name(name):
    name = name.lower()
    name = name.split()
    new = ''
    for word in name:
        new += word + '_'
    return new[:-1]
#print transform_name('Metal Mine')