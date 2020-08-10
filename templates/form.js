var servResponse = document.querySelector('#response');

document.forms.ourForm.onsubmit = function(e){
    e.preventDefault();

    var userInput = document.forms.ourForm.name.value;
    userInput = encodeURIComponent(userInput);

    var xhr = XMLHttpRequest();

    xhr.open('POST', 'form.php?' + 'name=' + userInput);

};
