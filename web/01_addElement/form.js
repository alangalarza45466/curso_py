import { $ } from "./logger.js"
import {fruits,addFruits} from "./main.js"
const form=$(".form")

form.onsubmit=(ev)=>{

    ev.preventDefault()
    const formData= new FormData(ev.target)
    const addEle = formData.get('bs')
    console.log(addEle); 
    fruits.push(addEle)
    console.log(fruits)
    addFruits()
}
