import UIKit

var str = "Hello, playground"

func swapTwoValues<T>(_ a: inout T, _ b: inout T) {
    let temporaryA = a
    a = b
    b = temporaryA
}

func swapTwoStrings(_ a: inout String, _ b: inout String) {
    let temporaryA = a
    a = b
    b = temporaryA
}

var someIntOne = 23
var someIntTwo = 45
print(someIntOne,someIntTwo)
swapTwoValues(&someIntOne, &someIntTwo)
//swapTwoStrings(&someIntOne, &someIntTwo) cannot be done since of INT type
print(someIntOne,someIntTwo)

var stringOne = "Hello"
var stringTwo = "World"
print(stringOne,stringTwo)
swapTwoValues(&stringOne, &stringTwo)
print(stringOne,stringTwo)

func printArray<T>(a: [T]) {
    for item in a {
        print (item)
    }
}

print(printArray(a: ["1",2,"hello"]))
