const container=document.querySelector('.container')
const text =document.querySelector('#text')
const pointer=document.querySelector('.pointer')
const gc=document.querySelector('.gradient-circle')
const totaltime=7500
const breath=(totaltime/5)*2
const hold=totaltime/5

BreathAnimation()

function BreathAnimation(){

  pointer.classList.toggle('toggle-pointer')
  gc.classList.toggle('toggle-gradient')
    text.innerHTML='<p>Breath In!</p>'
    container.className='container grow'

    setTimeout(()=>{
      text.innerText='hold!'

      setTimeout(()=>{
        text.innerText='Breath Out!'
        container.className='container shrink'
      },hold)
    },breath)
}

setInterval(BreathAnimation,totaltime);
