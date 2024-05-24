model_id = 'ft:gpt-3.5-turbo-0125:ssd:150-robot:9HnES2yH'

def fibonacci(n):
       if n >1: 
            result = fibonacci(n-1) + fibonacci(n-2)
          #   print(result)
            return result
       else:      
            return n
       
result = fibonacci(int(input("Enter number: ")))
print(result)