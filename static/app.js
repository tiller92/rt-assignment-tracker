// import and breal down and xl file

const file = document.querySelector('#xl-doc')
const form = document.querySelector('#file')
const btn = document.querySelector('#btn')
const test = document.createElement('h1')
const body = document.querySelector('body')


function fileGrab() {
    form.addEventListener("submit", function(e) {
        e.preventDefault()
        path
        console.log(file.value)
    })
}