import { $ } from "./logger.js"
const form = $(".form")

form.onsubmit = (ev) => {
  ev.preventDefault()
  const formData = new FormData(ev.target)
  const addData = formData.get("bs")
  console.log(addData);
  addElement(addData)
}