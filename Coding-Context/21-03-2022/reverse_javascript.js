
function reverseString(str) {

    var newString = "";
    for (var i = str.length - 1; i >=0; i--) {
        newString += str[i]
    }

    return newString
}
function FirstReverse(str) {
    var backwardDString = ""
    var splitString = str.split("")

    for (var i = splitString.length -1; i >=0 ; i--)  {
        backwardDString +=splitString[i]
    }

    return backwardDString
}

console.log(reverseString("otepa"))

console.log(FirstReverse("otepa wembo dfshfjksdhfjksf snmdfbvskfgksdjfgksjdfsd fsdfgdsfgdsfhdsfds fsdfsgdfhsgdfhsdf sdfgsdhfgsdhfgsdghfgsdghfgdjsgfgsdfghsd fsdfgsdfjyrwejrwerhhjds f23423462734g2v2342834234h ''''''''sdf'sd'f'''sdf"))