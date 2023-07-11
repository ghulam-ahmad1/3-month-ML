def my_function(*kids):
  print("The youngest child is " + str(kids))
my_function("Emil", "Tobias", "Linus")

def my_function(**kid):
  print('His first name is : '+kid['fname'])
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0 
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

