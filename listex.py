def try_to_change_list_contents(the_list):
    print 'got', the_list
    the_list.append('four')
    print 'changed to', the_list
import dis

outer_list = ['one', 'two', 'three']

print 'before, outer_list =', outer_list
dis.dis(try_to_change_list_contents(outer_list))
print 'after, outer_list =', outer_list
