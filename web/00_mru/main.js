import { d,$ } from "./logger.js"

const fruit = ["manzana", "naranja", "sandia"]

function addElement(dt) {
  const sect = $(".main-section")
  fruit.push(dt)
  
  fruit.forEach(element => {
    let p = d.createElement("p")
    p.textContent = element
    p.classList.add("fruit")
    sect.appendChild(p)
  })
}
addElement("")