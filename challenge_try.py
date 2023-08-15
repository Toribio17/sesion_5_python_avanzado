class challenge:
    
    def __init__(self):
        print("The constructor")
        
    def challenge_1(self):
        try:
            list_num = [1, 2, 3, 4, 5] 
            
            print(list_num[10])
        
        except IndexError as e:
            print("you are trying print an index not available")
        
        
    def add_value_list(self,value):
        try:
            list_values = [1,2,3,4]
            
            if value in list_values:
                raise ValueError("Error: Imposible añadir elementos duplicados => [elemento]")
            else:
                list_values.append(value)
        except ValueError as r:
            print(r)
            
    def challenge_3(self):
        try:
            colores = { 'rojo':'red', 'verde':'green', 'negro':'black'} 

            print(colores['blanco'])
        except KeyError as r:
            print("This Dict does not include the Keyword 'blanco', please add it before it")
    

if __name__ == '__main__':
    obj = challenge()
    #obj.challenge_1()
    obj.add_value_list(3)
    obj.challenge_3()
    