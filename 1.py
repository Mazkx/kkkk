from catalog.models import Book, Author, BookInstance, Genre

sender = Book
for fieldname in sender._meta.get_fields():
 try:
  print("normal lllllllllllllllll %s \n" % fieldname)
  print("nthhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh\n")
  m = re.search(r'(.+)\.(\S+)',fieldname)
  print("m.group(2) %s\n"   %   m.group(2))
  field = sender._meta.get_field(m.group(2))
except:
  print("fail\n")
