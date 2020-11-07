const burger=document.querySelector('.burger')
const nav=document.querySelector('.navitems')
const navlinks=document.querySelectorAll('.navitems li')
const ul=document.querySelector('.navitems')
const container=document.querySelector('.container')
const games=document.querySelector('#games')
burger.addEventListener('click',blur)

function toggle(){
container.classList.toggle('blur')
  nav.classList.toggle('nav-active')
  console.log('navactive');
  navlinks.forEach(function(link,index){
    if(link.style.animation){
      link.style.animation=''
    }
    else{
      var c=`NavAnim 0.5s forwards ${index/7+0.5}s`
    link.style.animation=c
    console.log(link.style.animation);
  }
  })
  burger.classList.toggle('toggle')
}
function blur(){
  toggle()
}
ul.addEventListener('click',toggle)
navlinks[0].addEventListener('click',function(){
  games.style.opacity='1'
})
