class try_clas:
    
    def __init__(self):
        print("The constructor")
        
    
    def divide(self):
        
        while True:
            try:
                number_1 = int(input("Enter a number"))
                number_2 = int(input("Enter denominator"))
                
                result = number_1/number_2
                
                if number_1 >= 0 and number_2 >= 0:
                    print("integer Numbers")
                else:
                    print("negative Numbers")
            
            except ZeroDivisionError as e:
                print("Zero Division Error: ", e)
            except ValueError as r:
                print("Value Error: ", r)
            else:
                print("Else was executed because an exception not occurred")
                print("The result is",result)
                break
    
    def divide_raise(self):
        while True:
            try:
                number_1 = int(input("Enter a number"))
                number_2 = int(input("Enter denominator"))
                
                result = number_1/number_2
                
                if number_1 >= 0 and number_2 >= 0:
                    print("integer Numbers")
                else:
                    raise Exception("Negative number")
                    #print("negative number")
            
            except ZeroDivisionError as e:
                print("Zero Division Error: ", e)
            except ValueError as r:
                print("Value Error: ", r)
                #se ejcutará solo si ninguna except sucede
            else:
                print("Else was executed because an exception not occurred")
                break
            finally:
                print("The result is",result)
                print("finally always executes")
                
    def raise_example_two(self):
        s = 'apple'

        try:
            num = int(s)
        except:
            print("problem")
            raise
            

if __name__ == '__main__':
    
    obj = try_clas()
    
    obj.divide()
    #obj.divide_raise()
    #obj.raise_example_two()