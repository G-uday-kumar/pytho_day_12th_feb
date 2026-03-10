// prog to calculate the total amount total electric units consumed
// condition 0-100 units4 rupess/unit
// 100-200 6 ru/units
// 200- 400 units 8 rupees
// >400 10 per unit 
let units=Number(prompt("enter units consumed"));
let amount=0;
let rem_unit=0
if(units<0||isNaN(units)){
    alert("enetr number only");
} 
else{
    if(units>400){
        amount+=(units-400)*10
        units=400
    }
    if(units>200){
        amount+=(units-200)*8
        units=200
    }
    if(units>100){
        amount+=(units-100)*6
        units=100
    }
    if(units>0){
        amount+=(units-0)*4

    }
    else{
        alert("provide proper input")
    }
    console.log("total=",amount);
}