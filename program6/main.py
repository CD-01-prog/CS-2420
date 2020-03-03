
#Test your program on several expressions, such as "x*x*x/(2*5)".
from graphics import *

class CoreStack:

  def __init__(self):
    self.items = []

  def Size(self):
    return len(self.items)

  def push(self, item):
    self.items.append(item)

  def pop(self):
    if self.Size() <= 0:
	    print("she is giving all that she got captain")
	    return
    return self.items.pop()
  
  def Seek(self, warrent):
    if warrent in self.items:
      return True
    return False

  def TopLook(self):
    return self.items[-1]

  
def InfixToPostfix(Infix):
  s = CoreStack()
  Postfix = ''
  Infix = str(Infix)
  for c in Infix:
    if c in '0123456789xX':
      Postfix += c
    elif c == '^':
      if s.TopLook('^'):
        Postfix += c
        s.push('^')
      else:
        s.push('^')
    elif c in '*/':
      if s.seek('*') or s.seek('/'):
        s.push('*')
        s.push('/')
    elif c in '+-':
      if c == '-':
        s.push('-')
      else:
        s.push('+')
    elif c == '(':
      s.push('(')
    elif c == ')':
      s.push(')')
    elif c == ' ':
      pass
    else:
      print('Error unrecognized character')
      return
  for i in range(s.Size()):
    LastOperators = s.pop()
    Postfix += LastOperators
  print(Postfix)
  return Postfix


def EvaluatePostfix(postfix,x):
  s = CoreStack()
  for c in postfix:
    if c.isdigit:
      s.push(c)
    elif c in 'xX':
      s.push(x)
    elif c == '-':
     rhs = c.pop()
     lhs = c.pop()
     result = lhs - rhs
     s.push(result)
    elif c == '+':
      rhs = c.pop()
      lhs = c.pop()
      result = lhs + rhs
      s.push(result)
    elif c == '*':
      rhs = c.pop()
      lhs = c.pop()
      result = lhs * rhs
      s.push(result)
    elif c == '/':
      rhs = c.pop()
      lhs = c.pop()
      reulst = lhs / rhs
      s.push(result)
  total = s.pop()
  print(total)
  return total


def PrintInstructions():
    print("This program can take expressions that consists of single digit integers, the variable x, the operators +, -, /, and *, and parenthesis.")
    
def main():
    PrintInstructions()
    infix = input("Enter your formula here: ")
    postfix = InfixToPostfix(infix)
                  
    # Generate the point data:
    X = []
    Y = []
    
    XLOW = -10
    YLOW = -10
    XHIGH = +10
    YHIGH = +10
    XINC = .1
        
    x = XLOW
    while x <= XHIGH:
        y = EvaluatePostfix(postfix, x)
        X.append(x)
        Y.append(y)
        x += XINC

    # Draw the point data:
    win = GraphWin("Graphing Calculator", 600, 600)
    win.setCoords(XLOW,YLOW, XHIGH,YHIGH)
    for i in range(len(X)-1):
        p1 = Point(X[i], Y[i])
        p2 = Point(X[i+1], Y[i+1])
        l = Line(p1, p2)
        l.draw(win)
        
    #c = Circle(Point(50,50), 10)
    #c.draw(win)

    # Wait for the user to click, then quit.
    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()
