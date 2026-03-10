 // program to print the total number of note
let amount = Number(prompt("enter the amount"))
let note = 0
if (isNaN(amount) || amount < 0) {
    alert("you should give valid input ")
}
else if (amount === 0) {
    alert("you should give a value ")
} else {
    console.log("total amount is :-",amount);

    if (amount > 500) {
        note = parseInt(amount / 500)
        console.log("500  repees", note);
        amount %= 500
    }
    if (amount > 200) {
        note = parseInt(amount / 200)
        console.log("200  repees", note);
        amount %= 200
    }
    if (amount > 100) {
        note = parseInt(amount / 100)
        console.log("100  repees", note);
        amount %= 100
    }
    if (amount > 50) {
        note = parseInt(amount / 50)
        console.log("50  repees", note);
        amount %= 50
    }
    if (amount > 20) {
        note = parseInt(amount / 20)
        console.log("20  repees", note);
        amount %= 20
    }
    if (amount > 10) {
        note = parseInt(amount / 10)
        console.log("10 repees", note);
        amount %= 10
    }
    if (amount > 5) {
        note = parseInt(amount / 5)
        console.log("5 repees", note);
        amount %= 5
    }
    if (amount > 2) {
        note = parseInt(amount / 2)
        console.log("2 repees", note);
        amount %= 2
    }
    if (amount >= 1) {
        note = parseInt(amount / 1)
        console.log("1 rupees", note);
        amount = 1
    }
}
// else{
//     console.log("you should give valid input ")
// }