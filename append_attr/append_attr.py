cellRecAttrs = {
    u'C.Acoustic': ('acousticSpace',),
    u'C.Climate': ('climate',),
    u'C.Encounter': ('encounterZone',),
    u'C.ImageSpace': ('imageSpace',),
    u'C.Location': ('location',),
    u'C.Music': ('music',),
    u'C.Name': ('full',),
    u'C.Owner': ('ownership',),
    u'C.RecordFlags': ('flags1',),
    u'C.SkyLighting': ('',),
    u'C.Regions': ('regions',),
    u'C.Water': ('water', 'waterHeight', 'waterNoiseTexture',
    'waterEnvironmentMap',),
}
cellRecFlags = {
    u'C.Acoustic': ('',),
    u'C.Climate': ('showSky',),
    u'C.Encounter': ('',),
    u'C.ImageSpace': ('',),
    u'C.Location': ('',),
    u'C.Music': ('',),
    u'C.Name': ('',),
    u'C.Owner': ('publicPlace',),
    u'C.RecordFlags': ('valu1', 'value2',),
    u'C.SkyLighting': ('useSkyLighting',),
    u'C.Regions': ('',),
    u'C.Water': ('hasWater',),
}
print cellRecAttrs
print cellRecFlags
print "cellRecAttrs:"
for tags in cellRecAttrs:
    print "x: ", tags, ", atrs: ", cellRecAttrs[tags]
    print "Length of: ", tags, " = ", len(tags), \
        ", Length of cellRecAttrs[x] : ", len(cellRecAttrs[tags])
    print
    # for attr in tags
    # print "This is attr: ", attr
    print
print
print "cellRecFlags:"
for x in cellRecFlags:
    print "x: ", x, "atrs: ", cellRecFlags[x]
    print "Length of: ", x, " = ", len(x), \
        "Length of cellRecFlags[x] : ", len(cellRecFlags[x])
    print

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for list in list_of_lists:
    for x in list:
        print x
print


class Iterable(object):
    def __init__(self, values):
        self.values = values
        self.location = 0

    def __iter__(self):
        return self

    def next(self):
        if self.location == len(self.values):
            raise StopIteration
        value = self.values[self.location]
        self.location += 1
        return value


attributes = ['water', 'waterHeight', 'waterNoiseTexture',
    'waterEnvironmentMap']
print Iterable(attributes)
print Iterable(attributes).next

print
class print_hi_not_bye:
  def __init__(self):
    self.name = "King"

  def hi(self):
    print(self.name)

class_alias = print_hi_not_bye()
class_alias.hi()  # prints King

print

answer = 11 / 3
remainder = 11 % 3
string1 = "the answer is"
string2 = "with a remainder of"
print "%s %d %s %d" % (string1, answer, string2, remainder)

print

astring = "Hello Big World!"
print "Hello = ", astring[0:5]
print "Big = ", astring[6:9]
print "World = ", astring[10:16]
print "H = ", astring[0]
print "B = ", astring[6]
print "W = ", astring[10]
print "Just B = ", astring[6:9:3]
print "B and g not i = ", astring[6:9:2]

word_array= ['R', 'e', 'd', ' ', 'T', 'w', 'o', ' ', 'B', 'i', 'g']
print word_array
print len(word_array)
print


#R | e | d |   | T | w | o |   | B | i | g
#0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10
new_string = "Red Two Big"
print "Red = ", new_string[-4:-0]
print "Two = ", new_string[4:7]
print "Big = ", new_string[8:11]
print "RTB = ", new_string[0:10:4]
print

new_string = "Red Two Big"
print "g = ", new_string[-1]
print "i = ", new_string[-2]
print "B = ", new_string[-3]
something = new_string[-1:-4]
print len(something)
print "[empty] = ", new_string[-1:-4]
other = new_string[-4:-1]
print len(other)
print " Bi = ", other

