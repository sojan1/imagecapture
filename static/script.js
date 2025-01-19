function capture_event() {
    //document.getElementById("status").innerText="";
    showLoader();

    fetch('/capture_event') 
        .then(response => response.json())  
        .then(data => {
            //document.getElementById("status").innerText = data.message;
            hideLoader()
            if (data.message=="True"){
                //alert(data.message);
                load_events();
            }else{
                alert("Error Occured");
            }
            
        })
        .catch(error => {
            //document.getElementById("status").innerText = "An error occurred.";
            hideLoader()
        });
    
}

 function load_events() {
    document.getElementById("events").innerHTML="";
    fetch('/load_events') 
        .then(response => response.text())  
        .then(data => {
            document.getElementById("events").innerHTML = data;
            
        })
        .catch(error => {
            document.getElementById("events").innerHTML = "An error occurred.";
        });
        
}

function showLoader() {
document.getElementById('loader').style.display = 'block';
}

function hideLoader() {
document.getElementById('loader').style.display = 'none';
}
