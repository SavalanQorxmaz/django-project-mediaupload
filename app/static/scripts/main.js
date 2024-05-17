
import './carousel.js'
import './advanced.js'
import './header.js'
import './contacts.js'

const analog = document.getElementById("analog");
const hour = document.getElementById("hour");
const minute = document.getElementById("minute")
const second = document.getElementById("second")

// document.body.style.backgroundColor = 'gray'
console.log(window.innerWidth)
window.addEventListener('resize',()=>{
    window.innerWidth<772?document.body.style.backgroundColor = 'yellow':document.body.style.backgroundColor = 'green'
    
})


let deg = 0;
for(let i=0;i<30;i++){


    
    let line = document.createElement("div");
    line.classList.add("line")
 
    line.style.transform = `rotateZ(${deg}deg)`;
    
analog.appendChild(line)

  for(let j=0;j<2;j++){
    let lineChild = document.createElement("div");
    if(i%5 == 0){
         lineChild.classList.add("long-line");
         
     }else{
         lineChild.classList.add("short-line")
     }
 line.appendChild(lineChild)
  }

 
    deg +=6
}




function analogC(){


    const date = new Date();
    let milliSeconds = date.getMilliseconds();
    let seconds = date.getSeconds();
    let minutes = date.getMinutes();
    let hours = date.getHours();
    let year = date.getFullYear();
    let month = date.getMonth();
    let monthDay = date.getDate();
    let weekDay = date.getDay();

    // analog clock
    let secondPosition = 360 / 60 * seconds + 360 /60000 *milliSeconds;
    let minutePosition = 360 / 60 * minutes + seconds / 10;
    let analogHours = hours;
    if(hours >11){
        analogHours -= 12;
    }
    let hourPosition = 360 / 12 * analogHours + minutes / 12 * 6;

    hour.style.transform = `rotateZ(${hourPosition}deg)`
    minute.style.transform = `rotateZ(${minutePosition}deg)`
    second.style.transform = `rotateZ(${secondPosition}deg)`



requestAnimationFrame(analogC)

}

requestAnimationFrame(analogC)


window.addEventListener("load", (event) => {
    document.querySelector('.load-cover').classList.add('hidden')
  });

function clickMe(){
    alert('clicked')
    console.log('clicked')
}


// window.addEventListener('click',(e)=>{
//     e.preventDefault()
//     // e.stopPropagation()
//     if(e.target.tagName== 'A'){
//         document.documentElement.scrollTop = document.getElementById(`${e.target.href.split('#')[1]}`).offsetTop-80

//         console.log(document.getElementById(`${e.target.href.split('#')[1]}`).offsetTop)
//         // document.documentElement.scrollTop = document.documentElement.scrollTop + 80
//     }
//     console.log(e.target.tagName === 'A')
    
    
// })