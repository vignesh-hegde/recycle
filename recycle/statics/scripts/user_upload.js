bueger_toggle = false; 
function bueger(){
    temp = [['0px',"45","0","#ffff"],["30px","0","-100%","#ffff"]]
    temp = temp[bueger_toggle?1:0];
    document.getElementById("middle").style.width = temp[0];
    document.getElementById("top").style.cssText = "transform:rotate(-"+temp[1]+"deg); transform-origin : bottom right;";
    document.getElementById("bottom").style.cssText = "transform:rotate("+temp[1]+"deg); transform-origin : top right;";  
    document.getElementById("nav-links").style.right = temp[2];
    document.getElementsByClassName("header")[0].style.background = temp[3];
    bueger_toggle = ! bueger_toggle;
}

const header = document.querySelector('header')
const brand = document.querySelector('.brand')
const hov = document.getElementsByClassName('nav-link')
const logo = document.getElementById('bLogo')
var style = getComputedStyle(document.body)

window.onscroll = function(){
    var top = window.scrollY;
    if(top>=70){
        header.classList.add('active')
        brand.classList.add('brnd')
        logo.style.transform = "rotate(240deg)"
        for(i=0;i<hov.length;i++){
            hov[i].style.color=style.getPropertyValue('--color-dark')
        }
        
        
    }else{
        header.classList.remove('active')
        brand.classList.remove('brnd')
        logo.style.transform = "rotate(0deg)"
        for(i=0;i<hov.length;i++){
            hov[i].style.color=style.getPropertyValue('--color-dark')
        }
    }
}


