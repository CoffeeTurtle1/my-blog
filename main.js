var mode = "light";

function dark() {
    if (mode == "dark") {
        mode = "light";
        document.getElementById("darkmode").innerHTML = "Dark Mode";
        document.documentElement.style.setProperty('--background-color', '#ffffff');
        document.documentElement.style.setProperty('--text-color', '#585858');
        document.documentElement.style.setProperty('--title-text-color', '#547aa1');
    } else {
        mode = "dark";
        document.getElementById("darkmode").innerHTML = "Light Mode";
        document.documentElement.style.setProperty('--background-color', '#242424');
        document.documentElement.style.setProperty('--text-color', '#e6e6e6');
        document.documentElement.style.setProperty('--title-text-color', '#5389c0');
    }
}