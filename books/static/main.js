console.log("hello,world")

const copyBtns = [...document.getElementsByClassName('copy-btn')]

console.log(copyBtns)

let previous = null

copyBtns.forEach(btn=> btn.addEventListener('click',()=>{
    console.log('click')
    const details = btn.getAttribute('data-book')
    console.log(details)

    // copy text
    navigator.clipboard.writeText(details)
    btn.textContent= 'copied'

    navigator.clipboard.readText().then(clipText=>{
        console.log(clipText)
        btn.textContent= `copied ${clipText}`
    })

    if (previous) {
        previous.textContent = 'click'
    }
    previous =btn

}))