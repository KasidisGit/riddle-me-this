var ans = document.getElementById("input");
var ansKey = document.getElementById("ansKey");

$("#input").keypress(function(event) { 
    if (event.keyCode == 13) { 
        $("#sub_btn").click();
        event.preventDefault();
    } 
});

$("#sub_btn").click(function() { 
    if (ans.value == ansKey.value) {
        console.log(true)
    }
    else {
        console.log(false)
        ans.value = ''
    }
}); 

function hint() {
    var ranChar = '';
    var characters = ansKey.value
    var charactersLength = characters.length;
    ranChar = characters.charAt(Math.floor(Math.random() * charactersLength));
    alert(ranChar)
}