import { $, cE, d } from "./logger.js"
// definir variables

export const fruits = ["manzana", "naranja", "platano"]
const root = $('.main')
const filtter = $(".filtter")

export function addFruits() {
  
  fruits.forEach(el => {
    //crear y agregarla etiqueta html p
    let p = cE('p')
    //agregar el texto a la etiqueta html p
    p.textContent = el
    //agregar el aatributo class a la etiqueta html p
    p.classList.add("fruit")
    root.appendChild(p)
    
    //agregar los elementos de nuestra lista fruits
    //agregar los elementos option a nuestro elemento select(filtter)
    let option = cE("option")
    //agregar el texto a la etiqueta html p
    option.textContent = el
    //agregar el atributo value a la etiqueta html option
    option.setAttribute("value", el)
    filtter.appendChild(option)
  })

}

addFruits()

console.log(filtter)