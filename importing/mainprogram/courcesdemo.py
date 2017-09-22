from .indexer import mymodule

courses = ['History', 'Math', 'Physics', 'CompSci']

def main():
    the_course = mymodule.find_index(courses, 'Math')
    print (the_course)

