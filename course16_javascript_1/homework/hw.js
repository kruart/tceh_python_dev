'use strict';
function isNumber(n) {
    return !isNaN(parseFloat(n)) && isFinite(n);
}

// 1. Напишите программу, которая считает площадь прямоугольника, спрашивая у пользователя длину двух сторон
function squareRectangle() {
    let a, b;

    while(true) {
        a = prompt("Input side A of the rectangle");
        if (isNumber(a)  && Number(a) >= 0) {
            break;
        }
    }

    while(true) {
        b = prompt("Input side B of the rectangle");
        if (isNumber(b)  && Number(a) >= 0) {
            break;
        }
    }

    return Number(a) * Number(b);
}


// 2. Напишите программу, которая спрашивает у пользователя два числа и знак: "+" или "-". В зависимости от знака выводит их сумму или разницу
function plusOrMinus() {
    let number1, number2, sign;
    while(!isNumber(number1)) {
        number1 = Number(prompt("Input first number"));
    }
    while(!isNumber(number2)) {
        number2 = Number(prompt("Input second number"));
    }
    while(sign !== '+' && sign !== '-') {
        sign = prompt("Input a plus or minus sign");
    }

    return sign === "+" ? number1 + number2 : number1 - number2
}


// 3. Напишите программу, которая находит все простые числа между 0 и пользовательским числом
function isPrime(num) {
    if(num < 2) return false;
    for (let i = 2; i < num; i++) {
        if(num % i === 0)
            return false;
    }
    return true;
}


function printAllPrimeNumbers() {
    let user_number;
    while (!isNumber(userNumber)) {
        userNumber = Number(prompt("Input your number"))
    }

    for (let i = 0; i < userNumber; i++) {
        if (isPrime(i))
            console.log(i);
    }
}

// 4. Напишите программу, которая выводит все кратные 5 числа между двумя пользовательскими числами
function printNumbers() {
    let number1, number2, multipleNumbers = [];

    while(!isNumber(number1)) {
        number1 = Number(prompt("Input first number"));
    }
    while(!isNumber(number2)) {
        number2 = Number(prompt("Input second number"));
    }

    for (let i = number1; i < number2; i++) {
        if (i % 5 === 0)
            multipleNumbers.push(i)
    }

    return multipleNumbers;
}

// 5. Создать лист из 6 любых чисел. Отсортировать его по возрастанию
let myList = [25, -23, 77, -123, 4, 0];
myList.sort(function(a, b) {
    return a - b;
});
console.log(myList);
// 6. Создать словарь из 5 пар: int -> str, например {6: '6'}, вывести его в консоль попарно
let my_dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f'};

for (let key in my_dict) {
    console.log(key + '==>' + my_dict[key]);
}

// 7. Создать tuple из 10 любых дробных чисел, найти максимальное и минимальное значение в нем
let floatList = [];
for (let i = 0; i < 10; i++) {
    let randomFloat = (Math.random() * 100).toFixed(2);
    floatList.push(randomFloat);
}

//create tuple
const color = [floatList];


// 8. Создать лист из 3 слов: ['Earth', 'Ukraine', 'Kyiv'], соеденить все слова в единую строку, чтобы получилось: 'Earth -> Ukraine -> Kyiv'
let strList = ['Earth', 'Ukraine', 'Kyiv'];

console.log(strList.join(' -> '));


// 9. Взять строку '/bin:/usr/bin:/usr/local/bin' и разбить ее в список по символу ':'
let someStr = '/bin:/usr/bin:/usr/local/bin';
let someList = someStr.split(':');
console.log(someList);


// 10. Пройти по всем числам от 1 до 100, написать в консоль, какие из них делятся на 7, а какие - нет
let divided = [];
let notDivided = [];

for (let i = 0; i < 100; i++) {
    if (i % 7 === 0) {
        divided.push(i)
    } else {
        notDivided.push(i)
    }
}

console.log('Divided numbers: ' + divided);
console.log('Not Divided numbers: ' + notDivided);


// 11. Создать матрицу любых чисел 3 на 4, сначала вывести все строки, потом все столбцы
function matrix() {
    let matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]];

    for (let i = 0; i < matrix.length; i++) {
        console.log("Line" + i + ": " + matrix[i]);
    }


    let column = [];
    for (let i = 0; i < matrix[0].length; i++) {
        for (let j = 0; j < matrix.length; j++) {
            column.push(matrix[j][i]);
        }
        console.log("Column: " + i + ": " + column);
        column = [];
    }
}


// 12. Создать список любых объектов, в цикле напечатать в консоль: объект и его индекс
let objectList = [{some: "somestr", any: 'anystr'}];

for (let index in objectList) {
    console.log(objectList + " its index = " + index)
}


// 13. Создать список с тремя значениями 'to-delete' и нескольми любыми другими, удалить из него все значения 'to-delete'
let checkList = [1, 'to-delete', 2, 'to-delete', 3, 4, 'to-delete', 5];

for (let i in checkList) {
    if (checkList[i] === 'to-delete') {
        checkList.splice(i, 1)
    }
}

console.log(checkList);


// 14. Пройти по всем числам от 1 до 10 в обратную сторону (то есть: от 10 до 1), напечатать их в консоль
for(let i = 10; i > 0; i--) {
    console.log(i);
}