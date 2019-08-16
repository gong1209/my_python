
while True:
    first=input("First number :")
    second=input("Second number :")
    try:
        ans=int(first)/int(second) # 因為input都是字串所以要轉int才能相除
    except ZeroDivisionError:
        print("You can't divide by zero")
    else:
        print(ans) # 若沒有出錯就印出兩個值相除
        break 

#  引發例外 raise
class InputError(Exception):
    pass
a= input("輸入1~100數字:")
a= int(a)
try:
    if a<=0 or a>=100:
        raise InputError
except  InputError:
    print("輸入錯誤")
else:
    print(a)








'''Python內建的例外層級結構
BaseException 
 +--  SystemExit 
 +--  KeyboardInterrupt 
 +--  GeneratorExit 
 +--  Exception 
      +--  StopIteration 
      +--  ArithmeticError 
      |     +--  FloatingPointError 
      |     +--  OverflowError 
      |     +--  ZeroDivisionError 
      +--  AssertionError 
      +--  AttributeError 
      +--  BufferError 
      +--  EOFError 
      +--  ImportError 
      +--  LookupError 
      |     +--  IndexError 
      |     +--  KeyError 
      +--  MemoryError 
      +--  NameError 
      |     +--  UnboundLocalError 
      +--  OSError 
      |     +--  BlockingIOError 
      |     +--  ChildProcessError 
      |     +--  ConnectionError 
      |     |     +--  BrokenPipeError 
      |     |     +--  ConnectionAbortedError 
      |     |     +--  ConnectionRefusedError 
      |     |     +--  ConnectionResetError 
      |     +--  FileExistsError 
      |     +--  FileNotFoundError 
      |     +--  InterruptedError 
      |     +--  IsADirectoryError 
      |     +--  NotADirectoryError 
      |     +--  PermissionError 
      |     +--  ProcessLookupError 
      |     +--  TimeoutError 
      +--  ReferenceError 
      +--  RuntimeError 
      |     +--  NotImplementedError 
      +--  SyntaxError 
      |     +--  IndentationError 
      |          +--  TabError 
      +--  SystemError 
      +--  TypeError 
      +--  ValueError 
      |     +--  UnicodeError 
      |          +--  UnicodeDecodeError 
      |          +--  UnicodeEncodeError 
      |          +--  UnicodeTranslateError 
      +--  Warning 
           +--  DeprecationWarning 
           +--  PendingDeprecationWarning 
           +--  RuntimeWarning 
           +--  SyntaxWarning 
           +--  UserWarning 
           +--  FutureWarning 
           +--  ImportWarning 
           +--  UnicodeWarning 
           +--  BytesWarning 
           +--  ResourceWarning
'''


















