import addition 
import subtraction              #or import addition,subtraction,multiplication,division
import multiplication,division

add1=addition.addition_1(3,5)

subt=subtraction.subtraction_1(10,40)

multi=multiplication.multiplication_1(5,10) #x:int y:int

div=division.division_1(10,2)  #(x: Any, y: Any) -> (Any | Literal['enter number greater than zero'])
print(f"addition is {add1},subtraction value is {subt},multiplication value is {multi},and division value is {div}")
