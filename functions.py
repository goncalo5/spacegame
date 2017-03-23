# Metal Mine => metal_mine
def transform_name(name):
    name = name.lower()
    name = name.split()
    new = ''
    for word in name:
        new += word + '_'
    return new[:-1]
#print transform_name('Metal Mine')


# 'metal_mine' => 'MetalMine'
def change2object_name(name, first_word=''):
    res = ''
    name = name.split('_')
    for word in name:
        res += word[0].upper() + word[1::]
    return first_word + res
#print change2object_name('metal_mine', 'Menu')