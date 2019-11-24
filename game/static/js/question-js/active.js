var ans = document.getElementById("input");
var ansKey = document.getElementById("ansKey");

$("#input").keypress(function(event) { 
    if (event.keyCode == 13) { 
        $("#sub_btn").click();
        event.preventDefault();
    } 
});

$("#sub_btn").click(function() { 
    // $("#status").show();
    // $("#status").hide(4000);
    document.getElementById("status").style.visibility = "hidden";
    document.getElementById("status").style.visibility = "visible";
}); 

function hint() {
    var ranChar = '';
    var characters = ansKey.value
    var charactersLength = characters.length;
    ranChar = characters.charAt(Math.floor(Math.random() * charactersLength));
    alert(ranChar)
}

function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
    document.getElementById("opennav").style.display = "none";
}
  
  function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("opennav").style.display = "block";
}