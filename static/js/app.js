function copyFunction() {
    var copyText = document.getElementById("result");
    copyText.select();
    copyText.setSelectionRange(0, 99999);
    document.execCommand("copy");
    document.getElementById('copy').innerHTML = 'Copied!'
}