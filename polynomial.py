
class X:
   def __init__(self):
       pass

   def __repr__(self):
       return "X"

   def evaluate(self, x_value):
       # TODO: Implement evaluation for variable X
       # Should return an Int object with the given x_value
       return Int(x_value)

   def simplify(self):
       # TODO (Optional Exercise): Implement simplification
       # X cannot be simplified further, so return self
       pass




class Int:
   def __init__(self, i):
       self.i = i


   def __repr__(self):
       return str(self.i)


   def evaluate(self, x_value):
       # TODO: Implement evaluation for integer constant
       # Should return an Int object with the stored integer value
       return self


   def simplify(self):
       # TODO (Optional Exercise): Implement simplification
       # Integer constants cannot be simplified further, so return self
       pass




class Add:
   def __init__(self, p1, p2):
       self.p1 = p1
       self.p2 = p2


   def __repr__(self):
       return repr(self.p1) + " + " + repr(self.p2)


   def evaluate(self, x_value):
       # TODO: Implement evaluation for addition
       # Should evaluate both operands and return their sum
       left = self.p1.evaluate(x_value).i
       right = self.p2.evaluate(x_value).i
       return Int(left + right)


   def simplify(self):
       # TODO (Optional Exercise): Implement simplification
       # Examples: X + 0 -> X, 0 + X -> X, 3 + 5 -> 8
       # Hint: Simplify operands first, then apply simplification rules
       pass




class Mul:
   def __init__(self, p1, p2):
       self.p1 = p1
       self.p2 = p2


   def __repr__(self):
       if isinstance(self.p1, Add):
           if isinstance(self.p2, Add):
               return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
           return "( " + repr(self.p1) + " ) * " + repr(self.p2)
       if isinstance(self.p2, Add):
           return repr(self.p1) + " * ( " + repr(self.p2) + " )"
       return repr(self.p1) + " * " + repr(self.p2)


   def evaluate(self, x_value):
       # TODO: Implement evaluation for multiplication
       # Should evaluate both operands and return their product
       left = self.p1.evaluate(x_value).i
       right = self.p2.evaluate(x_value).i
       return Int(left * right)


   def simplify(self):
       # TODO (Optional Exercise): Implement simplification
       # Examples: X * 0 -> 0, X * 1 -> X, 3 * 5 -> 15
       # Hint: Simplify operands first, then apply simplification rules
       pass


class Sub:
   def __init__(self, p1, p2):
       self.p1 = p1
       self.p2 = p2


   def __repr__(self):
       if isinstance(self.p1, Add) or isinstance(self.p1, Mul):
           left = f"( {repr(self.p1)} )"
       else:
           left = repr(self.p1)


       if isinstance(self.p2, Add) or isinstance(self.p2, Mul):
           right = f"( {repr(self.p2)} )"
       else:
           right = repr(self.p2)


       return f"{left} - {right}"


   def evaluate(self, x_value):
       # Evaluate both operands and return their difference as an Int
       left = self.p1.evaluate(x_value).i
       right = self.p2.evaluate(x_value).i
       return Int(left - right)
  
   def simplify(self):
       simplified_p1 = self.p1.simplify()
       simplified_p2 = self.p2.simplify()


       # Simplification rules
       if isinstance(simplified_p2, Int) and simplified_p2.i == 0:
           return simplified_p1  # X - 0 -> X
       if isinstance(simplified_p1, Int) and isinstance(simplified_p2, Int):
           return Int(simplified_p1.i - simplified_p2.i)  # 5 - 3 -> 2


       return Sub(simplified_p1, simplified_p2)


class Div:
   def __init__(self, p1, p2):
       self.p1 = p1
       self.p2 = p2


   def __repr__(self):
       if isinstance(self.p1, Add) or isinstance(self.p1, Mul) or isinstance(self.p1, Sub):
           left = f"( {repr(self.p1)} )"
       else:
           left = repr(self.p1)


       if isinstance(self.p2, Add) or isinstance(self.p2, Mul) or isinstance(self.p2, Sub):
           right = f"( {repr(self.p2)} )"
       else:
           right = repr(self.p2)


       return f"{left} / {right}"


   def evaluate(self, x_value):
       # Evaluate both operands and return their quotient as an Int
       numerator = self.p1.evaluate(x_value).i
       denominator = self.p2.evaluate(x_value).i
       if denominator == 0:
           raise ZeroDivisionError("Division by zero is not allowed.")
       return Int(numerator // denominator)


   def simplify(self):
       simplified_p1 = self.p1.simplify()
       simplified_p2 = self.p2.simplify()


       # Simplification rules
       if isinstance(simplified_p2, Int) and simplified_p2.i == 1:
           return simplified_p1  # X / 1 -> X
       if isinstance(simplified_p1, Int) and isinstance(simplified_p2, Int):
           if simplified_p2.i == 0:
               raise ZeroDivisionError("Division by zero is not allowed.")
           return Int(simplified_p1.i // simplified_p2.i)  # 6 / 2 -> 3


       return Div(simplified_p1, simplified_p2)




# Original polynomial example
poly = Add(Add(Int(4), Int(3)), Add(X(), Mul(Int(1), Add(Mul(X(), X()), Int(1)))))
print("Original polynomial:", poly)


# Test new Sub and Div classes (will fail until implemented)
print("\n--- Testing Sub and Div classes ---")
try:
   sub_poly = Sub(Int(10), Int(3))
   print("Subtraction:", sub_poly)
except Exception as e:
   print("❌ Subtraction test failed - Sub class not implemented yet")


try:
   div_poly = Div(Int(15), Int(3))
   print("Division:", div_poly)
except Exception as e:
   print("❌ Division test failed - Div class not implemented yet")


# Test evaluation (will fail until implemented)
print("\n--- Testing evaluation ---")
try:
   simple_poly = Add(Sub(Mul(Int(2), X()), Int(1)), Div(Int(6), Int(2)))
   print("Test polynomial:", simple_poly)
   result = simple_poly.evaluate(4)
   print(f"Evaluation for X=4: {result}")
except Exception as e:
   print("❌ Evaluation test failed - evaluate methods not implemented yet")


try:
   original_result = poly.evaluate(2)
   print(f"Original polynomial evaluation for X=2: {original_result}")
except Exception as e:
   print(
       "❌ Original polynomial evaluation failed - evaluate methods not implemented yet"
   )


# Option to run comprehensive tests
if __name__ == "__main__":
   import sys


   if len(sys.argv) > 1 and sys.argv[1] == "--test":
       print("\n" + "=" * 60)
       print("Running comprehensive test suite...")
       print("=" * 60)
       from test_polynomial import run_all_tests


       run_all_tests()
   else:
       print("\n💡 To run comprehensive tests, use: python polynomial.py --test")
       print("💡 Or run directly: python test_polynomial.py")

