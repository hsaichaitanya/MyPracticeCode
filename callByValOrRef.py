def try_to_change_list_contents(the_list):
    print 'got', the_list
    the_list = [1,2,3]
    print 'changed to', the_list

outer_list = ['one', 'two', 'three']

print 'before, outer_list =', outer_list
try_to_change_list_contents(outer_list)
print 'after, outer_list =', outer_list
