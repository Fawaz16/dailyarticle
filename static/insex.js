let minidiv = document.querySelector('.minidiv')
let hamburger = document.querySelector('.hamburger')
let closebtn = document.querySelector('.close')
let wrapper = document.querySelector('.wrapper')
let header= document.querySelector('.header')
let atext= document.querySelector('.a2-text')
let over= document.querySelector('.over')
let over1= document.querySelector('.b-text')

hamburger.addEventListener("click",() =>{
    minidiv.style.transform="translateX(0px)";
if (minidiv.style.transform="translateX(0px)") {
    hamburger.style.display="none"
    closebtn.style.display="block"
    wrapper.style.background= "#04006b"
    atext.style.display='none'
    header.style.display='none'
    over.style.display='none'
    over1.style.display='none'
    
}
})
closebtn.addEventListener("click",() =>{
    minidiv.style.transform="translateX(-768px)";
if (minidiv.style.transform="translateX(-768px)") {
    hamburger.style.display="block"
    closebtn.style.display="none"
    wrapper.style.background="rgb(49, 28, 167)"
    atext.style.display='block'
    header.style.display='block'
    over.style.display='block'
    over1.style.display='block'
    
}
})